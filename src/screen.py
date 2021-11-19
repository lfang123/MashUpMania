class Screen:
    # default constructor
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def display(self):
        print(self.get_title())
