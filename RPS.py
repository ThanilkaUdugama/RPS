# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def calculate_shows(stream, lookfor):
    count = 0
    for i in range(len(lookfor), len(stream) + 1):
        word = "".join(stream[i - len(lookfor): i])

        if word == lookfor:
            count += 1

    return count


def choose_option(stream, lookup_len):
    last_steps = "".join(stream[-(lookup_len):])
    counter_actions = {"R": "P", "P": "S", "S": "R"}

    guesses = ["R", "P", "S"]
    guess_data = ['', -1]
    for guess in guesses:
        result = calculate_shows(stream, last_steps + guess)

        if result > guess_data[1]:
            guess_data[1] = result
            guess_data[0] = guess

    return counter_actions[guess_data[0]]


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    lookback = 4

    if len(opponent_history) > 2 and len(opponent_history) <= lookback:
        guess = opponent_history[-2]
    else:
        guess = choose_option(opponent_history, lookback)

    return guess
