def read_db(filename):
    tavg_list = []
    rainfall_list = []
    rainy_day = 0
    
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line= line.strip()
            tokens = line.split(",")
            tavg=float(tokens[4])
            rainfall=float(tokens[9])
            
            tavg_list.append(tavg)
            rainfall_list.append(rainfall)
            
            if rainfall >= 5:
                rainy_day = rainy_day + 1
                
    return tavg_list, rainfall_list, rainy_day
            
       
def average(nums):
    return sum(nums)/len(nums)


def main():
    tavg_list, rainfall_list, rainy_day = read_db("ppp2025/hw09/weather_db.csv")
    
    avg_tem = average(tavg_list)
    total_rain = sum(rainfall_list)
    
    print(f"연평균기온은 {avg_tem:.2f}°C입니다.")
    print(f"총강우량은 {total_rain:.2f}mm입니다.")
    print(f"5mm 이상 강우 일수는 {rainy_day}일 입니다.")


    
if __name__=="__main__":
    main()