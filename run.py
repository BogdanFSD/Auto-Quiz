from questions import question_list

import random

import colorama

from colorama import Fore, Style
colorama.init(autoreset=True)



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
            print(Fore.LIGHTGREEN_EX+'corect')
            print()
        elif user_answer.upper() != answer.upper():
            self.score += 0  # once worn prints statement and add 0 to score
            print()
            print(Fore.LIGHTRED_EX+'wrong')
            print()
            print(f"correct is {answer}")  # shwos correct answer
            print()
        # shows score overall till that question included
        print(f"Current score is {self.score} out of 10")
        print()


prepare_quiz_questions()
game = Game(question_list)

while game.question_left():
    game.n_question()




