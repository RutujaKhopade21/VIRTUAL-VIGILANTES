import random
import time

class Quiz:
    def __init__(self, ques):
        self.ques = ques
        self.score = 0

    def display_question(self, question):1
        print(question['text'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

    def get_user_ans(self):
        while True:
            try:
                user_input = int(input("Your answer: "))
                if 1 <= user_input <= 4:
                    return user_input
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def start_quiz(self):
        random.shuffle(self.ques)

        for question in self.ques:
            self.display_question(question)
            start_time = time.time()

            user_answer = self.get_user_ans()

            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time > 10:
                print("Time's up! You took too long to answer.")
            elif user_answer == question['correct_option']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question['correct_option']}: {question['options'][question['correct_option'] - 1]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.ques)}")

questions = [
    {
        'text': 'In Which fort was Chhatrapati Shivaji Maharaj born?',
        'options': ['Shivneri Fort', 'Raigad Fort', 'Red Fort', 'Pratapgad Fort'],
        'correct_option': 1
    },
    {
        'text': "What was the name of Chhatrapati Shivaji Maharaj's mother?",
        'options': ['Putalabai', 'Soyarabai', 'Jijabai', 'Sakvarbai'],
        'correct_option': 3
    },
    {
        'text': "What was the name of Chhatrapati Shivaji Maharaj's father?",
        'options': ['Shahaji', 'Sai', 'Vyankoji', 'None of the above'],
        'correct_option': 1
    },
    {
        'text': "Who was the first wife of Chhatrapati Shivaji Maharaj?",
        'options': ['Sagunabai', 'Saibai', 'Laxmibai', 'Gunwantabai'],
        'correct_option': 2
    },
]

quiz = Quiz(questions)
quiz.start_quiz()