#A quiz game with a question and answer format

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]

for item in question_data:
    q = Question(item["text"], item["answer"])
    question_bank.append(q) #creates a list of Question objects

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'Thanks for playing!  Your score was {quiz.score}!')