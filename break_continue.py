st = 'Programming'
# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        break # 모음일 경우 반복문을 종료한다.
    print(ch)
print('The end')

st_1 = input()
#자음이 나타날때만 출력하는 기능
for ch in st_1:
    if ch in ['a','e','i','o','u']:
        continue # 모음일 경우 아래 출력을 건너뛴다.
    print("자음만 출력",ch)
print('The end')