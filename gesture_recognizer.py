"""
gesture_recognizer.py

This module is responsible for recognizing right-hand gestures for common mouse actions such as:
- Left click
- Double click
- Right click
- Scroll up/down
- Page navigation (forward/backward)

Initial Version (1.0):
- Custom gesture rules based on user-specified finger configurations:
    - Left Click: index and middle fingers extended and close together
    - Double Click: index, middle, and ring fingers extended and close together
    - Right Click: index and pinky extended, others folded
    - Scroll Up: hand open like a "stop" sign (all fingers extended)
    - Scroll Down: closed fist (all fingers folded)

Last Updated: May 2, 2025
"""

import math

# =======================================
# Utility functions
def euclidean_distance(p1, p2):
    """Helper function to compute distance between two 3D MediaPipe landmarks."""
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def fingers_stretched(lm, finger_tips):
    """Check if specified fingers are stretched out (tip y-coordinate lower than pip joint)"""
    for tip_idx, pip_idx in [(8, 6), (12, 10), (16, 14), (20, 18)]:  # tip and pip indices for each finger
        if tip_idx in finger_tips:
            if lm[tip_idx].y > lm[pip_idx].y:  # if finger is not stretched (tip is higher than pip)
                return False
    return True

def fingers_beside_each_other(lm, finger_tips, threshold=0.05):
    """Check if specified fingers are beside each other (x-coordinates are close)"""
    tips = [lm[i] for i in finger_tips]
    for i in range(len(tips)-1):
        if abs(tips[i].x - tips[i+1].x) > threshold:
            return False
    return True

# =======================================
# Main Class
class GestureRecognizer:
    """
    GestureRecognizer
    -----------------
    Classifies gestures made by the RIGHT hand using landmarks detected by MediaPipe Hands.
    """

    def __init__(self):
        # We may expand this class with more gesture types later
        pass

    def recognize(self, results):
        """
        Recognizes gestures from the RIGHT hand landmarks.

        Parameters:
            results: mediapipe.python.solution_base.SolutionOutputs
                The output from MediaPipe Hands, contains multi_hand_landmarks and handedness info.

        Returns:
            str or None: The recognized gesture name (e.g., 'left_click', 'right_click') or None if no gesture matched.
        """
        if not results.multi_hand_landmarks or not results.multi_handedness:
            return None

        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            handedness = results.multi_handedness[i].classification[0].label

            if handedness != "Right":
                continue  # We only classify gestures for the Left hand

            lm = hand_landmarks.landmark    # For readability

# =======================================
            # Gesture Classifications

            # 1. Left Click: index and middle finger beside each other stretched out
            if (fingers_stretched(lm, [8, 12]) and  # index and middle stretched
                fingers_beside_each_other(lm, [8, 12]) and  # beside each other
                not fingers_stretched(lm, [16, 20])):  # ring and pinky not stretched
                return "left_click"

            # 2. Double Left Click: index, middle, and ring finger beside each other stretched out
            if (fingers_stretched(lm, [8, 12, 16]) and  # index, middle, ring stretched
                fingers_beside_each_other(lm, [8, 12, 16]) and  # beside each other
                not fingers_stretched(lm, [20])):  # pinky not stretched
                return "double_click"

            # 3. Right Click: index and pinky finger stretched out
            if (fingers_stretched(lm, [8, 20]) and  # index and pinky stretched
                not fingers_stretched(lm, [12, 16])):  # middle and ring not stretched
                return "right_click"

            # 4. Scroll Up: stop sign (all fingers stretched except thumb)
            if (fingers_stretched(lm, [8, 12, 16, 20]) and  # all fingers stretched
                lm[4].y > lm[3].y):  # thumb not stretched (tip higher than pip)
                return "scroll_up"

            # 5. Scroll Down: fist (no fingers stretched)
            if all(not fingers_stretched(lm, [i]) for i in [8, 12, 16, 20]):  # no fingers stretched
                return "scroll_down"

        return None  # No gesture recognized from right hand