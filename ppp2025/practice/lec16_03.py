import random


def main():
    problems = ["banana", "apple"]
    
    solution = problems[random.randrange(len(problems))]
    solution = "apple"
    is_correct = False

    lives = 5
    
    
    answer = ["_" for n in range(len(solution))]
    print(answer)
    
    
    
    while True:
        answer = input(f"{''.join(answer)}?")

if __name__=="__main__":
    main()