def average(nums):
    return sum(nums)/len(nums)


def read_text(filename):
    
    with open(filename) as f:
     nums = [int(line.strip()) for line in f]
     
    return nums

def main():
    nums = read_text("ppp2025/hw08/number.txt")
    print(f"평균값은 {average(nums)}입니다.")
    
if __name__=="__main__":
    main()