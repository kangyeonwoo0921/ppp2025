H_kcal = 50
S_kcal = 33
B_kcal = 77

H_g = float(input("한라봉 섭취량:"))
S_g = float(input("딸기(설향) 섭취량:"))
B_g = float(input("바나나 섭취량:"))
 
total_kcal = (H_g/100 * H_kcal) + (S_g/100 * S_kcal) + (B_g/100 * B_kcal)
print(f"총 칼로리: {total_kcal:.2f}kcal/100g")