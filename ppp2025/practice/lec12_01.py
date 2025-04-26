from lec10_01 import get_weather_data

def get_weather_dates(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates



def maximum_temp_gap(dates, tmax, tmin):
    max_gap_date = dates[0]
    max_gap = tmax[0]-tmin[0]
    for i in range(len(dates)):
        date = dates[i]
        tx = tmax[i]
        tn = tmin[i]
        gap = tx -tn
        if max_gap < gap:
            max_gap = gap
            max_gap_date = date
    return [max_gap_date, max_gap]



def main():
    filename = "ppp2025/practice/weather_db.csv" 
    dates = get_weather_dates(filename)
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)
    max_gap_date, max_gap = maximum_temp_gap(dates, tmax, tmin)
    print(f"일교차가 가장 큰 일자는 {max_gap_date}입니다. 해당일의 일교차는 {max_gap}도 입니다.")    
    

if __name__=="__main__":
    main()
    
# 2022 18,7