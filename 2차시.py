# chapter3(프로그래밍 기초)~chapter(import 사용법)


#chapter3(포로그래밍 기초)

score = 0
print(score)
score = score + 100
print(score)


job = "초보 검사"
print("당신의 직업은 " + job)
print("클래스를 변경했다！")
job = "신출내기 용사"
print("새로운 직업은 " + job)


enemy = ["슬라임", "해골 병사", "마법사"]
print(enemy[0])
print(enemy[1])
print(enemy[2])


life = 0
if life <= 0:
    print("게임 오버입니다")
if life > 0:
    print("게임을 계속합니다")


gold = 100
if gold == 0:
    print("소지금이 없습니다")
else:
    print("구입을 계속하시겠습니까?")


def recover(val):
    print("당신의 체력은 ")
    print(val)
    print("회복했다！")

recover(100)


def add(a, b):
    return a + b

c = add(1, 2)
print(c)

#========================

#chapter4(import 사용법)

import calendar

print(calendar.month(2020, 2))
######


import calendar

print(calendar.isleap(2020))
#####

import datetime

print(datetime.date.today())
#####

import datetime

d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)
###########################

import datetime

today = datetime.date.today()
birth = datetime.date(1971, 2, 2)
print(today - birth)
###########################

import random

srp = random.choice(["가위", "바위", "보"])
print(srp)
############################

import random

cnt = 0
while True:
    r = random.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break
print(str(cnt) + "번째에 희귀 캐릭터 겟!")