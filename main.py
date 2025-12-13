import cv2
import mediapipe as mp

# MediaPipe - Modules Initialization:

mp_face_detection = mp.solutions.face_detection          # Namespace -> facial detection models, inference models.
mp_drawing = mp.solutions.drawing_utils                  # Utilitary functions to draw bounding box, points, lines, etc.

cap = cv2.VideoCapture(0)                                # Start capturing -> 0, 1, 2, etc.

# MediaPipe - Context Manager:

with mp_face_detection.FaceDetection(
    model_selection=0,                                   # 0 = near faces (single). 1 = middle/far distance (multiples)
    min_detection_confidence=0.6                         # 0-1 = recognition confidence
) as face_detection:
    
    #Main Loop:

    while cap.isOpened():
        ret, frame = cap.read()                          # If ret=true, go!
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Color conversion cv2=BGR. mp=RGB.
        results = face_detection.process(rgb_frame)         # Frame processment

        if results.detections:                              # REVIEW AND UNDERSTAND THIS: 
            for detection in results.detections:            # Detections is a List, and SUPER important to you to know all about it
                keypoint_drawing_spec = results             
                mp_drawing.draw_detection(frame, detection) # Draw bounding box and score in the frame

        cv2.imshow("Face Detection", frame)                 # Open a windows called "Face Detection" and draw the frame

        if cv2.waitKey(1) & 0xFF == 27:                     # WaitKey(1) refreshes 1ms and wait for detected 'esc' key pressed
            break

cap.release()                                               # Turn off webcam
cv2.destroyAllWindows()                                     # Close window and clean all
