# import randon to randomize questions
import random

# import questions for our Quiz

from questions import question_list


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
    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.que_list = q_list

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
            user_answer = input(f"{self.q_number})\
 {following_q['question']}{nl}{empty_string}{nl}\
{following_q['options']}{nl} {empty_string}\
 {nl}Please choose A, B, C or D  ").upper()  # prints question
            if user_answer in {"A", "B", "C", "D"}:
                break  # validate answer
            else:
                print()
                print('Invalid entry. Please try again ')
                print()

        self.validation_a(user_answer, following_q['correctOption'])

    def question_left(self):
        """
        checks if any questions left after printed one
        """
        # returns true if we have another question
        return self.q_number < len(self.que_list)

    def validation_a(self, user_answer, answer):
        """
        Compares answer of the user and correct answer to
        the question
        """
        if user_answer.upper() == answer.upper():
            self.score += 1  # Once correct increment score
            print()
            print('CORRECT')
            print()
        elif user_answer.upper() != answer.upper():
            self.score += 0  # once worn prints statement and add 0 to score
            print()
            print('WRONG')
            print()
            print(f"correct is {answer}")  # shwos correct answer
            print()
        # shows score overall till that question included
        print(f"Current score is {self.score} out of 10")
        print()


def greetings():
    """
    functoins that asks the name of the user
    and prints out questions
    """
    print('*' * 50)
    print()
    print('            WELCOME TO AUTO QUIZ')
    print()
    print(r"""
                        ______--------___
                  /|             / |
      o___________|_\__________/__|
      ]|___     |  |=   ||  =|___  |"
      //   \\    |  |____||_///   \\|"
      |  X  |\--------------/|  X  |\"
       \___/                  \___/
         """)
    print('*' * 50)
    print()
    print('    GAME INFO')
    print()
    print('This is QUIZ for people who think they\
   KNOW  something about a AUTO World')
    print('If you are one of them than E-ron-don-don!!!')
    print()

    name = input('What is your name stranger?  ')

    while len(name.strip()) == 0:  # checks if the name is empty
        print('Please enter not empty name.')
        name = input('What is your name stranger? ')
    while name.isnumeric():  # gives error if input numbers
        print('Please use letters only.')
        name = input('What is your name stranger? ')
    print()

    # validates the input
    start = input(f"{name} are you ready\
 for a rummmmmmble? (Yes/No) ")

    while True:

        if start.lower() == "yes":
            print("Awesome")
            print()
            print('Please be carefull questions are TRICKY!!!')
            print()
            while game.question_left():
                game.n_question()  # prints the questions
            print('    You finish this AUTO\
 Quiz. Thank you! See you later!!!')
            return True

        elif start.lower() == "no":
            print('byeeeeee')
            quit()

        else:
            print("Invalid entry. Please try again  ")
            print()
            start = input(f"{name} are you\
 ready for a rummmmmmble? (Yes/No) ")


prepare_quiz_questions()
game = Game(question_list)
greetings()
