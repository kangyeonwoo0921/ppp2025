# from practice.largest01_p import largest


def minmax(nums):
    return min(nums), max(nums)
    # max_num = nums[0]
    # min_num = nums[0]
    
    # for num in nums:
    #     if max_num < num:
    #         max_num = num
    #     if min_num > num:
    #         min_num = num
    # return min_num, max_num



def main():
    numbers = [3, 4, 5, 6, 7, 8, 18, 9, 10]
    
    mn, mx = minmax(numbers)
    
    print(f"최댓값은 {mx}입니다.")
    print(f"최솟값은 {mn}입니다.")

if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
