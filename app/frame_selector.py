import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_detection
mp_mesh = mp.solutions.face_mesh

face_detection = mp_face.FaceDetection(min_detection_confidence=0.6)
face_mesh = mp_mesh.FaceMesh(static_image_mode=True)

def blur_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def is_face_centered(bbox, img_shape):
    ih, iw, _ = img_shape
    x, y, w, h = bbox
    cx, cy = x + w/2, y + h/2
    return iw*0.3 < cx < iw*0.7 and ih*0.3 < cy < ih*0.7
    
def eyes_open(landmarks, h):
    # Left eye
    left_eye = abs((landmarks[159].y - landmarks[145].y) * h)
    # Right eye
    right_eye = abs((landmarks[386].y - landmarks[374].y) * h)

    eye_open_threshold = h * 0.01
    return left_eye > eye_open_threshold and right_eye > eye_open_threshold

def mouth_closed(landmarks, h):
    upper_idxs = [13, 312]
    lower_idxs = [14, 317]

    upper_y = sum(landmarks[i].y for i in upper_idxs) / len(upper_idxs)
    lower_y = sum(landmarks[i].y for i in lower_idxs) / len(lower_idxs)

    nose = landmarks[1]
    chin = landmarks[152]

    mouth_gap = abs((lower_y - upper_y) * h)
    face_height = abs((chin.y - nose.y) * h)

    return (mouth_gap / face_height) < 0.06

def select_best_frame(frames):

    best_score = -1
    best_frame = None

    for frame in frames:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 1️⃣ Face detection
        result = face_detection.process(rgb)
        if not result.detections:
            continue

        detection = result.detections[0]
        bbox = detection.location_data.relative_bounding_box
        h, w, _ = frame.shape

        box = (
            int(bbox.xmin * w),
            int(bbox.ymin * h),
            int(bbox.width * w),
            int(bbox.height * h)
        )

        score = 0

        # 2️⃣ Blur (sharpness)
        score += min(blur_score(frame), 300)

        # 3️⃣ Face centered
        if is_face_centered(box, frame.shape):
            score += 100

        # 4️⃣ Face mesh analysis
        mesh = face_mesh.process(rgb)
        if not mesh.multi_face_landmarks:
            continue

        landmarks = mesh.multi_face_landmarks[0].landmark

        # 5️⃣ Mouth closed
        if mouth_closed(landmarks, h):
            score += 200
        else:
            continue   # ❌ reject talking frames

        # 6️⃣ Eyes open
        if eyes_open(landmarks, h):
            score += 200
        else:
            continue   # ❌ reject blink frames

        # 7️⃣ Best frame update
        if score > best_score:
            best_score = score
            best_frame = frame

    return best_frame