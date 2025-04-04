def largest(nums):
    largest_num = nums[0]
    for num in nums:
        if largest_num < num:
            largest_num = num
    return largest_num




def main ():
    
    # a = 3
    # b = 4
    # c = 9
    # d = 8
    
    nums = [3, 4, 9, 8, 10, 11]
    print(f"가장 큰 수는 {largest(nums)}입니다.")

if __name__=="__main__":
    main()    
    
# def big(a, b):
# return big(big(big(x1, x2), x3) ,x4)


