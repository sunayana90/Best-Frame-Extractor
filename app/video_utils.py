import cv2

def extract_frames(video_path, base_gap=8):
    cap = cv2.VideoCapture(video_path)
    frames = []
    prev_frame = None
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        motion = 100  # default high motion

        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, frame)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            motion = gray.mean()

        # 📌 PAUSE DETECTED → CAPTURE MORE FRAMES
        if motion < 5:          # pause / stable
            frames.append(frame)
        elif frame_count % base_gap == 0:
            frames.append(frame)

        prev_frame = frame
        frame_count += 1

    cap.release()
    return frames
