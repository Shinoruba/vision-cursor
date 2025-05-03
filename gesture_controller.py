"""
gesture_controller.py

This module recognizes specific gestures made by the user's left hand (interpreted as "Right" by MediaPipe)
and maps them to system-level actions, such as adjusting volume.

Updated Logic (v1.2):
- Volume control only triggers when a "pinch gesture" is made (index and thumb close).
- Prevents unwanted volume adjustments from general hand movement.

Last Updated: May 3, 2025
"""

import math
import pyautogui

def control_volume_from_gestures(results, frame_shape):
    """
    Detects intentional pinch gesture between thumb and index of the left hand (MediaPipe "Right")
    and adjusts volume accordingly by simulating keyboard presses.

    Args:
        results: MediaPipe results object (landmarks and handedness).
        frame_shape: Tuple of (height, width) of the frame.

    Returns:
        Tuple (x1, y1, x2, y2): Pixel coordinates of the index and thumb tips if pinch is detected, else None.
    """
    frame_height, frame_width = frame_shape

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_info in enumerate(results.multi_handedness):
            hand_label = hand_info.classification[0].label  # "Left" or "Right"

            # "Right" in MediaPipe = user's LEFT hand
            if hand_label == "Right":
                hand_landmarks = results.multi_hand_landmarks[idx]

                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]

                x1, y1 = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
                x2, y2 = int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)

                distance = math.hypot(x2 - x1, y2 - y1)

                # Only control volume if fingers are in a pinch zone (intentionally close)
                if distance < 60:
                    if distance < 30:
                        pyautogui.press("volumedown")
                    else:  # 30 <= distance < 60
                        pyautogui.press("volumeup")
                    
                    return (x1, y1, x2, y2)  # Draw visual feedback

                # Fingers are far apart — treat as not pinching
                return None

    return None  # No relevant hand or gesture detected