from ultralytics import YOLO

model = YOLO("best.pt")  # Load the YOLO model

model.export(format="ncnn")