import cv2
import mediapipe as mp


mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


cap = cv2.VideoCapture(0)                                # Start capturing -> 0, 1, 2, etc.


with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=2,
    refine_landmarks=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
) as face_mesh:

    
    #Main Loop:

    while cap.isOpened():
        ret, frame = cap.read()                          # If ret=true, go!
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
            )


        cv2.imshow("Face Mesh", frame)                 # Open a windows called "Face Mesh" and draw the frame

        if cv2.waitKey(1) & 0xFF == 27:                     # WaitKey(1) refreshes 1ms and wait for detected 'esc' key pressed
            break

cap.release()                                               # Turn off webcam
cv2.destroyAllWindows()                                     # Close window and clean all
