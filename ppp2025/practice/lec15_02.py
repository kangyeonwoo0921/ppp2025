import random





def main():
    problems = ["바나나", "딸기", "토마토", "복숭아"]
    
    
    solution = problems[0]
    is_correct = False

    
    for i in range(3):
        answer = input("ㅂㄴㄴ?")
        if answer == solution:
            print("정답입니다.")
            break 
        else:
            print("다시 도전하세요.")
            
            
    if is_correct:
        print("게임오버")
    
    else: 
        print("축하합니다")            
            
if __name__=="__main__":
    main()