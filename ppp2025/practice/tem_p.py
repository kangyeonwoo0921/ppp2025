
def f2c(tf):
     return(tf - 32)* 5 / 9

def main():
    
    temp_f = 80
    temp_c = f2c(temp_f)
    print(f"{temp_f}F -> {temp_c}C")

    
if __name__ == "__main__":
    main()


