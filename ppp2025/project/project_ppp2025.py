import math


#가정용 키트 기반
def spi_purchase(V, D_max, T , I, stirring):
    
    #온도 계수
    f_T = math.exp((-(T-32)**2 )/(32))
    
    #빛 계수
    f_I = I / (I + 80)
    
    
    if stirring == "O":
        f_mix = 1.0
    else:
        f_mix = 0.85
        
    return V * D_max * f_T * f_I * f_mix
    


def main():
    D_max = 2.5
    V = float(input("수조부피(L):"))
    T = float(input("온도(℃): "))
    I=  float(input("광도(µmol/m²/s): "))
    stirring = str(input("교반(O, X): "))
    
    purchase = spi_purchase(V, D_max, T, I, stirring)
    
    print(f"예상 수확량은 {purchase:.2f}")
    

if __name__=="__main__":
    main()