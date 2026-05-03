"""
yolo_person_alarm.py

- 웹캠/비디오에서 YOLO로 사람(person)을 감지하면 경고음 재생
- ultralytics (YOLOv8), opencv-python, pygame 사용
- alarm.wav 파일을 같은 폴더에 넣어 사용하세요 (또는 경로를 변경)
"""

import time
import cv2
from ultralytics import YOLO
import pygame

# --------- 설정 ----------
VIDEO_SOURCE = 0            # 0 = 기본 웹캠, 또는 "video.mp4", "rtsp://..." 등
ALARM_SOUND_PATH = "alarm.wav"  # 같은 폴더에 alarm.wav 준비
COOLDOWN_SECONDS = 3        # 사람 감지 후 재생 간격(초). 너무 작으면 소리가 계속 난다.
CONFIDENCE_THRESHOLD = 0.7  # detection confidence threshold
# --------------------------

def init_sound(path):
    pygame.mixer.init()
    try:
        sound = pygame.mixer.Sound(path)
    except Exception as e:
        print("경고음 불러오기 실패:", e)
        sound = None
    return sound

def play_alarm(sound):
    if sound:
        try:
            sound.play()
        except Exception as e:
            print("경고음 재생 실패:", e)

def main():
    # 모델 로드 (yolov8n: 가볍고 빠름. 필요하면 yolov8m/YOLOv8 모델로 변경)
    print("YOLO 모델 로드중...")
    model = YOLO("yolov8n.pt")  # 로컬에 .pt가 없으면 ultralytics가 자동 다운로드 시도할 수 있음

    # 사물 이름 (클래스 이름) 확인
    names = model.model.names if hasattr(model, "model") else None
    if names is None:
        # fallback
        names = {0: "person"}

    # 사운드 초기화
    sound = init_sound(ALARM_SOUND_PATH)
    if sound:
        print("알람 사운드 로드 완료:", ALARM_SOUND_PATH)
    else:
        print("알람 사운드가 없습니다. 소리 재생은 동작하지 않습니다.")

    # 비디오 캡처
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        print("비디오 소스 열기 실패:", VIDEO_SOURCE)
        return

    last_alarm_time = 0.0

    print("처리 시작. 종료하려면 'q' 누르세요.")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("프레임을 가져올 수 없습니다. 종료합니다.")
                break

            # 모델에 프레임 전달 (stream=True로 반복 처리)
            # ultralytics의 모델은 BGR 이미지를 직접 받을 수 있음
            results = model(frame, stream=False)  # stream=False: 한 프레임 결과
            # results는 리스트(또는 Results 객체)
            person_detected = False

            # results[0]에 대해 boxes 확인
            res = results[0]
            boxes = getattr(res, "boxes", None)
            if boxes is not None and len(boxes):
                # boxes.cls: 클래스 id tensor, boxes.conf: confidence
                cls_ids = boxes.cls.cpu().numpy()    # numpy array
                confs = boxes.conf.cpu().numpy()
                xyxy = boxes.xyxy.cpu().numpy()     # [x1,y1,x2,y2]
                for i, cls in enumerate(cls_ids):
                    conf = confs[i]
                    if conf < CONFIDENCE_THRESHOLD:
                        continue
                    # 클래스 id 0은 COCO의 'person' (대부분의 학습된 모델에서)
                    class_name = names.get(int(cls), str(int(cls)))
                    if class_name.lower() == "person" or int(cls) == 0:
                        person_detected = True
                        x1, y1, x2, y2 = map(int, xyxy[i])
                        # 박스와 라벨 그리기
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                        label = f"{class_name} {conf:.2f}"
                        cv2.putText(frame, label, (x1, y1-8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            # 사람 감지되면 알람 (쿨다운 적용)
            now = time.time()
            if person_detected and (now - last_alarm_time) >= COOLDOWN_SECONDS:
                print("사람 감지! 알람 재생")
                play_alarm(sound)
                last_alarm_time = now

            # 화면 표시
            cv2.imshow("YOLO Person Alarm", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("사용자 요청: 종료")
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        pygame.mixer.quit()

if __name__ == "__main__":
    main()