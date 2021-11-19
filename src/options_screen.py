# screen to choose from a list of options
class OptionsScreen(Screen):
    def __init__(self, title, options):
        self.title = title
        self.options = options # list of strings

    def display(self):
        print(self.to_string())
        # get input
        # validate input
        # if invalid, get input and validate again

    def get_choice(self):
        return self.choice

    def set_choice(self, n):
        self.choice = int(n)

    def to_string(self):
        full_text = ""
        for i, option in enumerate(self.options):
            full_text += str(i) + ". " + option + "\n"
        full_text += "\nPlease enter the number of the option you wish to take: "
        return full_text
