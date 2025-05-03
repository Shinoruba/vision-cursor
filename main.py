"""
main.py

Early Version (1.5):
- Open webcam   (1.0)
- Display the live video feed   (1.0)
- Detect hands and draw landmarks using HandTracker (1.1)
- Track index fingertip to move system mouse cursor (1.2)
- Recognize pinch/spread gestures using left hand to control system volume (1.3)
- Recognize right-hand gestures (click, scroll) using GestureRecognizer (1.4)
- Show some small visual markers on screen  (1.3)
- Shows gesture label next to left hand bounding box (1.5)
- Quit when user presses 'q'    (1.1)

Last Updated: May 3, 2025
"""

import cv2 as cv  # OpenCV is used to access and manipulate the webcam feed
from hand_tracker import HandTracker  # Import HandTracker class
from cursor_controller import move_cursor_from_landmarks  # Mouse control based on finger position
from gesture_controller import control_volume_from_gestures  # Recognize left-hand gestures for volume control
from gesture_recognizer import GestureRecognizer  # Recognize left-hand gestures for clicking and scrolling
from mouse_controller import perform_mouse_action

def main():
    """
    The Main File ( haha get it? main.py? ok .. ) will initialize webcam feed and display it in a new window.
    It will also run both cursor tracking and gesture control logic.
    """
    
    cap = cv.VideoCapture(0)   # Initialize the webcam, the device is usually denoted as '0'.
    
    # Check if webcam has turned on successfully
    if not cap.isOpened():
        print("[ERROR] Could not turn on the webcam.")
        return
    
    print("[SUCCESS] Webcam has successfully turned on! Press 'q' to exit.")
    
    # Initializing our HandTracker
    tracker = HandTracker()
    recognizer = GestureRecognizer()  # NEW: Right-hand gesture recognizer
    
    # ==========================
    # Main loop that will continuously capture frames from webcam.
    while True:
        ret, frame = cap.read() # Read a frame from the webcam
        
        # If the frame ain't read correctly, break off
        if not ret:
            print("[ERROR] Could not grab the frame.")
            break
        
        frame, results = tracker.find_hands(frame)
        
        gesture = recognizer.recognize(results)  # Recognize gesture from current frame, will still pass `results` to gesture_controller after this
        
        # Redraw hands with optional label (only shows on left hand internally)
        frame, _ = tracker.find_hands(frame, gesture_label=gesture)
        
        fingertip_pos = move_cursor_from_landmarks(results, frame.shape[:2])    # Move the mouse based on index fingertip and get its pixel position

        # If we got a fingertip position, draw a small visual marker on screen
        if fingertip_pos:
            x_px, y_px = fingertip_pos
            cv.circle(frame, (x_px, y_px), 10, (0, 255, 0), cv.FILLED)  # Draw a green filled circle
            
        # This will handle the left hand = gesture detection for volume control
        gesture_line = control_volume_from_gestures(results, frame.shape[:2])
        if gesture_line:
            x1, y1, x2, y2 = gesture_line
            cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 4)  # This will draw red line between thumb & index
            
        # NEW: Detect right-hand gesture and print it
        gesture = recognizer.recognize(results)
        if gesture:
            print(f"[GESTURE] Left-hand gesture detected: {gesture}")
            perform_mouse_action(gesture)
        
        cv.imshow('Vision Cursor', frame)   # Display the captured frame in a window.
        
        # Wait for 1ms, then check if 'q' key was pressed to exit the window.
        if cv.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] The key 'q' was pressed. Exiting ...")
            break
            
    # ==========================
    # Release webcam and destroy all OpenCV windows.
    cap.release()
    cv.destroyAllWindows()
    print("[INFO] Both webcam and window has been closed. Ending program ...")
    
if __name__ == "__main__":
    main()