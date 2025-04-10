import os
import time
import replicate
from dotenv import load_dotenv
from picamera2 import Picamera2
from gpiozero import Button, LED
import requests
import re  # For text cleanup

# === CONFIG ===
BUTTON_PIN = 19  # GPIO 19 = Physical Pin 35
LED_PIN = 26     # GPIO 26 = Physical Pin 37

# === LOAD ENV ===
load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

# === GPIO SETUP ===
button = Button(BUTTON_PIN)
led = LED(LED_PIN)

# === FILE PATHS ===
desktop_path = "/home/Verse-2/Desktop"
image_path = os.path.join(desktop_path, "captured_image.jpg")
poem_path = os.path.join(desktop_path, "generated_poem.txt")
audio_path = os.path.join(desktop_path, "poem_audio.wav")

# === CAMERA ===
picam2 = Picamera2()

# === CAPTURE FUNCTION ===
def capture_photo_with_led_countdown():
    print("Starting 7-second countdown...")
    picam2.start()  # Start early so capture is instant post-countdown

    # Slow blink: 7 to 4
    for t in range(7, 3, -1):
        print(f"{t}...")
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

    # Fast blink: 3 to 0
    for t in range(3, -1, -1):
        print(f"{t}...")
        for _ in range(2):
            led.on()
            time.sleep(0.15)
            led.off()
            time.sleep(0.15)

    print("Capturing image...")
    led.on()  # LED stays on during image capture
    picam2.capture_file(image_path)
    picam2.stop()
    led.off()
    print(f"Image saved at: {image_path}")

# === SCENE DESCRIPTION ===
def get_scene_description():
    print("Generating scene description...")
    result = replicate.run(
        "yorickvp/llava-13b:80537f9eead1a5bfa72d5ac6ea6414379be41d4d4f6679fd776e9535d1eb58bb",
        input={
            "image": open(image_path, "rb"),
            "prompt": "Describe this scene in detail, including facial expressions, body language, mood, atmosphere, background elements, and any implied social or emotional context."
        }
    )
    return "".join(result) if hasattr(result, '__iter__') else str(result)

# === POEM GENERATION ===
def generate_poem(description):
    print("Generating poem...")
    prompt = f"""
Write an 8-line free verse poem inspired by the scene described below.
Use subtle humor, observational wit, and emotional texture. The tone should feel personal and slightly ironic. Avoid cliches. Use gender-neutral pronouns.

Do not include characters like (*), and avoid bold or italic formatting in the poem and poem title.

Scene description: {description}

Begin with the poem's title on the first line, followed by the poem.
"""
    result = replicate.run(
        "deepseek-ai/deepseek-v3",
        input={"prompt": prompt, "temperature": 0.7, "max_new_tokens": 256}
    )
    return "".join(result) if isinstance(result, (list, tuple)) else str(result)

# === TEXT TO SPEECH ===
def text_to_speech(poem_text):
    print("Converting poem to speech...")
    output = replicate.run(
        "jaaari/kokoro-82m:f559560eb822dc509045f3921a1921234918b91739db4bf3daab2169b71c7a13",
        input={
            "text": poem_text,
            "speed": 1,
            "voice": "af_nicole"
        }
    )
    audio_url = output[0] if isinstance(output, list) else output

    print(f"Downloading audio from: {audio_url}")
    response = requests.get(audio_url)
    with open(audio_path, "wb") as f:
        f.write(response.content)
    print(f"Audio saved to: {audio_path}")

# === PLAY AUDIO ===
def play_audio():
    print("Playing audio through 3.5mm jack...")
    os.system(f"aplay -D plughw:0,0 '{audio_path}'")

# === MAIN FUNCTION ===
def main():
    while True:
        print("Waiting for the previous button press to be released...")
        button.wait_for_release()
        print("Ready! Press the arcade button to begin.")
        button.wait_for_press()

        capture_photo_with_led_countdown()
        description = get_scene_description()
        poem = generate_poem(description)

        with open(poem_path, "w") as f:
            f.write(poem)

        print("\n=== Generated Poem ===\n")
        print(poem)
        print(f"\nPoem saved at: {poem_path}")

        # Sanitize poem for TTS
        cleaned_poem = re.sub(r"[*_~`]", "", poem)
        text_to_speech(cleaned_poem)
        play_audio()

        print("Done! Waiting for the next button press...\n")

# === START ===
main()
