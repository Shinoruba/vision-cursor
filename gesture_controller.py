"""
gesture_controller.py

This module recognizes specific gestures made by the user's left hand (interpreted as "Right" by MediaPipe)
and maps them to system-level actions, such as adjusting volume.

Initial gesture (1.1): 
- Distance-based gesture between thumb tip and index tip to simulate volume up/down using keyboard shortcuts.   (1.1)

Future expansion can include mute toggle, page navigation, etc. ( If I can handle it + If I have the time lmao )

Last Updated: April 30, 2025
"""

import math
import pyautogui

def control_volume_from_gestures(results, frame_shape):
    """
    Detects pinch/spread gestures of the left hand (MediaPipe label: "Right") and 
    adjusts volume accordingly by simulating keyboard key presses.

    Args:
        results: MediaPipe results object (landmarks and handedness).
        frame_shape: Tuple of (height, width) of the frame.

    Returns:
        Tuple (x1, y1, x2, y2) of index and thumb tip pixel coords if gesture is detected, else None.
    """
    frame_height, frame_width = frame_shape

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_info in enumerate(results.multi_handedness):
            hand_label = hand_info.classification[0].label  # "Left" or "Right"

            # "Right" label → user's left hand in front of camera
            if hand_label == "Right":
                hand_landmarks = results.multi_hand_landmarks[idx]

                # Index finger tip is landmark 8, thumb tip is landmark 4
                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]

                x1, y1 = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
                x2, y2 = int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)

                distance = math.hypot(x2 - x1, y2 - y1) # Calculate Euclidean distance between tips

                # Thresholds, I may need to tune this based on my camera distance ngl
                if distance < 40:
                    pyautogui.press("volumedown")
                elif distance > 100:
                    pyautogui.press("volumeup")

                return (x1, y1, x2, y2)

    return None  # No gesture detected