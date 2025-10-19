**🎨 Color Detector (PyQt5 + PIL)**

A lightweight desktop color picker built with PyQt5 and Pillow (PIL).
This tool allows you to detect, preview, and copy any color from your screen in HEX, RGB, or HSV format — simply by hovering your mouse and pressing Enter.

🧭 Features

🎯 Real-time color tracking — hover over any part of your screen to detect color.

🖱️ Keyboard shortcut:

Press Enter to start/stop color tracking.

**🎨 Multiple color formats:**

HEX (#rrggbb)

RGB ((r,g,b))

HSV ((h,s,v))

📋 Copy to clipboard in any format (via dropdown).

🧩 User-friendly PyQt5 GUI with clear color preview box.

💡 Info popup on startup explaining how to use the app.

🖥️ How It Works

Launch the app.

Press Enter to activate color tracking.

Move your mouse over any pixel on the screen.

Press Enter again to stop and lock the color.

Choose your preferred format (HEX / RGB / HSV).

Click “Copy to Clipboard” to copy the color code.

**📦 Installation**
1. Clone the repository
git clone https://github.com/yourusername/color-detector.git
cd color-detector

2. Install dependencies

Make sure you have Python 3.x installed, then run:

pip install PyQt5 Pillow pyperclip

3. Run the app
python color_detector.py

**🧩 Project Structure**
color-detector/
│
├── color_detector.py     # Main application file
├── README.md             # Documentation
└── LICENSE               # (Optional) License file

**🧠 Technical Overview**
Component	Description
GUI Framework	PyQt5 (QWidget, QLabel, QPushButton, etc.)
Screen Capture	PIL.ImageGrab (captures pixel color)
Clipboard Access	pyperclip
Color Formats	HEX, RGB, HSV
Shortcut Key	Enter key toggles color tracking
Refresh Rate	10ms (via QTimer)
📸 Screenshot Example

(Add your screenshot here)
Example:

![Color Detector Screenshot](screenshot.png)

#⚙️ Requirements

Python 3.7 or higher

PyQt5

Pillow (PIL)

Pyperclip

**🚀 Future Enhancements**

Color palette history

Custom hotkey selection

Option to pick colors from screenshots or images

Copy all formats at once

**🧑‍💻 Author**

Mobina RZ
🎨 Developer & Educator
📍 Mashhad, Iran
💡 Focused on creative Python tools and educational software

