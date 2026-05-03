# birthday_pyttsx3.py
import pyttsx3

# 엔진 초기화
engine = pyttsx3.init()

# 목소리 설정 (맥에서는 기본 시스템 TTS 사용)
engine.setProperty('rate', 150)   # 말하는 속도
engine.setProperty('volume', 1.0) # 볼륨 (0.0~1.0)

# 말할 문구
text = "생일 축하합니다"

# 말하기
engine.say(text)
engine.runAndWait()