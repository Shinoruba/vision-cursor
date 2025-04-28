"""
hand_tracker.py

Early Version (1.1):
- Handles hand detection and landmark drawing using MediaPipe.  (1.1)
- It sets up a reusable HandTracker class that can process webcam frames,
  detect hands, and return useful hand landmark data for further actions.   (1.1)

Last Updated: April 28, 2025
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
    
    def find_hands(self, image, draw=True):
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
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
        
        # Return the image and detection results
        return image, results