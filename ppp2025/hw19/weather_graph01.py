import requests
import pandas as pd
import matplotlib.pyplot as plt

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
    
    fig, axes = plt.subplots()
    df["date"] = pd.to_datetime(df[["year", "month", "day"]])
    
    summer_months = df[(df["month"]==6) | (df["month"]==7)| (df["month"]==8)]
    winter_months = df[(df["month"]==12) | (df["month"]==1)| (df["month"]==2)]
    
    summer_avg = summer_months.groupby("year")["tavg"].mean()
    winter_avg = winter_months.groupby("year")["tavg"].mean()
    
    summer_avg.plot(ax=axes, label = "summer", color = "red")
    winter_avg.plot(ax=axes, label = "winter", color = "blue")
    plt.show()
    
if __name__=="__main__":
    main()