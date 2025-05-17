def average(nums):
    return sum(nums)/len(nums)


def ignore_str(text:str) -> int:
    try:
        val =int(text)
        
        if val > 0:
            return val
    except ValueError:
        return None

def main():
    
    nums = []
    
    while True:
        x =input("X= ").strip()
        if x == "-1":
            break
        
        val = ignore_str(x)
        if val is not None:
            nums.append(val)
    
    print(f"입력된 값은 {nums}이고, 총 개수는 {len(nums)}, 평균은 {average(nums)}입니다.")
    
if __name__=="__main__":
    main()