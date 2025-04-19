def read_db(filename):
    calorie_dic = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        print(lines)
        for line in lines[1:]:
            line = line.strip()
            line.split()
            tokens = line.split(",")
            calorie_dic[tokens[0]]= int(tokens[1])
                        
    return calorie_dic
            
    
def main():
    fruit_cal = read_db("ppp2025/practice/calorie_db.csv")
    
    fruit_eat = {
        "쑥":150,
        "바나나": 200
    }
    
    total = 0
    for item in fruit_eat:
        total +=fruit_eat[item] * fruit_cal[item]
         
    print(f"총 칼로리는 {total}kcal 입니다.")
    
if __name__=="__main__":
    main()