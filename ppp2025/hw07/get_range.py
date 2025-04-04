def get_range_list(n):
    n_list = []
    for i in range(1, n+1): 
        n_list.append(i)
    return n_list

def main():
    n = int(input("숫자를 입력하시오."))
    print(f"리스트는 {get_range_list(n)}입니다.")

if __name__=="__main__":
    main()
        
    