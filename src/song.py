class Song:
    # default constructor
    def __init__(self):
        self.name = ""

    # constructor
    def __int__(self, name):
        self.name = name

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name
