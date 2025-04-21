def average(nums):
    return sum(nums)/len(nums)

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_data_int(fname, col_idx):
    weather_datas = [] 
    with open(fname, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(int(tokens[col_idx]))
    return weather_datas
            
def count_bigger_days(nums, criteria):
    cnt = 0
    for num in nums:
        if num >= criteria:
            cnt+= 1
    return cnt

def get_rain_events(rainfalls):
    events = []
    c_days = 0
    for rain in rainfalls:
        if rain > 0:
            c_days += 1
        else:
            if c_days > 0:
                events.append(c_days)
            c_days = 0
    if c_days > 0:
        events.append(c_days)
          
    return events

def rain_events(rainfalls):
    events = []
    total = 0
    for rain in rainfalls:
        if rain > 0:
            total += rain
        else:
            if total > 0:
                events.append(total)
            total = 0
    if total > 0:
        events.append(total)
    return events


    
def sumifs(rainfalls, months, selected=[6, 7, 8]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total += rain
    return total
        

def main():
    #1
    filename = "ppp2025/hw10/weather_db.csv"
    tavgs = get_weather_data(filename, 4)
    print(f"연평균 기온은(acg. of 연평균 {average(tavgs):.2f}입니다")  
     
    #2
    rainfalls = get_weather_data(filename, 9)
    # count_over5_rain = count_bigger_days(rainfalls, 5)
    count_over5_rain = len([x for x in rainfalls if x>=5])
    print(f"5mm이상 강우일수={count_over5_rain}일 입니다")
    
    #3
    print(f"총강수량은 {sum(rainfalls):,.2f}mm 입니다")
    
    #4 최장연속강우일수
    print(f"최장연속강우일수는 ={max(get_rain_events(rainfalls))}일 입니다")
    
    #5 강우이벤트 중 최대강수량
    
    events_total_rain = rain_events(rainfalls)
    print(f"강우이벤트 중 최대강수량은 {max(events_total_rain):.2f}mm 입니다")

    #6 top3 of tmax
    top3_tmax = sorted(get_weather_data(filename, 3))[-3:][::-1]
    print(f"가장 높았던 최고기온 3개는 {top3_tmax}입니다.")
    
    #7 여름철 강수량
    months = get_weather_data_int(filename, 1)
    print(f"여름철 강수량은 {sumifs(rainfalls, months, selected=[6, 7, 8]):.1f}mm입니다")
    
    #8
    filename_20yrs = "ppp2025/hw10/weather01-22.csv" 
    years= get_weather_data_int(filename_20yrs, 0)
    rainfalls = get_weather_data(filename_20yrs, 9)
    print(f"2021년 총 강수량은 {sumifs(rainfalls, years, selected=[2021]):.1f}mm입니다")
    print(f"2022년 총 강수량은 {sumifs(rainfalls, years, selected=[2022]):.1f}mm입니다")
    
    
if __name__=="__main__":
    main()