import cv2, datetime, os, threading
from picamera2 import Picamera2
from ultralytics import YOLO
from tkinter import Tk, Label, StringVar, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import time

import firebase_admin
from firebase_admin import credentials, db, storage

# Firebase 초기화
cred = credentials.Certificate("data-632b1-firebase-adminsdk-nc8tb-3cc3d0955c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-632b1.firebaseio.com/',
    'storageBucket': 'data-632b1.appspot.com'
})
bucket = storage.bucket()

# YOLO 모델 로드
model = YOLO("CSIF_detect_ncnn_model")

# 카메라 설정
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 640)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Tkinter UI 세팅
win = Tk()
win.title("CSIF Detection")
video_label = Label(win)
video_label.pack()

today = datetime.datetime.now().strftime("%Y-%m-%d")
ref = db.reference(f"manager/{today}")

name_var, job_var , level_var= StringVar(), StringVar(), StringVar()
current = "출근 전 입니다."
ttk.Label(win, text="이름:").pack()
combo = ttk.Combobox(win, textvariable=name_var)
combo.pack()

try:
    data = ref.get()
    name_options = list(data.keys()) if data else []
    combo['values'] = name_options
    if name_options:
        combo.current(0)
except Exception as e:
    print("Firebase 이름 목록 로딩 실패:", e)
    name_options = []
        
ttk.Label(win, text="직책:").pack()
level_list=['건설 근로자','건설 현장 관리','중장비 기사','기타']
combo1 = ttk.Combobox(win, textvariable=level_var,values=level_list)
combo1.current(0)
combo1.pack()

ttk.Label(win, text="업무:").pack()
job_list=['형틀 제작 작업','철근배치(배근)작업','시스템 동바리 작업','비계 설치 작업','학석 작업','바닥 및 벽면 견출 작업','기타 잔업 및 업무']
combo2 = ttk.Combobox(win, textvariable=job_var,values=job_list)
combo2.current(0)
combo2.pack()

def send():
    name = name_var.get().strip()
    job = job_var.get().strip()
    if not name or not job:
        messagebox.showwarning("입력 오류", "이름과 업무를 모두 입력하세요.")
        return

    global latest_annotated
    if latest_annotated is None:
        messagebox.showwarning("오류", "프레임이 준비되지 않았습니다.")
        return
    combo_str=combo.get() #선택된 콤보박스의 이름 가져오기
    combo1_str=combo1.get()
    combo2_str=combo2.get()
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{combo_str}CSIF.jpg"
    local_path = f"/tmp/{filename}"

    cv2.imwrite(local_path, latest_annotated)
    blob = bucket.blob(filename)
    blob.upload_from_filename(local_path)
    os.remove(local_path)

    ref2 = db.reference(f"workers/{timestamp.split()[0]}") #리얼타임에 출근자 명단 worker 버킷에 올리기.

    ref2.update({
        f"{combo_str}":str([combo1_str,combo2_str])
    })

    messagebox.showinfo("전송 완료", "전송되었습니다.") 

def inference_loop():
    global latest_frame, latest_annotated, detected_all

    while True:
        frame = picam2.capture_array()
        results = model(frame)
        boxes = results[0].boxes
        detected = {"Vest": False, "HardHat": False, "Goggles": False}

        for box in boxes:
            label = model.names[int(box.cls[0])]
            if label in detected and float(box.conf[0]) >= 0.5:
                detected[label] = True

        detected_all = all(detected.values())
        if detected_all:
            status = "All CSIF Detected"
            color = (0, 255, 0)
            annotated = results[0].plot()
            cv2.putText(annotated, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
            latest_frame = frame
            latest_annotated = annotated
            send() #이미지 파일 전송 함수 호출.
            global current
            current="장비 착용 검사 완료. 출근등록되었습니다."
            result_lb['text']=current
            return
        else:
            status = "Incomplete CSIF"
            color = (0, 0, 255)
        '''status = "All CSIF Detected" if detected_all else "Incomplete CSIF"
        color = (0, 255, 0) if detected_all else (0, 0, 255)'''
        annotated = results[0].plot()
        cv2.putText(annotated, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        latest_frame = frame
        latest_annotated = annotated

        time.sleep(0.1)  # 10fps 정도

def update_ui():
    
    if latest_annotated is not None:
        img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(latest_annotated, cv2.COLOR_BGR2RGB)))
        video_label.imgtk = img
        video_label.config(image=img)

    win.after(100, update_ui)

def start():
    # 추론 쓰레드 시작
    global current
    current="장비 착용 검사 중입니다."
    result_lb['text']=current
    threading.Thread(target=inference_loop, daemon=True).start()

start_btn = ttk.Button(win,text="출근체크 시작")
start_btn.pack()
start_btn.config(command=start)

result_lb = ttk.Label(win, text=current,font=("NanumGothic", 25))
result_lb.pack()

latest_frame = None
latest_annotated = None
detected_all = False

# UI 갱신 시작
update_ui()

win.mainloop()