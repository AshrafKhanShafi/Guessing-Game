#Guessing game 
message = '''WELCOME TO THE GUESSING GAME! 
TRY TO MATCH THE NUMBER BETWEEN 1 TO 100'''
print(message)

import random
def guessing_game():
    guessing_the_number = random.randint(1, 100)
    low_count = 0
    high_count = 0
    guess_count = 0
    while True:
        try:
            user_input = int(input("\n" + "Enter your guess: "))
            guess_count += 1
            if user_input > guessing_the_number:
                high_count += 1
                print("Too high")
            elif user_input < guessing_the_number:
                low_count += 1
                print("Too low")
            else:
                print("\n" + "CONGRATULATION! You have guessed the number and tried {} times.".format(guess_count - 1))
                print("\n" + "You have guessed {} high and {} low count.".format(high_count, low_count) + "\n")
                break
        except Exception as e:
            print("Invalid input or something error: {}".format(e))

guessing_game()
        