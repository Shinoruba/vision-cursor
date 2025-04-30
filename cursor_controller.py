"""
cursor_controller.py

Early Version (1.1):
- This module handles cursor movement using the tracked position of the index fingertip.    (1.1)
- It extracts landmark coordinates from MediaPipe results and maps them to the screen size
  to control the system mouse cursor using pyautogui.   (1.1)
  
Last Updated: April 28, 2025
"""

import pyautogui  # For controlling the system's mouse cursor
import cv2 as cv  # Needed for frame size
import numpy as np  # For scaling and coordinate mapping

screen_width, screen_height = pyautogui.size()  # Get screen size to use as target mapping space


def move_cursor_from_landmarks(results, frame_shape, hand_index=0):
    """
    Detects index fingertip landmark from MediaPipe results and moves the system cursor.

    Args:
        results: MediaPipe hand detection results.
        frame_shape: Tuple (height, width) of the captured webcam frame.
        hand_index (int): Which hand to use if multiple hands are detected. Default is 0 (first hand).
    """

    frame_height, frame_width = frame_shape # Extract dimensions of the webcam frame

    if results.multi_hand_landmarks:
        # Only proceed if the expected hand index exists
        if hand_index < len(results.multi_hand_landmarks):
            hand_landmarks = results.multi_hand_landmarks[hand_index]   # Get the selected hand's landmarks
            index_tip = hand_landmarks.landmark[8]  # Landmark index 8 corresponds to the tip of the index finger

            # Get normalized coordinates (range 0 to 1) and scale to frame size
            x_px = int(index_tip.x * frame_width)
            y_px = int(index_tip.y * frame_height)

            # Map webcam coordinates to screen coordinates
            screen_x = np.interp(x_px, [0, frame_width], [0, screen_width])
            screen_y = np.interp(y_px, [0, frame_height], [0, screen_height])

            
            pyautogui.moveTo(screen_x, screen_y)    # Move the mouse cursor

            # OPTIONAL: Draw a circle on the frame for feedback (This should be drawn in main.py ngl)
            return (x_px, y_px)  # Return pixel location on frame for feedback

    return None  # No hand detected or index out of range