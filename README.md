# Asterisk – A Sentient Camera

---

## Components

The project features two separate circuits: one powered by the Raspberry Pi for AI interaction  
and poem generation, and another using an Arduino to run a real-time audio-reactive lighting system.

---

### Circuit 01

#### ● Raspberry Pi 4  
Raspberry Pi 4 is a compact, affordable single-board computer that is powerful enough  
to run full operating systems like Linux, yet small enough to fit in embedded systems.  
It offers significant upgrades over previous models, with a faster CPU, more RAM options,  
dual HDMI outputs, and USB 3.0 support.  

We are using the Pi 4 for its ability to handle multiple tasks in real-time — like capturing  
camera input, generating poems using AI models, and playing audio — all without  
needing an external computer. While it's not the most power-efficient or compact  
model, the Pi 4 gives us the processing capacity needed for running advanced AI tasks  
locally.  

If you're setting up your Raspberry Pi 4 with an external monitor, keyboard, and mouse,  
we recommend the official Raspberry Pi 4 Desktop Kit, which includes everything  
needed to get started — including micro-HDMI cables for connecting to a display.  
[https://www.raspberrypi.com/products/raspberry-pi-4-desktop-kit/](https://www.raspberrypi.com/products/raspberry-pi-4-desktop-kit/)

![Raspberry Pi 4](https://www.generationrobots.com/19375-product_cover/raspberry-pi-4-model-b.jpg)


---

#### ● Raspberry Pi Camera Module V2  
The Raspberry Pi Camera Module V2 is an official high-quality camera add-on designed  
for Raspberry Pi boards. It features an 8-megapixel Sony IMX219 sensor and can  
capture still images at 3280 x 2464 resolution and record HD video at 1080p30,  
720p60, and 640x480p90. It's compact, lightweight, and connects directly to the Pi via  
the CSI (Camera Serial Interface) port using a ribbon cable.  

Its reliable image quality and native integration with Raspberry Pi make it a great fit for  
real-time computer vision tasks. It’s important to enable the camera interface via the  
Pi's configuration settings before use, and ensure the ribbon cable is securely  
connected — the camera is delicate and sensitive to handling.  

![Raspberry Pi Camera Module V2](https://m.media-amazon.com/images/I/41AbFOdJqQL.jpg)

---

#### ● Arcade Button Chrome Silver Plated  
The Arcade Button is a tactile, spring-loaded button commonly used in DIY electronics  
and gaming projects for its satisfying click and retro aesthetic. It’s durable, easy to  
mount, and visually striking thanks to its chrome finish. Internally, it operates as a  
simple momentary switch — when pressed, it completes a circuit, sending a signal to  
the connected microcontroller or computer.  

We used the arcade button as the user input trigger: pressing it starts the entire  
interaction sequence — activating the camera, generating a poem, and playing audio.  
It’s connected to the Raspberry Pi’s GPIO pins, and due to its robust size and clear  
physical feedback, it invites interaction and enhances the artifact’s tactile quality.  

![Arcade Button](images/Arcade%20Button.png)

---

#### ● Jumbo Blue LED  
The Jumbo Blue LED is a large, bright light-emitting diode typically used in interactive  
projects for signaling or visual feedback. We use the Jumbo Blue LED as a visual  
countdown indicator. Once the arcade button is pressed, the LED begins blinking to  
signal that the system is processing. It connects to one of the Raspberry Pi’s GPIO pins  
through a current-limiting resistor to prevent burnout.  

![Jumbo Blue LED](https://5.imimg.com/data5/ECOM/Default/2024/7/436918091/IG/XF/LX/56767488/undefinedimg11687609097965-png-500x500.png)

---

#### ● AYL Mini Speaker System  
The AYL Mini Speaker System is a compact, portable audio speaker designed for use  
with smartphones, laptops, and embedded systems like the Raspberry Pi. Despite its  
small size, it delivers surprisingly clear and loud sound, making it ideal for  
space-constrained interactive installations that still need effective audio output.  

The AYL Mini Speaker plays the AI-generated poem using text-to-speech audio. It  
connects to the Raspberry Pi via the 3.5mm audio jack and is powered by its built-in  
rechargeable battery. Its plug-and-play nature makes integration seamless.  

![AYL Mini Speaker](images/AYL%20Mini%20Speaker%20System.png)

---

### Circuit 02

#### ● Arduino Uno  
The Arduino Uno is a popular open-source microcontroller board based on the  
ATmega328P. It’s designed for ease of use in prototyping and physical computing,  
offering 14 digital I/O pins, 6 analog inputs, and simple USB programming. It’s ideal for  
controlling sensors, LEDs, motors, and other hardware.  

We use the Arduino Uno to power the audio-reactive lighting system, which responds in  
real time to the poem's playback. Its ability to handle analog audio signals and drive  
visual outputs independently makes it a perfect complement to the Raspberry Pi,  
allowing both circuits to run specialized tasks in parallel.  

![Arduino Uno](https://5.imimg.com/data5/OU/HS/GC/SELLER-20589996/arduino-uno-500x500.jpg)

---

#### ● Electret Microphone Amplifier - MAX4466 with Adjustable Gain  
The MAX4466 is a low-noise, high-gain electret microphone amplifier with adjustable gain control.  
It includes a built-in potentiometer that allows you to fine-tune the sensitivity for your needs.  
This module is great for capturing clear and consistent audio, even in variable sound environments.  

We use the MAX4466 in combination with the **Arduino Uno** for our interactive lighting setup.  
It captures the sound of the AI-generated, spoken poem and produces a responsive analog signal.  
This signal reflects the audio volume and drives the LED animations in real time.  
The LEDs visually respond to rhythm, intensity, and tone, enhancing the poetic performance experience.  
This creates a rich, immersive fusion of sound and light that evolves with every word.

![Electret Microphone Amplifier - MAX4466 with Adjustable Gain](https://i.ebayimg.com/images/g/u~EAAOSwnbZYFHi7/s-l400.jpg)

---

#### ● NeoPixels Sticks  
The NeoPixel Stick – 8 x 5050 RGB LED with Integrated Drivers is a compact LED strip  
featuring 8 individually addressable RGB LEDs. Each LED can display 24-bit color, and  
the entire stick is controlled using a single digital pin, thanks to the built-in WS2812  
drivers.  

We use six NeoPixel Sticks in the Arduino-powered audio-reactive circuit to create  
vibrant, real-time visual responses to the spoken poem. The sticks react to the audio  
levels captured by the MAX9815 microphone, lighting up and animating in patterns that  
reflect the tone of the poem. 

![NeoPixels Sticks](https://90a1c75758623581b3f8-5c119c3de181c9857fcb2784776b17ef.ssl.cf2.rackcdn.com/656499_493114_01_front_comping.jpg)

---

#### ● On-Off Rocker Switch  
The On-Off Rocker Switch is a simple, durable switch used to manually control the  
power supply to electronic circuits. It features a stable, click-based toggle mechanism  
and is commonly mounted into enclosures for easy access. The rocker switch acts as a  
power control, allowing us to safely turn ‘Circuit 02’ on or off without unplugging wires.  

![On-Off Rocker Switch](https://mgispeedware.com/wp-content/uploads/2019/12/neon_rocker_red.jpg)

---

#### ● Power Banks  
Power banks are portable battery packs designed to supply power to electronic devices  
on the go. We use power banks to make the system fully mobile and self-contained,  
allowing it to operate without needing a wall outlet. The Raspberry Pi requires a  
high-capacity, stable 5V/3A power bank to run smoothly, while a separate power bank  
can be used for the Arduino and LED circuit to prevent power fluctuations.  

![Power Banks](https://mobileimages.lowes.com/productimages/c95d846f-30c7-4886-afa9-3f757eca19d8/42192142.jpg?size=xl)

---

## Software

### ● Raspberry Pi System  
- **Raspberry Pi OS**: Lightweight Linux-based operating system for the Pi.  
- **Python 3**: Main programming language used to run the entire interaction logic.  

### ● Arduino Audio-Reactive System  
- **Arduino IDE**: Used to write and upload code to the Arduino Uno.  
- **Adafruit NeoPixel Library**: Controls the NeoPixel LED animations.  
- **Custom Arduino Sketch**: Reads sound input from the MAX9815 mic and controls  
  the lighting effects in real time.  

### ● AI Models via Replicate  
- **LLaVA-13B**: Generates a scene description from the captured image.  
- **DeepSeek V3**: Creates an 8-line poem from the scene description.  
- **kokoro-82m (Jaaari)**: Converts poem text into natural-sounding spoken audio.  

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

