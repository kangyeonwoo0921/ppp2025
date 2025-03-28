def main():
    
    fruit_cal= {
        "한라봉": 0.5,
        "딸기": 0.34,
        "바나나": 0.77
    }
    
    fruit_eat = {
        "한라봉":100,
        "딸기": 100,
        "바나나": 100
    }
    
    total = 0
    for item in fruit_eat:
        total +=fruit_eat[item] * fruit_cal[item]
        
    print(f"총 칼로리는 {total}kcal 입니다.")
    
if __name__=="__main__":
    main()