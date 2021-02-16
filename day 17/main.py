from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import Tk

questions = [ Question(q['text'], q['answer']) for q in question_data ]

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!")
print(f'Youre final score was: {quiz.score}/{len(quiz.q_list)}')