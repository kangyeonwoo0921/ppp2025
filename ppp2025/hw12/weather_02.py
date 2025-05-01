import requests
import os

def download_weather_db(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open("./weather_146_2020.csv", "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def average(tavg):
    return sum(tavg)/len(tavg)




def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas


def main():
    filename = "./weather_146_2020.csv"
    if not os.path.exists(filename):
        download_weather_db(146, 2020, "./weather_146_2020.csv")
        
    tavg=get_weather_data(filename, 4)
    rainfalls = get_weather_data(filename, 9)
    count_over5_rain = len([x for x in rainfalls if x>=5])
    
    print(f"연평균 기온은 {average(tavg):.2f}C 입니다.")
    print(f"5mm이상 강우 일수는 {count_over5_rain}일 입니다.")
    print(f"총 강수량은 {sum(rainfalls):,.2f}mm 입니다.")

if __name__=="__main__":
    main()