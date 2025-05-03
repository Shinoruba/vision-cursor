"""
utils.py

Utility functions used across VisionCursor modules.

Initial Version (1.0):
- Contains reusable helpers for distance calculation and hand landmark analysis:
    - euclidean_distance
    - fingers_stretched
    - fingers_beside_each_other

Last Updated: May 3, 2025
"""

import math

def euclidean_distance(p1, p2):
    """
    Computes the Euclidean distance between two MediaPipe landmarks.

    Args:
        p1, p2: mediapipe.framework.formats.landmark_pb2.NormalizedLandmark
            The two landmarks whose distance is to be calculated.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def fingers_stretched(lm, finger_tips):
    """
    Determines if specific fingers are stretched (extended upward).

    Args:
        lm (list): List of hand landmarks.
        finger_tips (list): List of finger tip indices to evaluate.

    Returns:
        bool: True if all specified fingers are stretched, False otherwise.
    """
    for tip_idx, pip_idx in [(8, 6), (12, 10), (16, 14), (20, 18)]:  # tip and pip indices for each finger
        if tip_idx in finger_tips:
            if lm[tip_idx].y > lm[pip_idx].y:  # if finger is not stretched (tip is higher than pip)
                return False
    return True


def fingers_beside_each_other(lm, finger_tips, threshold=0.05):
    """
    Checks if the specified fingers are beside each other (x-coordinates are close).

    Args:
        lm (list): List of hand landmarks.
        finger_tips (list): List of finger tip indices to check.
        threshold (float): Max difference in x-coordinate for fingers to be considered "beside each other".

    Returns:
        bool: True if all specified fingers are beside each other, False otherwise.
    """
    tips = [lm[i] for i in finger_tips]
    for i in range(len(tips) - 1):
        if abs(tips[i].x - tips[i + 1].x) > threshold:
            return False
    return True