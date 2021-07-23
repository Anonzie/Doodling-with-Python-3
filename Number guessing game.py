import random
# Importing the random module

print('Welcome to my number guessing game!')
print("The Rules:\nYou get five guesses.\nThat's it ;), Best of luck!")

ran_num = random.randint(1, 10)
# Creates the random number that'll be guessed.

for num_of_guesses in range(1, 6):
    guess = int(input("Please input your guess: "))

    if guess == ran_num:
        print(f"Congratulations, you've guessed the number, {ran_num}. \nIt took you {num_of_guesses} guesses to guess the number."), exit()
    #If our guess is equal to the random number, then it prints the above message, and ends the game

    elif guess > ran_num:
        guesses_left = 5 - num_of_guesses, print(f"Sorry, {guess} is larger than the random number.\nCurrently, you are on guess {num_of_guesses}, you have {guesses_left} guesses left.")
    #If our guess is larger than the random number, it prints the above message, and will continue looping the input until we've reached five guesses. 

    elif guess < ran_num:
        guesses_left = 5 - num_of_guesses, print(f"Sorry, {guess} is smaller than the random number.\nCurrently, you are on guess {num_of_guesses}, you have {guesses_left} guesses left.")
    #If our guess is smaller than the random number, it prints the above message, and continues the input until we reach 5 guesses.

    else:
        print("Sorry, the program cannot understand your input.")
    #If the user inputs something that isn't an integer, it will print the above message and explain to the user that their input wasn't understood.