import math

r = float(input("반지름:"))
pi = math.pi

area = pi * pow(r, 2)

print(f"반지름이 {r}인 원의 면적은 {area:.3f}이다.")