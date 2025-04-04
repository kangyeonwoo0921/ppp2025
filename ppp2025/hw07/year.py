def is_leap_year(y):
    if y % 4 == 0:
        return("윤년")
    
    elif y % 4 == 0 and y % 100 == 0:
        return("윤년 아님")

    else:
        return("윤년 아님")
        
def main():
    
    year = int(input("년도를 입력하세요:"))
    print(f"결과는 {is_leap_year(year)}입니다.")

if __name__=="__main__":
    main()
    