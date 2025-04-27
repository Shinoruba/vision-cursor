# VisionCursor: Real-Time Hand Gesture Mouse Control

VisionCursor is a Python-based application that transforms your webcam into a virtual mouse controller. By leveraging computer vision, it tracks your index finger to move the cursor and recognizes hand gestures for actions like clicking, navigating pages, and adjusting volume.

## Features

- **Cursor Control**: Move the mouse cursor using your index finger.
- **Gesture Recognition**: Perform actions like click, double-click, and page navigation through specific hand gestures.
- **Dual-Hand Functionality**: Use the other hand for additional controls, such as volume adjustment.
- **Real-Time Processing**: Achieves low-latency performance using MediaPipe and OpenCV.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shinoruba/vision-cursor.git
    cd vision-cursor
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main application:

```bash
python main.py
```

Ensure your webcam is connected. The application will start tracking your hand movements and respond to recognized gestures.

---

## Project Structure
vision-cursor/
- ├── main.py
- ├── hand_tracker.py
- ├── gesture_recognizer.py
- ├── mouse_controller.py
- ├── utils.py
- ├── requirements.txt
- └── README.md
#### ㅤ
- `main.py`: Initializes and runs the application.
- `hand_tracker.py`: Handles hand and finger tracking using MediaPipe.
- `gesture_recognizer.py`: Interprets hand gestures.
- `mouse_controller.py`: Maps gestures to mouse actions.
- `utils.py`: Contains utility functions.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
