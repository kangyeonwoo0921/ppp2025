import random

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ',
                'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ',
                'ㅌ', 'ㅍ', 'ㅎ']
def to_chosung_ch(ch):
    return(ord(ch) - ord("가"))//588

def to_chosung(text):
    full_text = []
    for ch in text:
        index = to_chosung_ch(ch)
        
        if 0 <= index <= len(chosung_list):
            full_text.append(chosung_list[index])
        else:
            full_text.append(ch)
    return "".join(full_text)




def main():
    problems = ["바나나", "딸기", "토마토", 
                "복숭아", "망고", "포도", "샤인머스켓"]
    
    solution = problems[random.randrange(len(problems))]
    is_correct = False

    print(f"문제를 맞춰보세요! 초성:{to_chosung(solution)}")
    
    for i in range(3):
        answer = input("정답을 입력하세요: ")
        if answer == solution:
            print("정답입니다.")
            break
        else:
            print("다시 도전하세요.")
            
    if is_correct:
            print("게임오버")
            
    else:
            print("축하합니다.")
            
if __name__=="__main__":
    main()