"""
mouse_controller.py

Executes actual system-level mouse actions in response to recognized gestures.

Initial Version (1.0):
- Maps gesture strings from GestureRecognizer to PyAutoGUI/pynput mouse actions
- Handles: left click, double click, right click, scroll up/down

Last Updated: May 3, 2025
"""

import pyautogui
import time

# Optional: prevent PyAutoGUI failsafe from interrupting
pyautogui.FAILSAFE = False

# Timing for debounce and delay
LAST_GESTURE_TIME = 0
GESTURE_COOLDOWN = 0.8  # seconds

def perform_mouse_action(gesture_name):
    """
    Maps a recognized gesture to a real mouse action.

    Args:
        gesture_name (str): The gesture name, e.g. 'left_click', 'scroll_up'.
    """
    global LAST_GESTURE_TIME
    current_time = time.time()

    if current_time - LAST_GESTURE_TIME < GESTURE_COOLDOWN:
        return  # Prevent accidental gesture spamming

    if gesture_name == "left_click":
        pyautogui.click()
        print("[ACTION] Left click performed.")

    elif gesture_name == "double_click":
        pyautogui.doubleClick()
        print("[ACTION] Double click performed.")

    elif gesture_name == "right_click":
        pyautogui.rightClick()
        print("[ACTION] Right click performed.")

    elif gesture_name == "scroll_up":
        pyautogui.scroll(300)  # Scroll up
        print("[ACTION] Scroll up performed.")

    elif gesture_name == "scroll_down":
        pyautogui.scroll(-300)  # Scroll down
        print("[ACTION] Scroll down performed.")

    # Update last gesture time
    LAST_GESTURE_TIME = current_time