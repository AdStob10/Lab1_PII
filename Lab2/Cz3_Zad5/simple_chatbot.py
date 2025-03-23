class SimpleChatbot():

    def __init__(self, questions: list[str]):
        self.questions = questions
        self.question_count = len(questions)
        self.question_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.question_counter < self.question_count:
            question = self.questions[self.question_counter]
            self.question_counter += 1
            return question
        else:
            raise StopIteration
