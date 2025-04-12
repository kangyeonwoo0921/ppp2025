def maximum(nums):
    result = max(nums)
    return result

def read_text(filename):
    with open(filename) as f:
        nums = [int(line.strip()) for line in f]
    return nums

def main():
    nums = read_text("ppp2025/hw08/number.txt")
    print(f"최댓값은 {maximum(nums)}입니다.")
     
if __name__=="__main__":
    main()