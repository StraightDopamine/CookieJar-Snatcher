# Description

This project functions as a cookie snatcher utilizing Python subprocesses and sub-requests. **No root privileges are required.** 

I improved and added my own functionality by integrating an ESP32-S3 USB device that automatically deploys and executes the payload on the target machine, exfiltrating data via a Discord webhook. This allows the information to be accessed remotely while leaving a minimal operational footprint. 

### Future Ideas / Roadmap:
* **Metadata Snatching:** Pulling location/geographical metadata.
* **TinyFlask or FastAPI:** So I was thinking, instead of Discord Webhook which _can_ get you banned :( instead we can use FastAPI or TinyFlask to transfer the data more effectively.

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

1. So I made some major updates with the code where you no longer need to clone it
2. Now all you do is copy and flash the code from the arduino into the USB with your discord webhook attached of course
3. Thats it your ready to go without anything new.

Note: So this Arduino one liner was primarily me with the env and curl but the piping through the discord webhook in Arduino was not mine I had never thought of it until I ran into token issues with private repos but its all fixed now
