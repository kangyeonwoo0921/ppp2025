def num_n(n):
    total = 0
    for i in range(1, n+1):
        total += i   
    return (total)

def main():
    number = int(input("수를 입력하시오:"))
    print(num_n(number))
    
if __name__=="__main__":
    main()