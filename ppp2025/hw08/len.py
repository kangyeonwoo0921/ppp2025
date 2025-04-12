def lenght(nums):
    result = len(nums)
    return result

def text2list(text):
    text_list = text.split()
    # nums = []
    # for num_text in text_list:
    #     nums.append(int(num_text))
    nums = [int(x) for x in text_list]
    return nums


def read_text(filename):
    text = ""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            text += " " + line.strip()
    return text

def main():
    text = read_text("ppp2025/hw08/number.txt")
    nums = text2list(text)
    print(f"숫자의 갯수는 {lenght(nums)}")

if __name__=="__main__":
    main()
        
        