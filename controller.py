from questions import question_data

class Player():
    def __init__(self, player_name) -> None:
        self.name = player_name
        self.score = 0
        self.max_score = 0
        self.questions = question_data
    
    def check_answer(self, answer, question):
        self.max_score += question.points
        if question.answer == answer:
            self.score += question.points
            return True
        else:
            self.score -= 1
            return False
        
    def next_question(self, question, extra_points=0):
        if len(self.questions) == 0:
            return False
        q = self.questions.pop(0)
        question.question = q["text"]
        question.answer = q["answer"]
        question.points += extra_points
        return question
