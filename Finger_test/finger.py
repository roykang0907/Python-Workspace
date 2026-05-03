import cv2
import mediapipe as mp
import time
import requests
import threading
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ================== 텔레그램 설정 ==================
BOT_TOKEN = "8742370545:AAEfEfL82xQplOq-YdeJ8K_Ax5U7IbYnjuw"
CHAT_ID = "8705687831"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(
            url,
            data={"chat_id": CHAT_ID, "text": message},
            timeout=2
        )
        print("✅ 전송 완료:", message)
    except:
        print("⚠️ 전송 실패 (무시)")

def send_async(message):
    threading.Thread(target=send_telegram, args=(message,), daemon=True).start()

# ================== MediaPipe 설정 ==================
model_path = "hand_landmarker.task"

BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

latest_result = None

def result_callback(result, output_image, timestamp_ms):
    global latest_result
    latest_result = (result, output_image)

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    num_hands=1,
    result_callback=result_callback
)

# ================== 손가락 계산 ==================
def count_fingers(hand_landmarks, handedness):
    fingers = 0

    # 엄지
    if handedness == "Right":
        if hand_landmarks[4].x < hand_landmarks[3].x:
            fingers += 1
    else:
        if hand_landmarks[4].x > hand_landmarks[3].x:
            fingers += 1

    # 나머지
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for tip, pip in zip(tips, pips):
        if hand_landmarks[tip].y < hand_landmarks[pip].y:
            fingers += 1

    return fingers - 1

# ================== 카메라 ==================
cap = cv2.VideoCapture(0)

gesture_start_time = None
current_gesture = -1
sent_gesture = -1

HOLD_TIME = 1.0  # 1초 유지 조건

with HandLandmarker.create_from_options(options) as landmarker:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        timestamp = int(time.time() * 1000)
        landmarker.detect_async(mp_image, timestamp)

        if latest_result is not None:
            result, output_image = latest_result
            draw_frame = output_image.numpy_view()
            draw_frame = cv2.cvtColor(draw_frame, cv2.COLOR_RGB2BGR)

            finger_count = 0

            if result.hand_landmarks:
                hand_landmarks = result.hand_landmarks[0]
                handedness = result.handedness[0][0].category_name
                finger_count = count_fingers(hand_landmarks, handedness)

                h, w, _ = draw_frame.shape

                for lm in hand_landmarks:
                    x, y = int(lm.x * w), int(lm.y * h)
                    cv2.circle(draw_frame, (x, y), 5, (0,255,0), -1)

                for connection in HAND_CONNECTIONS:
                    start = hand_landmarks[connection[0]]
                    end = hand_landmarks[connection[1]]
                    x1, y1 = int(start.x * w), int(start.y * h)
                    x2, y2 = int(end.x * w), int(end.y * h)
                    cv2.line(draw_frame, (x1, y1), (x2, y2), (255,0,0), 2)

                cv2.putText(draw_frame, f"{handedness}: {finger_count}",
                            (10,40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0,255,255), 2)

            # ================== 제스처 유지 로직 ==================

            now = time.time()

            if finger_count in [1, 2]:

                if current_gesture != finger_count:
                    current_gesture = finger_count
                    gesture_start_time = now

                else:
                    if now - gesture_start_time >= HOLD_TIME:
                        if sent_gesture != finger_count:

                            if finger_count == 1:
                                send_async("아빠에게: 데이터 좀 보내주세요")
                                print("📨 1초 유지 → 데이터 요청 전송")

                            elif finger_count == 2:
                                send_async("아빠에게: 폰 좀 열어주세요")
                                print("📨 1초 유지 → 폰 열어달라 전송")

                            sent_gesture = finger_count

            else:
                # 손 내리면 초기화
                current_gesture = -1
                gesture_start_time = None
                sent_gesture = -1

            cv2.imshow("Hand Tracking", draw_frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()