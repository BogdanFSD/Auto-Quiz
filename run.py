def greeting_screen():
    pass

def start_game():
    """
    function that runs all necessary fnuction to start
    """
    attempts = []
    correct_attempts = 0
    question_num = 0 # index of questions to help me itarate 

    for question in questions:  #
        print("*" * 10) # just to make it more pleasant to for human eye
        print(question)
        for choice in choices[question_num]: 
            print(choice) 

        while True:                    
            attempt = input("Choose an answer A, B, C or D: ").upper()
            if attempt in {"A", "B", "C", "D"}:
                attempts.append(attempt)
                break
            else:
                print("Invalid entry")

        correct_attempts += correct_answers(questions.get(question), attempt)
        question_num += 1

    show_points(correct_attempts, attempts)


def correct_answers(answer, attempt):
    if answer == attempt:
        print("corect")
        return 1
    else:
        print("wrong")
        return 0

def show_points(correct_attempts, attempts):
    print("*" * 10)
    print("result")
    print("Answers: ")
    for i in questions:
        print(questions.get(i))
    print()

    print("Attempts")
    for i in attempts:
        print(i)
    print()

    

def restart():
    pass



questions = {
    "Who Created tesla?": "A",
    "What does BMW stand for?": "C",
    "Which 2020 Audi model has the highest starting MSRP?": "D",
    "Which group is Bentley a subsidiary of?": "A",
    "In which city can you find the headquarters of Kia?": "A"
}

choices = [
    ["A. Elon Musk", "B. Bill Gates", "C. Ford", "D. Johny Depp"],
    ["A. Berlin Motor Works", "B. Brunswick Motor Works","C. Bavarian Motor Works", "D. Borgoholzhausen Motor Works"],
    ["A. Q7", "B. S6", "C. TTS", "D. A8"],
    ["A. Volkswagen Group", "B. PSA", "C. Ford Motor Company", "D. Hyundai Motor Group"],
    ["A. Bangkok", "B. Kuala Lumpur", "C. Singapore ", "D. Seoul "]
    ]


start_game()

