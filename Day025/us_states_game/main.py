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
    if answer_state == "Exit":
        # before exiting the game, collect all the states not correctly guessed,
        # and then display them on the screen in red text
        missing_states = []
        for state in all_states:
            if state not in states_guessed:
                missing_states.append(state)
        print(missing_states)
        for ms in missing_states:
            missing_state = states_data[states_data.state == ms]
            state_writer.pencolor('red')
            state_writer.goto(x=int(missing_state.x), y=int(missing_state.y))
            state_writer.write(arg=ms.title(), align='center',
                               font=('Arial', 13, 'normal'))
        # turn missing states into a csv file
        new_data = pandas.DateFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    elif answer_state in all_states:
        # write the correct guesses onto the map
        print(int(found_state.x), int(found_state.y))
        state_writer.goto(x=int(found_state.x), y=int(found_state.y))
        state_writer.write(arg=answer_state.title(),
                           align='center', font=('Arial', 13, 'normal'))
        # record the correct guesses in a list
        states_guessed.append(answer_state)
        # create a new output dataframe, first as a python dict, then convert to dataframe, then to csv
        PROMPT = "Guess another state name."
    else:
        PROMPT = "Try again!"

    # get the user answer and convert to correct case for searching
    answer_state = screen.textinput(title=f'{len(states_guessed)}/50 States Correct',
                                    prompt=PROMPT).title()


# keep track of the score

screen.exitonclick()

