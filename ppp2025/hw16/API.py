import requests

from sfarm_hw import submit_to_api






def main():
    name = "강연우"
    affiliation = "스마트팜학과"
    student_id = "202410055"

    answer1 = 1
    answer2 = 2
    answer3 = 3
    answer4 = 4

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()