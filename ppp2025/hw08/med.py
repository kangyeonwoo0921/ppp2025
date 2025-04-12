def median(nums):
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list)//2]

def read_text(filename):
    with open(filename) as f:
        nums = [(line.strip()) for line in f]
    return nums

def main():
    nums = read_text("ppp2025/hw08/number.txt")
    print(f"중앙값은 {median(nums)}입니다.")
    
if __name__=="__main__":
    main()