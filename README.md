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

## License
This project is open-source and licensed under the [MIT License](LICENSE).

---

## Acknowledgments
Thanks to the open-source community and contributors of Raspberry Pi, Arduino, Adafruit, and Replicate AI models.

