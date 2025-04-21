# 🔑 Keylogger (For Educational Use Only)

A simple keylogger built in Python for **educational and ethical hacking purposes**. This project demonstrates how keystroke logging works for security researchers, developers, and students studying cybersecurity.

> ⚠️ **Disclaimer**: This software is intended strictly for **authorized testing**, **self-education**, and **research purposes**. Misuse of this tool is **illegal** and unethical. Always obtain **explicit permission** before running on any system you do not own.

---

## 📌 Features

- Logs all keystrokes typed on the keyboard.
- Optionally writes keystrokes to a log file.
- Can run in the background silently.
- Cross-platform support (Windows, macOS, Linux).

---

## 📂 Project Structure

```
keylogger/
├── keylogger.py          # Main keylogging script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 💻 Installation

### 🔧 Requirements
- Python 3.6+
- [pynput](https://pypi.org/project/pynput/)

### 📦 Install Dependencies

install manually:

```bash
pip install pynput
```

---

## 🚀 Usage

```bash
python keylogger.py
```

To log output to a file:

```bash
python keylogger.py --output logs.txt
```

To stop the script, press `Ctrl+C` in the terminal.

---

## ✅ Example Output

```
[+] Key pressed: a
[+] Key pressed: b
[+] Key pressed: Space
[+] Key pressed: Enter
```

---

## 🔐 Ethical Use Guidelines

- ✅ Only run on machines **you own** or have **explicit permission** to test.
- ❌ Do not use to collect sensitive or personal information.
- ✅ Use in controlled lab environments for learning cybersecurity techniques.
- ❌ Never deploy in production or on unsuspecting users/systems.

---

## 📜 License

MIT License — feel free to modify and expand this project for your **ethical hacking** studies or **security research**.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the logger, add features, or enhance security practices.
