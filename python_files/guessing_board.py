class Board:
    def __init__(self, data):
        self.data = data
        self.total = len(self.data)
        self.user_guess = ""
        with open("../correctly_guessed_count") as count_file:
            self.guessed_count = int(count_file.read())

    def create_board(self, screen, count):
        # with open("../correctly_guessed_count") as count_file:
        #     count = int(count_file.read())
        self.user_guess = screen.textinput(title=f"{count}/{self.total} States Correct",
                                           prompt="What's another state name?")

    def increase_count(self):
        self.guessed_count += 1
        with open("../correctly_guessed_count", "w") as count_file:
            count_file.write(f"{self.guessed_count}")
