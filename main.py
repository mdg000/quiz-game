# 100 Days of Code
# Quiz Game

from art import logo
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

print(logo)

question_bank = []
for i in range(len(question_data)):
    question = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

print("This is a quiz consisting of 25 True or False Questions. Good Luck!\n")

while quiz.still_has_questions():
    quiz.next_question()

print("You finished the Quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
grade = quiz.score / quiz.question_number * 100

if grade > 50:
    print(f"You passed with {round(grade)} %")
else:
    print(f"You failed with {round(grade)} %")


