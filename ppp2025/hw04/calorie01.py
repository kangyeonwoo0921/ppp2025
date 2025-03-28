

calories = {
    "한라봉":50,
    "딸기(설향)": 34,
    "바나나": 77   
}

H_g = float(input("한라봉 섭취량:"))/100
S_g = float(input("딸기(설향) 섭취량:"))/100
B_g = float(input("바나나 섭취량:"))/100
 
if H_g < 0 or S_g < 0 or B_g < 0 :
    print("계산할 수 없습니다.")
    
if H_g == 0 and S_g == 0 and B_g == 0 :
    print("섭취량이 없습니다.")
 


total_kcal = calories["한라봉"] * H_g + calories["딸기(설향)"] * S_g + calories["바나나"] * B_g

print(f"총 칼로리: {total_kcal:.2f}kcal/100g")