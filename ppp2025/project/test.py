import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import koreanize_matplotlib 

#생체량 계산식
def biomass_concentration(W_1, W_2, V):
    X = (W_2 - W_1) / V
    return X

#생장률 계산식
def specific_growth_rate(X_1, X_2, t_1, t_2):
    u = (np.log(X_2) - np.log(X_1)) / (t_2 - t_1)
    return u

#수확량 계산식
def productivity (X, t):
    P = X / t
    return P

#로지스틱 생장 모델
def growth_model(X_0, K, r, t_predict):
    X_t = K / (1 + (K - X_0 / X_0) * np.exp(-r * t_predict))
    return X_t
    
# 생장 곡선 기반 수확시점 계산식
def harvest_time(r, X_0, K, alpha):
    t_harvest = (1 /r) * np.log( ((K - X_0) / X_0) * (1 / (1/alpha - 1)) )
    return t_harvest


def main():
    file_path_01 = "C:\code\ppp2025\project\growth_rate.CSV"
    df = pd.read_csv(file_path_01, encoding="utf-8-sig")
 
    
    fig, axs = plt.subplots(2,2)
    
    #생장률 그래프
    t_1= (df["t1"])
    t_2= (df["t2"])
    X_1= (df["X1"])
    X_2= (df["X2"])
    
    df["date"] = (df["t1"] + df["t2"])/ 2 
    
    growth_biomass= specific_growth_rate(X_1, X_2, t_1, t_2)
    df["growth_biomass"] =growth_biomass
    axs[0, 0].plot(df["date"], df["growth_biomass"], color = "green", marker = ".", label = "생장률")
    axs[0, 0].set_xlabel("time(day)")
    axs[0, 0].set_ylabel("growth rate")
    axs[0, 0].legend()
    
    
    #생체량, 수확량 그래프
    W_1= (df["W1"])
    W_2= (df["W2"])
    t= (df["t2"] - df["t1"])
    V = (df["volume"])
    
    df["biomass_rate"] = biomass_concentration(W_1, W_2, V)
    df["productivity_rate"] = productivity(df["biomass_rate"], t)
    axs[0, 1].plot(df["date"], df["biomass_rate"], color = "red", marker = "." , label = "생체량")
    axs[0, 1].plot(df["date"], df["productivity_rate"], color = "blue", marker = ".", label = "수확량")
    axs[0, 1].set_xlabel("time(day)")
    axs[0, 1].set_ylabel("biomass(g/L)")
    axs[0, 1].legend()
    
    
    #로지스틱 생장 모델
    X_0 = (df["X1"].iloc[0])
    K = (df["X2"].max())
    r = (df["growth_biomass"].mean())
    t_predict = np.arange(0, 20, 0.1)
    alpha = 0.9
    
    X_t_predict = growth_model(X_0, K, r, t_predict)
    t_harvest = harvest_time(r, X_0, K, alpha)
    axs[1, 0].plot(t_predict, X_t_predict, color = "green", marker= ".", label = "예측 생체량" )
    axs[1, 0].axvline(x = t_harvest, color = "red", linestyle = "dashed", label = "예상 수확시점")
    axs[1, 0].set_xlabel("time(day)")
    axs[1, 0].set_ylabel("biomass(g/L)")
    axs[1, 0].set_title("로지스틱 생장모델")
    axs[1, 0].legend()
   
   #누적 생산량
    df["cumulative_biomass"] = df["biomass_rate"].cumsum()
    axs[1, 1].plot(df["date"], df["cumulative_biomass"], color = "green", marker = ".", label = "누적 생산량")
    axs[1, 1].set_xlabel("time(day)")
    axs[1, 1].set_ylabel("biomass(g/L)")
    axs[1, 1].set_title("누적 총 생산량")
    axs[1, 1].legend()
    
    
    plt.tight_layout()
    
    plt.savefig("spirulina.png", dpi = 300,
                transparent = False)
    
    

if __name__=="__main__":
    main()
    