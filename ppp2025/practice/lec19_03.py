import requests
import pandas as pd
import matplotlib.pyplot as plt

def download_weather(station_id, year,filename):    
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)
        



def main():
    filename = "weather_146_2024.csv"
    download_weather(146, 2024, filename)   
    
    df = pd.read_csv(filename, skipinitialspace=True)
    df["tdiff"] = df["tmax"]- df["tmin"]
    
    
    fig, ax = plt.subplots()
    df["date"]  = pd.to_datetime(df[["year", "month", "day"]])
    df[df["month"]==3].plot("day", "tavg", ax=ax)
    df.plot(x= "date", y = "tavg", ax=ax)
    plt.show()
    
if __name__=="__main__":
    main()