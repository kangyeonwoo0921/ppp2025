import requests
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def download_weather(station_id, year_1, year_2 ,filename):    
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year_1}&ey={year_2}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)
        
def main():
    filename = "weather_112_2024.csv"
    download_weather(112, 1980, 2024, filename)
    
    df = pd.read_csv(filename, skipinitialspace=True)
    
    fig, ax = plt.subplots()
    df["date"] = pd.to_datetime(df[["year", "month", "day"]])
    
    birthday = df[(df["month"]==9) & (df["day"]==21)]   
    birthday.plot("date", "tavg", ax=ax, label = "연우생일", color = "black")
    
    hottest = birthday["tavg"].max()
    coolest = birthday["tavg"].min()
    
    print(f"가장 높은 기온은 {hottest}C 입니다.")
    print(f"가장 낮은 기온은 {coolest}C 입니다.")
   
    
    ax.set_ylabel("평균온도")
    ax.set_xlabel("날짜")
    
    plt.show()
    
    
if __name__=="__main__":
    main()