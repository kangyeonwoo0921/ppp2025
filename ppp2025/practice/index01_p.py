def minmax(nums):
    return min(nums), max(nums)
    

def main():
    # test_input = "3, 4, 5, 6, 7, 8, 18, 9, 10"
    # print(test_input.split())
    numbers = [3, 4, 5, 6, 7, 8, 18, 9, 10]
    nums = []
    for text in test_input.split(","):
        nums.append(int(text))
        
    # nums = [int(x) for x in test_input.split(",")]
    # nums = [A for B in C]
    print(nums)
    
    mn, mx = minmax(numbers)
    
    print(f"최댓값은 {mx}입니다.")
    print(f"최솟값은 {mn}입니다.")

if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
