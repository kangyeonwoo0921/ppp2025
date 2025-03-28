import math

weight = int(input("몸무게가 얼마인가요"))
height = int(input("키가 얼마인가요"))

height_m = height/100

BMI = round(weight / pow(height_m, 2))

if 23<= BMI<=24.9:
    print("비만 전 단계입니다.")

elif 25<=BMI<=29.9:
    print("1단계 비만입니다.")

elif 30<=BMI<=34.9:
    print("2단계 비만입니다.")

elif BMI<50:
    print("3단계 비만입니다.")
    
else:
    print("정상입니다.")
    

print(f"키는{height}cm, 몸무게는{weight}kg, BMI는{BMI}")

