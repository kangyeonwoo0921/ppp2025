def text2list(txt):
    txt_list = txt.split()
    nums = []
    for num_text in txt_list:
        nums.append(int(num_text))
     
    nums = [int(x) for x in txt_list]
    return nums

def average(nums):
    return sum(nums)/len(nums)


def median(nums):
    # print(nums)
    # print(sorted(nums))
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list)//2]
    
def read_text(filename):
    text = ""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(f"!{line.strip()}!")
            text += " " + line.strip()
        # print(text)
    return text
        
            
def read_numbers(filename):
    nums = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
    return nums


    
def main():  
    text = read_text("ppp2025/practice/number1.txt")
    nums = text2list(text)        
    print(nums)
    print(f"중앙값은{median(nums)}")
    print(f"평균값은 {average(nums)}")
        
if __name__=="__main__":
        main()
        
    
    
    