
def gugudan(dan):
    result = []
    for i in range(1, 10):
        result.append(f"{dan} * {i} = {dan * i}")
    return(result)
    
    
def main():
    num = int(input("곱할 수:"))
    result = gugudan(num)
    for lines in result:
        print(lines)

if __name__=="__main__":
    main()
      