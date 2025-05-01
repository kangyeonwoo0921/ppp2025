import requests
import os

def download_weather(station_id, year,filenmae):
    
    URL = "https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open("./weather_146_2020.csv", "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)
        
    



def main():
    filename = "./weather_146_2020.csv"
    if not os.path.exists(filename):
        download_weather(146, 2020, "./weather_146_2020.csv")

    # URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    # with open("./weather_146_2020.csv", "w", encoding="UTF-8-sig") as f:
    #     resp = requests.get(URL)
    #     resp.encoding = "UTF-8"
    #     f.write(resp.text)
        
    

if __name__=="__main__":
    main()