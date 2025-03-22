import sys

calories = [50, 34, 77] 

H_g = float(input("한라봉 섭취량:"))
S_g = float(input("딸기(설향) 섭취량:"))
B_g = float(input("바나나 섭취량:"))
 
if H_g > 0 or S_g > 0 or B_g > 0 :
    print("계산할 수 없습니다.")
    sys.exit()

if H_g == 0 and S_g == 0 and B_g == 0 :
    print("섭취량이 없습니다.")
    sys.exit()


total_kcal = calories[0] * H_g + calories[1] * S_g + calories[2] * B_g

print(f"총 칼로리: {total_kcal:.2f}kcal/100g")