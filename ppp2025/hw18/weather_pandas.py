import pandas as pd
import requests
from sfarm_hw import submit_to_api

def download_weather(station_id, year,filename):    
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)
        
        

        

def main():
    file_2012 = "weather_146_2012.csv"
    download_weather(146, 2012, file_2012)
    
    file_2024 = "weather_146_2024.csv"
    download_weather(146, 2024, file_2024)
    
    file_2020 ="weather_146_2020.csv"
    download_weather(146, 2020, file_2020)
    
    file_2019 = "weather_146_2019.csv"
    download_weather(146, 2019, file_2019)
    
    file_2019_s = "weather_119_2019.csv"
    download_weather(119, 2019, file_2019_s)
    
    df_2012 = pd.read_csv(file_2012, skipinitialspace=True)
    df_2024 = pd.read_csv(file_2024, skipinitialspace= True)
    df_2020 = pd.read_csv(file_2020, skipinitialspace=True)
    df_2019 = pd.read_csv(file_2019, skipinitialspace=True)
    df_2019_s = pd.read_csv(file_2019_s, skipinitialspace=True)
    
    df_2020["tdiff"] = df_2020["tmax"] - df_2020["tmin"]
    t_rainfall_2019 = df_2019["rainfall"].sum()
    t_rainfall_2019_s = df_2019_s["rainfall"].sum()
    rainfall_gap = round(abs(t_rainfall_2019 - t_rainfall_2019_s))

    
    print(round(df_2012["rainfall"].sum(), 1))
    print(df_2024["tmax"].max())
    print(df_2020["tdiff"].max())
    print(round(abs(rainfall_gap), 1))
    
    name = "강연우"
    affiliation = "스마트팜학과"
    student_id = "202410055"

    answer1 = round(df_2012["rainfall"].sum(), 1)
    answer2 = df_2024["tmax"].max()
    answer3 = df_2020["tdiff"].max()
    answer4 = round(abs(rainfall_gap), 1)
    

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

   
    
    
if __name__=="__main__":
    main()



        