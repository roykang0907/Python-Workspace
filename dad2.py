import turtle
import random
import time
import pyttsx3

engine = pyttsx3.init()

# 목소리 설정 (맥에서는 기본 시스템 TTS 사용)
engine.setProperty('rate', 150)   # 말하는 속도
engine.setProperty('volume', 1.0) # 볼륨 (0.0~1.0)

# 말할 문구
text = "생일 축하합니다"

# 말하기
engine.say(text)
engine.runAndWait()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MESSAGE = "생신 축하드립니다!"
FONT_NAME = "Malgun Gothic"
FONT_SIZE = 48
FONT_STYLE = "bold"
LETTER_DELAY = 0.35

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("생일 축하합니다")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 40)
pen.setheading(0)

total_chars = len(MESSAGE)
approx_char_width = FONT_SIZE * 0.6
start_x = - (total_chars * approx_char_width) / 2
x = start_x
y = 40

colors = ["#E63946", "#F77F00", "#F9C74F", "#90BE6D", "#43AA8B", "#577590", "#8338EC", "#FF6B6B"]

for ch in MESSAGE:
    pen.goto(x, y)
    pen.color(random.choice(colors))
    pen.write(ch, align="left", font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
    x += approx_char_width
    time.sleep(LETTER_DELAY)

def draw_balloon(x, y, radius, color):
    b = turtle.Turtle()
    b.hideturtle()
    b.speed(0)
    b.penup()
    b.goto(x, y - radius)
    b.pendown()
    b.color(color)
    b.begin_fill()
    b.circle(radius)
    b.end_fill()

    b.penup()
    b.goto(x, y - radius)
    b.pendown()
    b.width(2)
    b.goto(x, y - radius - 60)

def confetti(n):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for _ in range(n):
        cx = random.randint(-SCREEN_WIDTH//2 + 10, SCREEN_WIDTH//2 - 10)
        cy = random.randint(-SCREEN_HEIGHT//2 + 10, SCREEN_HEIGHT//2 - 10)
        t.penup()
        t.goto(cx, cy)
        t.pendown()
        t.dot(random.randint(6, 14), random.choice(colors))

draw_balloon(-220, 160, 40, "#FF6B6B")
draw_balloon(-160, 120, 30, "#90BE6D")
draw_balloon(220, 160, 45, "#577590")
draw_balloon(170, 120, 30, "#F9C74F")

confetti(80)

screen.mainloop()