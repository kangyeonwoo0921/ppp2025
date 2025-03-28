import math


r = float(input("반지름:"))

if r <= 0 :
    print("반지름은 양수여야 합니다.")
 
    
pi = math.pi

area = pi * pow(r, 2)
perimeter = 2 * pi * r


print(f"반지름이 {r}인 원의 면적은 {area:.2f}이다.")
print(f"반지름이 {r}인 원의 둘레는 {perimeter:.1f}이다.")