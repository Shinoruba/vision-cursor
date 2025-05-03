"""
gesture_recognizer.py

This module is responsible for recognizing left-hand gestures for common mouse actions such as:
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

Last Updated: May 3, 2025
"""

from utils import euclidean_distance, fingers_stretched, fingers_beside_each_other

class GestureRecognizer:
    """
    GestureRecognizer
    -----------------
    Classifies gestures made by the left hand using landmarks detected by MediaPipe Hands.
    """

    def __init__(self):
        """
        I may or may not expand this class with more gesture types later.
        It entirely depends if I have the time haha lmao xd.
        Goodluck in CSOPESY Yazan! Thanks Yazan! You are Welcome Yazan!
        """
        pass

    def recognize(self, results):
        """
        Recognizes gestures from the left hand landmarks.

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

        return None  # No gesture recognized from left hand