def read_db(filename):
    calorie_dic = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            line.split()
            tokens = line.split(",")
            calorie_dic[tokens[0]]= int(tokens[1])
                        
    return calorie_dic
            
    
def main():
    fruit_cal = read_db("ppp2025/hw09/calorie_db.csv")
    
    fruit_eat= {}
    inputs = input("과일이름과 그램수를 입력하시오:").split(",")
    
    for pair in inputs:
        name, gram = pair.strip().split()
        fruit_eat[name] = float(gram)
        
    
    total = 0
    for item in fruit_eat:
        total +=fruit_eat[item] * fruit_cal[item]
         
    print(f"총 칼로리는 {total}kcal 입니다.")
    
if __name__=="__main__":
    main()