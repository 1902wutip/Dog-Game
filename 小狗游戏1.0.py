import turtle
import random
import time

window = turtle.Screen()
window.title("弹跳小狗")
window.bgcolor("white")
window.setup(width=800, height=600)
canvas = turtle.Turtle()
canvas.speed(0)
canvas.shape("square")
canvas.color("black")
canvas.penup()
canvas.goto(-400, -300)
canvas.pendown()
canvas.fd(800)
canvas.lt(90)
canvas.fd(600)
canvas.lt(90)
canvas.fd(800)
canvas.lt(90)
canvas.fd(600)
canvas.lt(90)
canvas.hideturtle()

vx_dog = 3
vy_dog = 10
acceleration = 1
vx_obstacle = 3
attack = 0.001    ##  probability of
level = 1

dog = turtle.Turtle()
dog.speed(0)
dog.shape("turtle")
dog.color("brown")
dog.penup()
dog.goto(-380, -280)
dog.dx = 0
dog.dy = 0
#turtle.register_shape("dog.gif")  # 注册自定义图标文件
#dog.shape("dog.gif")  # 将小狗的图标形状更改为自定义图标

obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("red")
obstacle.penup()
obstacle.goto(380, -280)
vx_obs = vx_obstacle*level
obstacle.dx = -vx_obs

def move():
    x = dog.xcor() + dog.dx
    dog.setx((2*(x>=0)-1) * min(390,abs(x)))
    dog.sety(max(-280,dog.ycor() + dog.dy))

def jump():
    if dog.ycor() <= -280:
        dog.dy = vy_dog*(1+0.5*(level-1))

def fall():
    if dog.ycor() > -280:
        dog.dy -= acceleration*(1+1.2*(level-1))
    else:
        dog.dy = 0
        dog.sety(-280)
    if abs(dog.xcor()) >= 390:
        dog.dx = 0

def left():
    dog.dx -= vx_dog

def right():
    dog.dx += vx_dog

def move_obstacle():
    x = obstacle.xcor() + obstacle.dx
    obstacle.setx((2*(x>=0)-1) * min(390,abs(x)))
    if abs(x) >= 390:
        obstacle.dx = vx_obs*(2*(x<=0)-1)

def collision():
    if dog.distance(obstacle) < 20:
        return True
    else:
        return False

subtitle = turtle.Turtle()
subtitle.color("black")
subtitle.penup()
subtitle.hideturtle()
subtitle.write(f"Level {level}",align="center",font=("Courier",24,"normal"))

window.listen()
window.onkey(jump, "space")
window.onkey(left, "Left")
window.onkey(right, "Right")
t0 = time.time()
while True:
    window.update()
    time.sleep(0.02)
    move()
    fall()
    move_obstacle()
    if collision():
        break
    if time.time()-t0 >= 30:
        level += 1
        subtitle.write(f"Level {level}",align="center",
                       font=("Courier",24,"normal"))
        vx_obs = vx_obstacle*level
        obstacle.dx = (2*(obstacle.dx>=0)-1) * vx_obs
        t0 = time.time()
    if time.time()-t0 >= 3:
        subtitle.clear()
    if random.random() <= attack*level:
        obstacle.dx = -obstacle.dx
subtitle.clear()
subtitle.write(f"Failed at: Level {level}",
               align="center",font=("Courier",24,"normal"))
time.sleep(3)
