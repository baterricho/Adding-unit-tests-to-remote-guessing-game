def check_guess(secret, guess):
    if guess == secret:
        return "Correct!"
    elif guess < secret:
        return "Too low!"
    else:
        return "Too high!"

def play_guess_game(secret=5, input_func=input, print_func=print):
    print_func("Welcome to the guessing game!")
    guess = int(input_func("Guess a number: "))
    result = check_guess(secret, guess)
    print_func(result)
    return result
