class QuizBrain:
    def __init__(self, q_list) -> None:
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        if self.q_number == len(self.q_list):
            print('no more questions')
            return
        question = self.q_list[self.q_number]

        answer = input(f'{self.q_number+1}. {question.text} (True/False) ')
        self.q_number += 1
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list) 

    def check_answer(self, input, correct_ans):
        if input.lower() == correct_ans.lower():
            print('you got it right!')
            self.score += 1
        else: 
            print('you got it wrong!')
        print(f"The correct answer is {correct_ans}")
        print(f'your score is {self.score} out of {self.q_number} ')
        print("\n")
