def get_weather_data(filename, col_idx):
    weather_datas = []
    with open (filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_dates(filename):
    weather_dates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates
            

def best_gap_year(tmax, tmin, dates):
    result = []
    
    max_gap_date = dates[0]
    max_gap = tmax[0]-tmin[0]
    current_year = dates[0][0]
    
    for i in range(1, len(dates)):
        tx = tmax[i]
        tn = tmin[i]
        gap = tx - tn
        year, month, day = dates[i]
        
        if year == current_year:
            if max_gap < gap:
                max_gap = gap
                max_gap_date = dates[i]
            
        else:
            result.append([current_year, max_gap_date[1], max_gap_date[2], round(max_gap, 1)])
            
            current_year = year
            max_gap = gap
            max_gap_date = dates[i]   
            
    result.append([current_year, max_gap_date[1], max_gap_date[2], round(max_gap, 1)])
                
    return result
    
    
def gdd_year(tavg, dates):
    result = []
     
    temp_cum = 0
    base_temp = 5
    current_year = dates[0][0]
    for i in range(len(tavg)):
        t = tavg[i]
        year, month, day = dates[i]
        if year == current_year:
            if dates[i][1] in [5, 6, 7, 8, 9]:
                if t >= base_temp:
                    temp_cum+=(t-base_temp)
                    
        else:
            result.append([current_year, temp_cum])
            current_year = year
            temp_cum = 0
            if dates[i][1] in [5, 6, 7, 8, 9]:
                if t >= base_temp:
                    temp_cum+=(t-base_temp)
                    
    result.append([current_year, temp_cum])
            
    return result
        
    


def main():
    filename = "ppp2025/hw11/weather01-22.csv"
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)
    tavg = get_weather_data(filename, 4)
    dates = get_weather_dates(filename)
    gap_results = best_gap_year(tmax, tmin, dates)
    gdd_results = gdd_year(tavg, dates)
    
    print("연도별 최대일교차:")
    for year, month, day, gap in gap_results:
        print(f"- {year}년 {month}월 {day}일: {gap:.1f}도")
        
    print("연도별 적산온도:")
    for year, temp_sum in gdd_results:
        print(f"- {year}년: {temp_sum:.1f}도")
        
   
   
if __name__ == "__main__":
    main() 