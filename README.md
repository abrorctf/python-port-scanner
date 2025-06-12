📬 Author
Abror Hamidov
Cybersecurity Learner
Linkedin link - www.linkedin.com/in/abror-hamidov

# python-port-scanner
basic beginner friendly script written in python syntax for scanning ports.

⚠️ Disclaimer: This tool is for educational purposes only. Scanning ports on systems you do not own or have explicit permission to scan may be illegal in your country. Always get authorization first.

# 🔍 Python Network Port Scanner

This is a simple yet powerful **multi-threaded port scanner** built using Python. The script scans a target IP address or domain to identify **open ports** and their associated **services**. This is a great beginner project for anyone interested in networking, cybersecurity, or Python development.

---

## 🧠 Features

- Accepts a **domain name or IP address** as input
- Converts the hostname to IP using `socket.gethostbyname()`
- Offers two scanning modes:
  - Scan **all ports** (1–65535)
  - Scan only **well-known ports** (1–1024)
- Uses **multi-threading** for faster scanning
- Detects and displays **open ports** and their corresponding **services**
- Handles common socket and input errors gracefully

---

## 🛠️ Technologies Used

- Python 3.x
- `socket` module – for networking
- `threading` – to run scans in parallel
- `datetime` – to measure scan time
- `sys` – for command-line argument parsing

---

## 📦 How to Use

### 🔗 Requirements
- Python 3.x installed on your system

### ▶️ Running the Script
```bash
python scanner.py <target>


