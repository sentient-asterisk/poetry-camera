# Sentient Artefact

An interactive multimedia experience that generates poetry from a scene and responds with light and sound. Built using Raspberry Pi and Arduino, the artefact combines AI with tactile and audio-reactive interaction.

---

## Components

The project consists of **two circuits**:
- **Circuit 01:** Powered by Raspberry Pi for AI interaction and poem generation.
- **Circuit 02:** Powered by Arduino for real-time audio-reactive lighting.

---

## 📷 Circuit 01 – Raspberry Pi System

### Raspberry Pi 4
A powerful SBC used for real-time tasks such as:
- Capturing images
- Generating poems via AI
- Playing audio output

> **Recommended:** Raspberry Pi 4 Desktop Kit for complete setup.

### Raspberry Pi Camera Module Rev 1.3
- 8MP Sony IMX219 sensor
- Captures high-quality images and HD video
- Connected via CSI ribbon cable

### Arcade Button (Chrome Silver Plated)
- Momentary switch triggering the interaction sequence
- Connected to GPIO pins
- Tactile and visually engaging

### Jumbo Blue LED
- Visual countdown indicator
- Blinks after button press to signal processing
- Connected through GPIO with a current-limiting resistor

### AYL Mini Speaker
- Compact, loud audio output
- Plays AI-generated poem via 3.5mm jack
- Rechargeable and portable

---

## 💡 Circuit 02 – Arduino System

### Arduino Uno
- Controls audio-reactive lighting
- Processes analog signals from microphone
- Runs lighting animations in sync with poem audio

### Electret Microphone Amplifier (MAX9814)
- Captures real-time sound levels with AGC
- Outputs analog volume signal to Arduino

### NeoPixel Sticks
- 8x5050 RGB LEDs per stick
- 6 sticks used for dynamic lighting effects
- Controlled via single digital pin using WS2812 protocol

### On-Off Rocker Switch
- Manual power control for Circuit 02
- Ensures safe power management

### Power Banks
- Ensures full mobility
- One power bank for Pi (5V/3A)
- One for Arduino + LEDs to avoid power fluctuation

---

## 🧠 Software

### Raspberry Pi
- **OS:** Raspberry Pi OS (Linux-based)
- **Language:** Python 3

### Arduino
- **IDE:** Arduino IDE
- **Libraries:** Adafruit NeoPixel Library
- **Sketch:** Custom script for sound-reactive lighting

### AI Models (via [Replicate](https://replicate.com))
- **LLaVA-13B:** Generates scene description
- **DeepSeek V3:** Generates 8-line poem
- **kokoro-82m:** Converts poem text to spoken audio

---

## 💬 Interaction Flow

1. **User presses arcade button**
2. LED countdown starts
3. Camera captures image
4. AI generates description → poem → audio
5. Poem played through speaker
6. Arduino reacts to audio with dynamic lights

---

## System Overview

### 1. Set Up and Test Your Raspberry Pi and Camera

**Connect the Camera Module**  
Attach the Camera Module to the CSI (Camera Serial Interface) port on your Raspberry Pi.

**Insert SD Card**  
Use a microSD card with a fresh install of Raspberry Pi OS and insert it into your Pi.

**Connect to a Monitor**  
Plug your Raspberry Pi into a monitor using a mini HDMI cable.

**Power Up the Pi**  
Connect the power supply. A green LED should turn on, and the startup screen should appear on the monitor.

**Open the Terminal**  
Once the Pi boots up, open the Terminal to configure system settings.

**Configure Camera & Serial Settings**  
In the Terminal, run:

```bash
sudo raspi-config
```

Then adjust the following:  
Enable Serial Port (allows communication with external devices like printers)  
Disable Serial Console (prevents it from using the same port)

**Restart the Pi**  
Apply the changes and reboot the system if prompted.

---

### 2. Set Up the AI

Create an account on Replicate and generate an API token.

In your project directory, create a .env file to store sensitive info:

```bash
nano .env
```

Add your token like this:

```env
REPLICATE_API_TOKEN=your_token_here
```

---

### 3. Run Asterisk End-to-End

**Connect the Arcade Button and LED**  
Wire the arcade button and jumbo LED to GPIO pins 27–40 on the Raspberry Pi.

**Start the Asterisk script**  
In the terminal, run:

```bash
python main.py
```

**Trigger the Interaction**  
Press the arcade button to begin. The LED will blink, indicating a short countdown before the photo is captured.

**Experience the Output**  
After the image is taken, a poem is generated and spoken aloud—completing the interaction.

---

### 4. Automatically Run Asterisk on Startup

To make the Asterisk script launch automatically when the Raspberry Pi boots up, set up a cron job:

**Open your crontab**  
In the terminal, type:

```bash
crontab -e
```

**Add this line at the bottom** (replace the path if your script is in a different folder):

```bash
# Run Asterisk script at startup
@reboot python /home/pi/asterisk/main.py >> /home/pi/asterisk/errors.txt 2>&1
```

This line tells the Pi to run your script on boot and log any errors to errors.txt for debugging.

**Important Notes**  
Use absolute file paths.  
Double-check that your username and directories are correct.

**Reboot to test**

```bash
sudo reboot
```

---

### 5. Stay Connected to Wi-Fi

Your Raspberry Pi must stay connected to Wi-Fi at all times for Asterisk to function properly.

The system relies on internet access to:  
Send images to Replicate's AI models  
Receive the generated poem and spoken audio

Without Wi-Fi, the camera can’t process or generate any poems.

---

## License
This project is open-source and licensed under the [MIT License](LICENSE).

---

## Acknowledgments
Thanks to the open-source community and contributors of Raspberry Pi, Arduino, Adafruit, and Replicate AI models.

