import math

weight = int(input("몸무게가 얼마인가요"))
height = int(input("키가 얼마인가요"))

height_m = height/100

BMI = round(weight / pow(height_m, 2))
print("키는{}cm, 몸무게는{}kg, {}BMI".format(height, weight, BMI))