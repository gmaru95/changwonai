나이 = int(input("나이 입력 : "))
walk = int(input("걸음수 입력 :"))
time = 12
if 나이 < 20:
    print("청소년 할인")
else:
    print("할인불가")

if walk >= 1000:
    print("목표달성")
else:
    print("목표실패")

if time<12:
    print("오전")
else:
    print("오후")