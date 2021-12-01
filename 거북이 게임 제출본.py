hap = 0
import time
print('게임: 거북이 게임')
time.sleep(1)
print('')
print('게임 설명')
time.sleep(0.5)
print('사물 또는 사물의 일부를 보고 무엇인지 맞추는 게임')
time.sleep(2)
print('')
print('게임 시작!')
time.sleep(1)

import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t1.speed(7)
t1.shape('turtle')
t2.shape('turtle')
t1.pensize(3)
t2.pensize(2)
t3.pensize(5)
t4.pensize(5)
t3.color('orange')
t4.color('orange')
t1.up()
t1.goto(200,0)
t1.down()
t2.goto(0,0)
t1.setheading(90)
t2.setheading(90)

t1.circle(200)

for i in range(12):
    t2.penup()
    t2.forward(150)
    t2.pendown()
    t2.forward(50)
    t2.penup()
    t2.backward(200)
    t2.pendown()
    t2.right(360/12)

t3.dot()
t3.left(35)
t3.forward(100)
t4.right(90)
t4.forward(130)

print('')
print('')
clock=input(str('사물을 맞춰보세요:'))

if clock == '시계':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 시계입니다.')

print()
print('다음 문제')
t1.reset()
t2.reset()
t3.reset()
t4.reset()

import turtle as t
t.shape("turtle")
t.speed(8)
t.pencolor("black")
t.width(13)
t.penup()
t.setposition(0,100)
t.pendown()
t.circle(-170,30)
t.right(90)
t.fillcolor("orange")
t.begin_fill()
t.circle(60)
t.end_fill()
t.left(90)
t.circle(-170,300)
t.left(90)
t.fillcolor("orange")
t.begin_fill()
t.circle(60)
t.end_fill()
t.right(90)
t.circle(-170,30)
t.fillcolor("orange")
t.begin_fill()
t.circle(-170)
t.end_fill()
t.penup()
t.color("black")
t.setposition(-100,7)
t.width(15)
t.pendown()
t.forward(60)
t.penup()
t.setposition(50,7)
t.pendown()
t.forward(60)
t.width(10)
t.penup()
t.setposition(0,-75)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.left(70)
t.circle(-25,310)
t.left(115)
t.circle(-25,310)
t.end_fill()
t.circle(-1)
t.penup()
t.color("black")
t.setposition(-78,-35)
t.pendown()
t.circle(5)
t.penup()
t.setposition(78,-35)
t.pendown()
t.circle(5)

print('')
print('')
lion=input(str('캐릭터를 맞춰보세요:'))

if lion == '라이언':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 라이언입니다.')

print()
print('다음 문제')
t.reset()


import turtle as t

t.ht()
t.penup()
t.goto(0,150)
t.pendown()

t.color("pink")
t.speed(0)
for i in range(150):
    t.pensize(i/10)
    t.fd(i)
    t.left(65)

t.color("green")
t.setheading(270)
for i in range(50):
    t.pensize(20)
    t.fd(i/4)

t.setheading(60)
t.color("yellowgreen")
for x in range(100):
    t.pensize(100-x)
    t.fd(x/10)

t.penup()
t.seth(240)
for x in range(100):
    t.fd(x/10)
t.pendown()

t.setheading(120)
for x in range(100):
    t.pensize(100-x)
    t.fd(x/10)

print('')
print('')
flower=input(str('사물을 맞춰보세요:'))

if flower == '꽃':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 꽃입니다.')

print()
print('다음 문제')
t.reset()

t.bgcolor("pink")

t.color("red")
t.begin_fill()
for i in range(3):
    t.fd(200)
    t.right(360/3)
t.end_fill()

t.fd(100)
t.color("lightgreen")
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(130,130)
t.color("chocolate")
t.begin_fill()
t.circle(70)
t.end_fill()

print('')
print('')
icecream=input(str('사물을 맞춰보세요:'))

if icecream == '아이스크림':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 아이스크림입니다.')

print()
print('다음 문제')
t.reset()
t.bgcolor("white")

import turtle
t=turtle. Turtle ()
t. shape ("turtle")
t. color ("blue")

t.circle(-50)
t.forward(100)
t.left(90)
t.forward(80)
t.left(90)
t.forward(150)

print('')
print('')
thing=input(str('사물을 맞춰보세요:'))

if thing =='자동차':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 자동차입니다.')
time.sleep(0.3)
print()
print('정답공개')
time.sleep(0.5)


t.right(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.right(90)
t.forward(120)
t.left(90)
t.forward(80)
t.left(90)
t.forward(110)
t.circle(-50)
t.forward(230)
time.sleep(1)


t.reset()
import turtle
t=turtle. Turtle ()
t. shape ("turtle")
t. color ("blue")

print()
print('다음 문제')
time.sleep(1)
t.left(90)
t.forward(100)
t.right(130)
t.forward(40)
t.left(90)
t.forward(55)
t.left(90)
t.forward(100)
t.left(40)
t.forward(30)
shirt=input(str('사물을 맞춰보세요:'))

if shirt == '옷':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 옷입니다.')
time.sleep(0.3)
print()
print('정답공개')
time.sleep(0.5)


t.left(40)
t.forward(30)
t.right(90)
t.forward(30)
t.left(50)
t.forward(30)
t.left(45)
t.forward(100)
t.left(90)
t.forward(55)
t.left(90)
t.forward(40)
t.right(133)
t.forward(100)
t.left(88)
t.forward(100)
time.sleep(2)

print()
print('다음 문제')

t.reset()
import turtle

t = turtle.Turtle()
t. shape("turtle")
t. pencolor("#000000")
t. width(5)
t.speed(5)

t.fillcolor("white")
t.up()
t.goto(0, 60)
t.down()
t.begin_fill()
t.circle(-100)
t.end_fill()

t.up()
t.goto(0, 50)
t.down()
t.begin_fill()
t.circle(70)
t.end_fill()

t.color("#000000")
t.up()
t.goto(-20, 120)
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()

t.up()
t.goto(25, 120)
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()

t.up()
t.goto(5, 80)
t.down()
t.color("orange")
t.begin_fill()
t.circle(10, steps = 3)
t.end_fill()

t.color("orangered")
t.up()
t.goto(-53,55)
t. width(30)
t.down()
t.fd(110)

t.color("#000000")
t.up()
t.goto(0, -10)
t. width(5)
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()

t.up()
t.goto(0, -50)
t. width(5)
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()

t.up()
t.goto(0, -95)
t. width(5)
t.down()
t.begin_fill()
t.circle(5)
t.end_fill()

t. pencolor("#000000")
t.up()
t.goto(0, 260)
t.down()
t.fillcolor("orangered")
t.begin_fill()
t.circle(-60, steps = 3)
t.end_fill()

t. pencolor("white")
t.up()
t.goto(-52,170)
t. width(7)
t.down()
t.begin_fill()
t.fd(104)
t.end_fill()

t. pencolor("#000000")
t.up()
t.goto(0, 260)
t. width(3)
t.down()
t.fillcolor("white")
t.begin_fill()
t.circle(5)
t.end_fill()


print('')
print('')
snowman=input(str('사물을 맞춰보세요:'))

if snowman == '눈사람':
    hap = hap + 1
    print('정답입니다.')
    time.sleep(0.3)
    print(hap,'점입니다')
else:
    print('정답이 아닙니다.')
    print('정답은 눈사람입니다.')

t.reset()

time.sleep(1)
print('')
print('최종점수는 :',hap,'점')
print('수고하셨습니다.')
