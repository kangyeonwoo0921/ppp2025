def largest(x1, x2, x3):
    if x1 > x2:
        if x1 > x3:
            return x1
        if x1 < x3:
            return x2
        else:
            return x3
    else:
        if x2 > x3:
            if x2 > x1:
                return x2
            if x2 < x1:
                return x1
            else:
                return x3
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




def main():
    a = 5
    b = 9
    c = 2

    print(f"가장 큰 숫자는 {largest(a, b, c)}입니다.")


    
if __name__=="__main__":
    main()
    