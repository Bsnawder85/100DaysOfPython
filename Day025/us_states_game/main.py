import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_guessed = []
states_data = pandas.read_csv('50_states.csv')
state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()
all_states = states_data.state.to_list()

PROMPT = "Guess a state name."

# get the first user answer and convert to correct case for searching
answer_state = screen.textinput(title=f'{len(states_guessed)}/50 States Correct',
                                prompt=PROMPT).title()

# use a loop to allow the user to keep guessing
while len(states_guessed) <= 50:
    # check if the guess is among the 50 states
    found_state = states_data[states_data.state == answer_state]
    if found_state == "Exit":
        break
    elif answer_state in all_states:
        # write the correct guesses onto the map
        print(int(found_state.x), int(found_state.y))
        state_writer.goto(x=int(found_state.x), y=int(found_state.y))
        state_writer.write(arg=answer_state.title(),
                           align='center', font=('Arial', 16, 'normal'))
        # record the correct guesses in a list
        states_guessed.append(answer_state)
        PROMPT = "Guess another state name."
    else:
        PROMPT = "Try again!"

    # get the user answer and convert to correct case for searching
    answer_state = screen.textinput(title=f'{len(states_guessed)}/50 States Correct',
                                    prompt=PROMPT).title()


# keep track of the score

screen.exitonclick()

