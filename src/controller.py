# Controller is CLI for now. GUI to come later
class Controller:
    def __init__(self, screens):
        self.screens = {}
        for screen in screens:
            self.screens[screen.get_title()] = screen

    def start(self):
        self.screens["StartScreen"].display()
