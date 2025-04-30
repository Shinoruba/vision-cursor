"""
main.py

Early Version (1.2):
- Open webcam   (1.0)
- Display the live video feed   (1.0)
- Detect hands and draw landmarks using HandTracker (1.1)
- Track index fingertip to move system mouse cursor (1.2)
- Show a small circle at the fingertip location for user feedback   (1.2)
- Quit when user presses 'q'    (1.1)

Last Updated: April 30, 2025
"""

import cv2 as cv  # OpenCV is used to access and manipulate the webcam feed
from hand_tracker import HandTracker  # Import HandTracker class
from cursor_controller import move_cursor_from_landmarks  # Mouse control based on finger position

def main():
    """
    The Main File ( haha get it? main.py? ok .. ) will initialize webcam feed and display it in a new window.
    """
    
    cap = cv.VideoCapture(0)   # Initialize the webcam, the device is usually denoted as '0'.
    
    # Check if webcam has turned on successfully
    if not cap.isOpened():
        print("[ERROR] Could not turn on the webcam.")
        return
    
    print("[SUCCESS] Webcam has successfully turned on! Press 'q' to exit.")
    
    # Initializing our HandTracker
    tracker = HandTracker()
    
    # ==========================
    # Main loop that will continuously capture frames from webcam.
    while True:
        ret, frame = cap.read() # Read a frame from the webcam
        
        # If the frame ain't read correctly, break off
        if not ret:
            print("[ERROR] Could not grab the frame.")
            break
        
        frame, results = tracker.find_hands(frame)
        
        fingertip_pos = move_cursor_from_landmarks(results, frame.shape[:2])    # Move the mouse based on index fingertip and get its pixel position

        # If we got a fingertip position, draw a small visual marker on screen
        if fingertip_pos:
            x_px, y_px = fingertip_pos
            cv.circle(frame, (x_px, y_px), 10, (0, 255, 0), cv.FILLED)  # Draw a green filled circle
        
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