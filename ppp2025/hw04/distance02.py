import math

x1 = int(input("x1:"))
y1 = int(input("y1:"))

if x1 > 0 and y1 > 0 :
    print("입력하신 좌표는 제 1사분면입니다.")

elif x1 < 0 and y1 > 0 :
    print("입력하신 좌표는 제 2사분면입니다.")
    
elif x1 < 0 and y1 < 0 :
    print("입력하신 좌표는 제 3사분면입니다.")
    
elif x1 > 0 and y1 < 0 :
    print("입력하신 좌표는 제 4사분면입니다.")
    
elif y1 == 0 :
    print("입력하신 좌표는 x축 위에 있습니다.")

elif x1 == 0 :
    print("입력하신 좌표는 y축 위에 있습니다.")
    
x2 = int(input("x2:"))
y2 = int(input("y2:"))

if x2 > 0 and y2 > 0 :
    print("입력하신 좌표는 제 1사분면입니다.")

elif x2 < 0 and y2 > 0 :
    print("입력하신 좌표는 제 2사분면입니다.")
    
elif x2 < 0 and y2 < 0 :
    print("입력하신 좌표는 제 3사분면입니다.")
    
elif x2 > 0 and y2 < 0 :
    print("입력하신 좌표는 제 4사분면입니다.")
    
elif y2 == 0 :
    print("입력하신 좌표는 x축 위에 있습니다.")

elif x2 == 0 :
    print("입력하신 좌표는 y축 위에 있습니다.")
    

distance = math.sqrt((x2-x1)**2 + (y2 -y1)**2)



print(f"지점의 거리는 {distance:.3f}입니다.")

