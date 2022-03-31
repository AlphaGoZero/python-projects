class Quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_reply = input(f"Q.{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(user_reply, current_question.answer)


    def still_have_question(self):
        return (len(self.question_list) > self.question_number)


    def check_answer(self, user_reply, question_answer):
        if user_reply.lower() == question_answer.lower():
            print("You are correct")
            self.score += 1
        else:
            print("It's wrong")
        print(f"The correct answer is {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
