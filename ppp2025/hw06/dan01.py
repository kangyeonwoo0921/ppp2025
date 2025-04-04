
def gugudan(dan):
    
    for i in range(9):
        print(f"{dan} * {i+1} = {dan*(i+1)}")
    # result = []
    # for i in range(1, 10):
    #     result.append(f"{dan} * {i} = {dan * i}")
    # return(result)
    
    
def main():
    num = int(input("곱할 수:"))
    result = gugudan(num)
    #for lines in result:
    print(result)

if __name__=="__main__":
    main()
      