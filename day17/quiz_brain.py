class QuizBrain:
    def __init__(self, input_list):
        self.question_number = 0
        self.question_list = input_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(answer, current_question.answer)
       
    def still_has_questions(self):        
        if self.question_number == len(self.question_list):
            return False
        else:
            return True
    
    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
