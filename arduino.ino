#include <Adafruit_NeoPixel.h>
#include <math.h>

#define MIC_PIN A0
#define LED_PIN 6
#define SWITCH_PIN 7
#define NUM_PIXELS 48 // 6 sticks × 8 LEDs

Adafruit_NeoPixel strip(NUM_PIXELS, LED_PIN, NEO_GRB + NEO_KHZ800);

float smoothedVolume = 0;

void setup() {
  pinMode(SWITCH_PIN, INPUT_PULLUP); // Switch is connected between D7 and GND
  strip.begin();
  strip.show();
  Serial.begin(9600);
}

void loop() {
  // Read ON/OFF switch (LOW = ON, HIGH = OFF)
  bool isOn = digitalRead(SWITCH_PIN) == LOW;

  if (isOn) {
    int micValue = analogRead(MIC_PIN);
    int amplitude = abs(micValue - 512);

    smoothedVolume = (smoothedVolume * 0.92) + (amplitude * 0.08);

    float normalized = smoothedVolume / 512.0;
    float scaled = pow(normalized, 1.8);
    int brightness = constrain(scaled * 255, 0, 255);

    int red = (brightness * 100) / 255;
    int green = 0;
    int blue = brightness;

    for (int i = 0; i < NUM_PIXELS; i++) {
      strip.setPixelColor(i, strip.Color(red, green, blue));
    }
    strip.show();
  } else {
    // Turn off all LEDs when switch is off
    for (int i = 0; i < NUM_PIXELS; i++) {
      strip.setPixelColor(i, 0);
    }
    strip.show();
  }

  delay(10);
}
