PS 43 - Hangman Game (Python 3)

import random
import sys

WORDS = ["python", "hangman", "program", "keyboard", "variable",
         "function", "string", "random", "console", "developer"]
MAX_WRONG = 6


def choose_word(test_mode):
    """Return the secret word (fixed in test mode, random otherwise)."""
    return "python" if test_mode else random.choice(WORDS)


def masked(word, guessed):
    """Show the word with unguessed letters as underscores."""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def is_valid(text):
    """A valid guess is exactly one alphabetic character."""
    return len(text) == 1 and text.isalpha()


def play(word):
    guessed = set()   
    wrong = 0

    print("Welcome to Hangman! You have 6 wrong guesses.")
    print("Word:", masked(word, guessed))

    while wrong < MAX_WRONG and not all(ch in guessed for ch in word):
        try:
            guess = input("Guess a letter: ").strip().lower()
        except EOFError:
            print("\nNo more input. Game ended.")
            return

        if not is_valid(guess):
            print("Invalid input. Enter a single letter.")
            continue

        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue  # repeated letter: no attempt lost

        guessed.add(guess)
        if guess in word:
            print(f"{guess}: Correct")
        else:
            wrong += 1
            print(f"{guess}: Wrong guess ({wrong}/{MAX_WRONG})")
        print("Word:", masked(word, guessed))

    if all(ch in guessed for ch in word):
        print(f"You won! The word was {word}.")
        print(f"Wrong guesses: {wrong}/{MAX_WRONG}")
    else:
        print(f"Game Over! The word was {word}.")


def main():
    test_mode = "--test" in sys.argv
    play(choose_word(test_mode))


if __name__ == "__main__":
    main()
