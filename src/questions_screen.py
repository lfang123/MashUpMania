# screen to enter one or more values
class QuestionsScreen(Screen):
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions # list of strings

    def ask_question(self, question):
        print(question)
        # get input, may not need ask_question function

    def display(self):
        for question in self.questions:
            answer = self.ask_question(question)
            self.answers.append(answer)
