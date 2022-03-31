from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still_have_question():
    #include the check answer and score system
    quiz.next_question()

print("Here is the end of quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")