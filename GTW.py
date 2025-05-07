import random

words = ["turtle", "tiger", "zebra", "mouse", "horse", "rabbit"]
secret_word = random.choice(words)
guesses_left = 10
dashes = "-" * len(secret_word)

print(dashes)
print("10 Incorrect guess left!")


def get_guess():
    while True:
        guess = input("Guess: ")

        if not guess.islower():
            print("Your guess must be a lowercase letter!")

        elif len(guess) > 1:
            print("Your guess must have exactly one character!")
        else:
            return guess


def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result


while guesses_left > 0:
    guess = get_guess()

    if guess in secret_word:
        print("That letter is in the word!")
        dashes = update_dashes(secret_word, dashes, guess)
        print(dashes)
        print(f"{guesses_left} Incorrect guesses left.")

    else:
        guesses_left -= 1
        print("That letter is not in the word.")
        print(f"{guesses_left} Incorrect guesses left.")

    if guesses_left == 0:
        print(f"you lose the secret word was {secret_word}.")

    if "-"  not in dashes:
        print(f"Congratulations, You guesss the secret word: {secret_word} to win the game!")
        break
