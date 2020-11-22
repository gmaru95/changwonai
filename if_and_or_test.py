a = int(input("1숫자를 입력하세요"))
b = int(input("2숫자를 입력하세요"))

if(a%2==0)and(b%2==0):
    print("두수 모두 짝수")
elif (a%2==0)or(b%2==0):
    print("둘중 하나는 짝수")
else:
    print("둘다 홀수")