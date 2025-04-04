def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for fruit in fruits:
        total += fruits_calorie_dic[fruit]* fruits[fruit]
    return total

def main():
     fruit = {"딸기": 300, "한라봉": 150}
    
     fruit_calorie_dic = {"한라봉":
    0.5, "딸기": 0.34, "바나나": 0.77}
     
     print(f"총 칼로리는 {total_calorie(fruit, fruit_calorie_dic)}kcal입니다.")
     
if __name__ == "__main__":
    main()
     
     
    