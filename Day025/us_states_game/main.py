import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv('50_states.csv')
state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()

# get the user answer and convert to correct case for searching
answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name?").lower().capitalize()

# check if the guess is among the 50 states
found_state = states_data[states_data.state == answer_state]
if len(found_state) != 0:
    # write the correct guesses onto the map
    print(found_state.values[0][1], found_state.values[0][2])
    state_writer.goto(x=found_state.values[0][1], y=found_state.values[0][2])
    state_writer.write(arg=found_state.values[0][0], align='center', font=('Arial', 16, 'normal'))

# use a loop to allow the user to keep guessing

# record the correct guesses in a list

# keep track of the score

screen.exitonclick()

