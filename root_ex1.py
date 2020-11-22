def root_ex():
    a = int(input('2차항계수:'))
    b = int(input('1차항계수:'))
    c = int(input('상수는:'))
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2

r1, r2 = root_ex()    
print("해는{}또는{}".format(r1,r2))