fruit_cal = {
    "한라봉":0.5,
    "딸기(설향)": 0.34,
    "바나나": 0.77   
}

fruit_eat = {
    "한라봉": 150,
    "딸기(설향)": 200,
    "바나나": 100
}

fruit_list = ["한라봉", "딸기(설향)", "바나나"]

total = 0
for item in fruit_eat.keys():
    print(item)
    # print(item, fruit_cal[item], fruit_eat[item], 
    #       fruit_cal[item] * fruit_eat[item])
    total += fruit_cal[item] * fruit_eat[item]
   
print(f"총 칼로리는{total} kcal입니다.")


