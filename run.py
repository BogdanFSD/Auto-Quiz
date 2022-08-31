from questions import question_list
import random






def prepare_quiz_questions():
    """
   Function that will randomize order of our
   questions for a quiz
   """
    random.shuffle(question_list)

class Game:
    """
    This is the logic of the quiz.
    That helps programm runs properly
    and display everything in correct order
    """
    def __init__(self, que_list):
        self.question_number = 0
        self.score = 0
        self.que_list = que_list

    def n_question(self):
        """
        Prints question in the order of question number
        with relevant options for answer and answer

        """
        empty_string = ''  # to give some space between text
        nl = '\n'  # Prints questions and options from new string
        following_q = self.que_list[self.q_number]
        # prints each option from new line and not in the brackets
        following_q['options'] = '\n'.join(following_q['options'])
        self.q_number += 1  # increment question number
        while True:   # loop that validate users answer
            user_answer = input(f"{Fore.LIGHTMAGENTA_EX}{self.q_number})\
 {following_q['question']}{nl}{empty_string}{nl}{Fore.LIGHTYELLOW_EX}\
{following_q['options']}{nl} {empty_string}{Fore.LIGHTBLUE_EX}\
 {nl}Please choose A, B, C or D  ").upper()  # prints question
            if user_answer in {"A", "B", "C", "D"}:
                break  # validate answer
            else:
                print()
                print('Invalid entry. Please try again ')
                print()

        def question_left(self):
        """
        checks if any questions left after printed one
        """
        # returns true if we have another question
        return self.q_number < len(self.que_list)









"""def greeting_screen():
    print("Welcome to a Fun Car Quiz! \nAre you ready to check your knowledge?")
    print("There are total of 4 question and 4 answers to each of them. Once you are done with all question you will receive your score.")
    print(r"""
                                                ______--------___
                                        /|             / |
                            o___________|_\__________/__|
                            ]|___     |  |=   ||  =|___  |"
                            //   \\    |  |____||_///   \\|"
                            |  X  |\--------------/|  X  |\"
                            \___/       1924        \___/
        """)


    while True:
        start = input("Are you ready for a rummmmmmble? (Yes/No) ")

        if start.lower() == "yes":
            print("great")
            start_game()
            return True

        elif start.lower() == "no":
            print("BYEEE")
            quit()

        else:
            print("Invalid entry. Yes or No")

            continue

    start_game()

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

    score = int((correct_attempts/len(questions))*100)
    print("your score is " + str(score)+ "%")

    restart()

def restart():
    while True:
        response = input("Do you want to continue? (Yes/No) ")

        if response.lower() == "yes":
            print("great")
            start_game()
            return True

        elif response.lower() == "no":
            print("BYEEE")
            quit()

        else:
            print("Invalid entry. Yes or No")

            continue




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


if __name__ == "__main__":
    greeting_screen()
"""
