# Description

This project functions as a cookie snatcher utilizing Python subprocesses and sub-requests. **No root privileges are required.** 

I improved and added my own functionality by integrating an ESP32-S3 USB device that automatically deploys and executes the payload on the target machine, exfiltrating data via a Discord webhook. This allows the information to be accessed remotely while leaving a minimal operational footprint. 

### Future Ideas / Roadmap:
* **Metadata Snatching:** Pulling location/geographical metadata.
* **Archive Exfiltration:** Compressing target text files into a `.zip` archive before exfiltrating them through the Discord webhook.

*Note: Yes, AI was used to help structure the JSON payload handling since I haven't worked with JSON in a while, but the core implementation and logic were built from scratch.*

---

# Setup

* **Hardware:** Custom ESP32-S3 USB stick (tested with the LILY-GO T3 Dongle).
* **Target Environment:** Python installed on the host computer (the payload utilizes a temporary Python virtual environment for security and dependency management).
* **Firmware:** Arduino code (C++, provided in the repo).
* **Dependencies:** Uses the official Espressif GitHub core for the ESP32 Arduino environment.

---

# Operation

To deploy and run this code securely:

1. Clone this repository and **keep it private** so your Discord webhook URL is not exposed publicly.
2. Add your personal Discord webhook URL into your Python script (`xenon.py`).
3. Update the Arduino code (`.ino`) to point to your own raw GitHub URL rather than the default template.
4. Flash the code to your ESP32-S3 and deploy.
