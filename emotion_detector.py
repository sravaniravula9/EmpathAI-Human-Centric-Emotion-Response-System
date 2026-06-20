import cv2
import time
from deepface import DeepFace

def detect_emotion():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Camera Not Found"

    emotion = "No Face Detected"
    start = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )

            emotion = result[0]['dominant_emotion']

            cv2.putText(
                frame,
                f"Emotion: {emotion}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        except:
            cv2.putText(
                frame,
                "No Face Detected",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

        cv2.imshow("EmpathAI Camera", frame)

        if time.time() - start > 5:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return emotion.capitalize()