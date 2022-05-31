#include <Adafruit_NeoPixel.h>
#define PIN 6
#define NUMPIXELS 6
#define DELAYVAL 50

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

byte r, g, b;
int index;

void setup() {
  pixels.begin();
  pixels.clear();
  pixels.show();
  Serial.begin(19200);
}

void loop() {
  index = 0;
  while (Serial.available() < 3);
  delay(DELAYVAL);
  while (Serial.available() >= 3) {
    r = Serial.read();
    g = Serial.read();
    b = Serial.read();
    pixels.setPixelColor(index, r, g, b);
    index += 1;
  }
  pixels.show();
  Serial.write(r);
}
