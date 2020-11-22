def func(shape, width = 1, height=1, radius =1):
    if shape == 0:
        return width * height
    if shape == 1:
        return 3.14* radius **2

print("rect=",func(0, width= 10, height=2))
print("circle=",func(1, radius=5))