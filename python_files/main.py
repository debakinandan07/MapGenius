import time
import turtle
from turtle import Screen
from guessing_board import Board
from write_state_name_on_map import StateOnMap
import pandas as pd

# def get_coordinates(x , y):
#     print(x , y)
# turtle.onscreenclick(get_coordinates)

name = ""
x_cor = 0
y_cor = 0

screen = Screen()
screen.tracer(0)
image = "../blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("../csv_files/50_states.csv")
states = data.state

board = Board(data)
state_name = StateOnMap()

all_guessed = False
guessed_state_list = []
remaining_states_to_guess = []

"""this will set position for the state and pass as arguments to the 
    method in Board class for the turtle to write"""
def set_position_for_state(row):
    global name, x_cor, y_cor
    name = row.iloc[0]["state"]
    x_cor = row.iloc[0]["x"]
    y_cor = row.iloc[0]["y"]
    state_name.show_state_name(name, x_cor, y_cor)


"""this appends all the states that are already guessed and are there in the guessed_file and 
    then shows them on the map when the user revisit for the guessing"""
try:
    guessed_states = pd.read_csv("../csv_files/guessed_states.csv")
    g_states = guessed_states["0"]
    for g_state in g_states:
        guessed_state_list.append(g_state)
        for state in states:
            if state == g_state:
                guessed_row = data[states == state]
                set_position_for_state(guessed_row)
except (KeyError, FileNotFoundError):
    pass

while not all_guessed:
    time.sleep(0.1)
    screen.update()
    board.create_board(screen, board.guessed_count)
    guess = board.user_guess.title()

    for state in states:
        """this helps to exit the game when user wishes to do so"""
        if guess is None or guess == "Save":
            remaining_states_to_guess = [state for state in states if state not in guessed_state_list]
            rd = pd.DataFrame(remaining_states_to_guess)
            rd.to_csv("../csv_files/remaining_states_to_guess.csv")
            gd = pd.DataFrame(guessed_state_list)
            gd.to_csv("../csv_files/guessed_states.csv")
            turtle.bye()
            all_guessed = True

        """this checks if user guessed it correctly"""
        if guess == state and guess not in guessed_state_list:
            correct_state_row = data[data.state == guess]
            set_position_for_state(correct_state_row)
            board.increase_count()
            guessed_state_list.append(guess)

        """this checks if the user guessed all the states correctly"""
        if board.guessed_count == board.total:
            all_guessed = True
            print("Congrats Champ! You guessed all of them correctly.")

screen.mainloop()
