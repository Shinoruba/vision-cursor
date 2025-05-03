"""
hand_tracker.py

Early Version (1.2):
- Handles hand detection and landmark drawing using MediaPipe. (1.1)
- Draws bounding box around detected hand. (1.2)
- Displays gesture label near the hand (e.g., "left_click"). (1.2)

Last Updated: May 3, 2025
"""

import cv2 as cv  # OpenCV, for image processing
import mediapipe as mp  # MediaPipe, for hand tracking

class HandTracker:
    """
    A class to perform hand detection and landmark extraction using MediaPipe Hands solution.
    """
    
    def __init__(self, max_num_hands=2, detection_confidence=0.7, tracking_confidence=0.7):
        """
        Initializes the MediaPipe Hands model with the desired parameters.
        
        Args:
            max_num_hands (int): Maximum number of hands to detect.
            detection_confidence (float): Minimum detection confidence threshold.
            tracking_confidence (float): Minimum tracking confidence threshold.
        """
        
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        
        self.mp_draw = mp.solutions.drawing_utils   # Initialize MediaPipe drawing utility for visualization
        
    # =======================================
    
    def find_hands(self, image, draw=True, gesture_label=None):
        """
        Processes an image to detect hands and optionally draws the landmarks.
        
        Args:
            image (numpy.ndarray): The BGR image frame captured from webcam.
            draw (bool): If True, draws hand landmarks on the image.
        
        Returns:
            image (numpy.ndarray): The image with or without hand landmarks drawn.
            results (mediapipe.python.solutions.hands.Hands): The detection results containing hand landmarks.
        """
        
        img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert the BGR image to RGB because MediaPipe expects RGB format
        
        results = self.hands.process(img_rgb)   # Perform hand detection

        # If hands are detected and draw option is True, draw landmarks
        if results.multi_hand_landmarks and results.multi_handedness:
                    for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                        handedness = results.multi_handedness[idx].classification[0].label

                        if draw:
                            # Draw landmarks
                            self.mp_draw.draw_landmarks(
                                image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                            )

                            # Get bounding box for the hand
                            h, w, _ = image.shape
                            x_list = [int(lm.x * w) for lm in hand_landmarks.landmark]
                            y_list = [int(lm.y * h) for lm in hand_landmarks.landmark]

                            x_min, x_max = min(x_list), max(x_list)
                            y_min, y_max = min(y_list), max(y_list)

                            # Draw rectangle
                            cv.rectangle(image, (x_min - 20, y_min - 20), (x_max + 20, y_max + 20), (0, 255, 0), 2)

                            # Show gesture only for left hand (MediaPipe label: "Right")
                            if handedness == "Right" and gesture_label:
                                cv.putText(
                                    image,
                                    gesture_label,
                                    (x_min - 20, y_min - 30),
                                    cv.FONT_HERSHEY_SIMPLEX,
                                    0.8,
                                    (0, 255, 255),
                                    2
                                )

        return image, results