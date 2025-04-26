from lec10_01 import get_weather_data

def get_weather_dates(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates

def gdd(tavg):
    temp_cum = 0
    base_temp = 5
    for t in tavg:
        if t >= base_temp:
            temp_cum += (t-base_temp)
    return temp_cum
        

def gdd_season(tavg, dates):
    temp_cum = 0
    base_temp = 5
    for i in range(len(tavg)):
        t = tavg[i]
        if dates[i][1] in [5, 6, 7, 8, 9]:
            if t >= base_temp:
                temp_cum += (t-base_temp)
    return temp_cum
        



def main():
    filename = "ppp2025/practice/weather_db.csv" 
    dates = get_weather_dates(filename)
    tavg = get_weather_data(filename, 4)
    print(f"GDD는 {gdd(tavg):.1f}입니다.")
    print(f"여름철 GDD는 {gdd_season(tavg, dates):.1f}입니다.")
    
if __name__=="__main__":
    main()
    