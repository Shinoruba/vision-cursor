# 🎯 VisionCursor: Real-Time Hand Gesture Mouse Control

VisionCursor is a Python-based application that transforms your webcam into a virtual mouse controller.  
It tracks your finger to move the cursor and recognizes hand gestures for actions like clicking, navigating pages, and adjusting volume, all in real time! 🖐️🖥️

## ✨ Features

- 🖱️ **Cursor Control**: Move your PC mouse cursor simply by moving your index finger.
- 🤏 **Gesture Recognition**: Trigger click, double-click, and page navigation through hand gestures.
- ✋ **Dual-Hand Functionality**: Control the cursor with one hand, and adjust the volume/ettings with the other.
- ⚡ **Real-Time Processing**: Fast and smooth hand tracking using efficient computer vision techniques.

---

## 🚀 Getting Started
Follow these simple steps to clone and run the project:

### 1. Clone the repository
```bash
git clone https://github.com/Shinoruba/vision-cursor.git
cd vision-cursor
```

### 2. Create and activate a virtual environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the required packages
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```

Make sure your webcam is connected and active! 📸

---

## 🛠️ Language, Libraries, and Tools Used
- **Python** 🐍 = Easy to read/interpret language, ideal for computer vision tasks.
- **MediaPipe** 🎯 = Real-time hand tracking by Google; extremely fast and optimized even for low-end PC systems.
- **OpenCV** 🖼️ = The leading library for image and video processing; used to access webcam frames and handle image transformations.
- **PyAutoGUI** 🎮 = Allows the Python script to control the mouse and keyboard seamlessly.
- **pynput** ⌨️ = An alternative input control library for extended keyboard/mouse actions.
- **NumPy** 📊 = For efficient numerical operations and matrix transformations.

These libraries together enable real-time, accurate, and resource-light performance.

## 📁 Project Structure
vision-cursor/
- ├── main.py                     # Main application entrypoint
- ├── hand_tracker.py             # Hand detection and landmark extraction using MediaPipe
- ├── cursor_controller.py        # Uses right index fingertip to control system cursor
- ├── gesture_controller.py       # Uses left-hand pinch/spread gestures to change system volume.
- ├── gesture_recognizer.py       # Classifies left-hand gestures like left/right click, double-click, scroll up/down.
- ├── mouse_controller.py         # Executes real mouse actions like clicking and scrolling using pyautogui.
- ├── utils.py                    # Utility file for helper functions like distance calculations and gesture checks.
- ├── requirements.txt            # Ensures all dependencies are installed in one command.
- └── README.md                   # You’re reading it right now silly! 😋

### 🗂️ Description of Each File
- `main.py`: 	The entry point of the application. Initializes the camera, loads modules, tracks cursor with the right index fingertip, and detects volume gestures with the left hand.
- `hand_tracker.py`: Handles all functionality related to detecting and tracking hands and fingers using MediaPipe.
- `cursor_controller.py`: Maps the right hand’s index finger movement to system cursor position using PyAutoGUI.
- `gesture_controller.py`: Detects pinch/spread gestures from the left hand to trigger system volume adjustments.
- `gesture_recognizer.py`: Detects gestures like left/right click, double-click, scroll up/down.
- `mouse_controller.py`: Executes real mouse actions like clicking and scrolling using pyautogui.
- `utils.py`: A utility file with helper functions (e.g., calculating distances between fingers, smoothing cursor motion).
- `requirements.txt`: Lists all required Python libraries for easy environment setup.
- `README.md`: You’re reading it right now silly! 😋

**NOTE**: I am using semantic versioning (SemVer) for assigning version numbers to each file, why? It looks cool. The format is: `MAJOR.MINOR.PATCH`.

---

## 🤝 Contributing
Contributions are welcome!
If you find a bug or have a suggestion for improvement, feel free to open an Issue or submit a Pull Request.
Steps to Contribute:
1. Fork the repository 🍴
2. Create your feature branch (git checkout -b feature/AmazingFeature) 🚀
3. Commit your changes (git commit -m 'Add some AmazingFeature') ✅
4. Push to the branch (git push origin feature/AmazingFeature) 🔥
5. Open a Pull Request 📬

## 📜 License
This project is licensed under the MIT License, go crazy with it 💀 and by that- I mean improve the codebase as you see fit.

## 👨‍💻 Author
- Name: Yazan M. Homssi
- GitHub: Shinoruba
- Professional Email: homssi002@gmail.com
- University Email: yazan_homssi@dlsu.edu.ph
- LinkedIn: https://www.linkedin.com/in/yazan-homssi/