"""
cursor_controller.py

Early Version (1.2):
- This module handles cursor movement using the tracked position of the right hand's index fingertip.    (1.2)
- It extracts landmark coordinates from MediaPipe results and maps them to the screen size
  to control the system mouse cursor using pyautogui.   (1.1)
  
Last Updated: May 3, 2025
"""

import pyautogui  # For controlling the system's mouse cursor
import cv2 as cv  # Will I need this for frame size(?)
import numpy as np  # For scaling and coordinate mapping

screen_width, screen_height = pyautogui.size()  # Get screen size to use as target mapping space

def move_cursor_from_landmarks(results, frame_shape):
    """
    Detects the index fingertip of the user's right hand (interpreted as "Left" by MediaPipe) 
    and moves the system cursor accordingly.

    Args:
        results: MediaPipe hand detection results (contains landmarks and handedness).
        frame_shape: Tuple (height, width) of the webcam frame.

    Returns:
        (x_px, y_px): Pixel coordinates of the fingertip for visualization, or None if right hand not found.
    """
    frame_height, frame_width = frame_shape

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_info in enumerate(results.multi_handedness):
            hand_label = hand_info.classification[0].label  # "Left" or "Right"

            # Reverse logic: "Left" label means user's right hand (due to camera mirror view)
            if hand_label == "Left":
                hand_landmarks = results.multi_hand_landmarks[idx]

                index_tip = hand_landmarks.landmark[8]  # Personal Note: Index finger tip is landmark #8

                # Convert normalized landmark to pixel coordinates
                x_px = int(index_tip.x * frame_width)
                y_px = int(index_tip.y * frame_height)

                flipped_x = frame_width - x_px  # Flip x-axis for screen coordinate mapping only

                # Map to screen space
                screen_x = np.interp(flipped_x, [0, frame_width], [0, screen_width])
                screen_y = np.interp(y_px, [0, frame_height], [0, screen_height])

                pyautogui.moveTo(screen_x, screen_y)

                return (x_px, y_px)  # Use original X for drawing the green circle around my pointy index pointy finger

    return None  # No matching hand detected