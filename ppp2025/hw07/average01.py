def average(nums):
    total = sum(nums)
    average = total/len(nums)
    return average

def main():
    nums_input = "4, 6, 9, 10"
    nums = []
    for text in nums_input.split(","):
        nums.append(int(text))
    # nums = [4, 6, 9, 10]
    print(f"평균값은 {average(nums)}입니다.")
    
if __name__=="__main__":
    main()