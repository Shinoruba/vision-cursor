# 🎯 VisionCursor: Real-Time Hand Gesture Mouse Control

VisionCursor is a Python-based application that transforms your webcam into a virtual mouse controller.  
It tracks your finger to move the cursor and recognizes hand gestures for actions like clicking, navigating pages, and adjusting volume — all in real time, without any physical device needed! 🖐️🖥️

## ✨ Features

- 🖱️ **Cursor Control**: Move your PC mouse cursor simply by moving your index finger.
- 🤏 **Gesture Recognition**: Trigger click, double-click, and page navigation through easy-to-do hand gestures.
- ✋ **Dual-Hand Functionality**: Control the cursor with one hand and adjust volume or settings with the other.
- ⚡ **Real-Time Processing**: Fast and smooth hand tracking using efficient computer vision techniques.
- 🌐 **Cross-Platform**: Works on Windows, macOS, and Linux.

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
- **Python** 🐍 — Easy-to-read language ideal for quick prototyping and computer vision tasks.
- **MediaPipe** 🎯 — Real-time hand tracking by Google; extremely fast and optimized even for low-end systems.
- **OpenCV** 🖼️ — Leading library for image and video processing; used to access webcam frames and handle image transformations.
- **PyAutoGUI** 🎮 — Allows the Python script to control the mouse and keyboard seamlessly.
- **pynput** ⌨️ — An alternative input control library for extended keyboard/mouse actions.
- **NumPy** 📊 — For efficient numerical operations and matrix transformations.

These libraries together enable real-time, accurate, and resource-light performance.

## 📁 Project Structure
vision-cursor/
- ├── main.py
- ├── hand_tracker.py
- ├── gesture_recognizer.py
- ├── mouse_controller.py
- ├── utils.py
- ├── requirements.txt
- └── README.md

### 🗂️ Description of Each File
- `main.py`: The entry point of the application. Initializes the camera feed, loads the hand tracking and gesture recognition modules, and coordinates cursor movement.
- `hand_tracker.py`: Handles all functionality related to detecting and tracking hands and fingers using MediaPipe.
- `gesture_recognizer.py`: Contains logic to interpret different hand gestures (e.g., pinch for click, swipe for navigation).
- `mouse_controller.py`: Maps recognized gestures to real mouse events using PyAutoGUI or pynput.
- `utils.py`: A utility file with helper functions (e.g., calculating distances between fingers, smoothing cursor motion).
- `requirements.txt`: Lists all required Python libraries for easy environment setup.
- `README.md`: You’re reading it right now! 📚

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
This project is licensed under the MIT License — see the LICENSE file for details.

## 👨‍💻 Author
- Name: Yazan M. Homssi
- GitHub: Shinoruba
- Professional Email: homssi002@gmail.com
- University Email: yazan_homssi@dlsu.edu.ph
- LinkedIn: https://www.linkedin.com/in/yazan-homssi/
