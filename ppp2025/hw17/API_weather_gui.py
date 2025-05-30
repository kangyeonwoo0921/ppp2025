import requests
import os
import tkinter as tk
from tkinter import simpledialog
import rich

from sfarm_hw import submit_to_api

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="입력창", prompt=text)





def download_weather(station_id, year,filename):    
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)
        
def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas
   
def best_gap_2024(tmax, tmin):
    max_gap = 0
    for i in range(1, len(tmax)):
        gap = tmax[i] - tmin[i]
        if gap > max_gap:
            max_gap = gap
    return max_gap




def main():
    file_2015 = "./weather_146_2015.csv"
    if not os.path.exists(file_2015):
        download_weather(146, 2015, "./weather_146_2015.csv")
    rainfall_2015 = get_weather_data(file_2015, 9)
    
    file_2022 = "./weather_146_2022.csv"
    if not os.path.exists(file_2022):
        download_weather(146, 2022, "./weather_146_2022.csv")
    tavg_2022 = get_weather_data(file_2022, 4)
    
    file_2024 = "./weather_146_2024.csv"
    if not os.path.exists(file_2024):
        download_weather(146, 2024, "./weather_146_2024.csv")
    tmin_2024 = get_weather_data(file_2024, 5)
    tmax_2024 = get_weather_data(file_2024, 3)
    rainfall_2024 = get_weather_data(file_2024, 9)
    
    file_2024_suwon = "./weather_119_2024.csv"
    if not os.path.exists(file_2024_suwon):
        download_weather(119, 2024, "./weather_119_2024.csv")
    rainfall_2024_suwon = get_weather_data(file_2024_suwon, 9)
    
    
    
    rainfall_gap = abs(sum(rainfall_2024)- sum(rainfall_2024_suwon))
    

    
    rich.print(f"전주시 2015년 연 강수량은 [bold blue]{sum(rainfall_2015):.1f}mm[/bold blue]입니다. :cloud:")
    rich.print(f"전주시 2022년 최대기온은 [bold blue]{max(tavg_2022)}C[/bold blue]입니다. :sun:")
    rich.print(f"전주시 2024년 최대일교차는 [bold blue]{best_gap_2024(tmax_2024, tmin_2024)}C[/bold blue]입니다. :sun:")
    rich.print(f"수원시와 전주시 2024년 총강수량 차이는 [bold blue]{rainfall_gap:.1f}mm[/bold blue]입니다. :cloud:")
    
    name = gui_input("이름을 입력하세요")
    affiliation = gui_input("학과를 입력하세요")
    student_id = gui_input("학번을 입력하세요")

    answer1 = round(sum(rainfall_2015), 1)
    answer2 = max(tavg_2022)
    answer3 = best_gap_2024(tmax_2024, tmin_2024)
    answer4 = round(rainfall_gap, 1)

    # submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

   
    
    

if __name__=="__main__":
    main()
