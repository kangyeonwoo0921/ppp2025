def c2f(tc):
    return(tc * 9/5) + 32

def main():
    
    temp_c = int(input("섭씨:"))
    temp_f = c2f(temp_c)
    
    print(f"{temp_c}C -> {temp_f}F")
    
if __name__=="__main__":
    main()

