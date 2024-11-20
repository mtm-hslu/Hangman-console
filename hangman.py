import os

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]

def hangman(word):
    word = word.upper()
    guessed = "_" * len(word)
    guessed_correctly = set()
    guessed_incorrectly = set()
    messages = []
    tries = 6
    print("Welcome to Hangman!")

    while tries > 0 and "_" in guessed:
        os.system("clear")
        print(display_hangman(tries))
        print(f"Word: {' '.join(guessed)}")
        print(f"Incorrect guesses: {', '.join(sorted(guessed_incorrectly))}")
        for message in messages:
            print(message)
        guess = input("Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            messages.append(f"Invalid input '{guess}'. Please guess a single letter.")
            continue

        if guess in guessed_correctly or guess in guessed_incorrectly:
            messages.append(f"You've already guessed '{guess}'!")
            continue

        if guess in word:
            guessed_correctly.add(guess)
            guessed = "".join([char if char in guessed_correctly else "_" for char in word])
            messages.append(f"Good guess! {guess} is in the word.")
        else:
            guessed_incorrectly.add(guess)
            tries -= 1
            messages.append(f"Wrong guess! {guess} is not in the word.")

    os.system("clear")
    if "_" not in guessed:
        print(display_hangman(tries))
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    word_to_guess = input("Enter the word to guess: ").strip()
    hangman(word_to_guess)
