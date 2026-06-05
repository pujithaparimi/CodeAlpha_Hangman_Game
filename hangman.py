import random

# List of words
words = [
    "python",
    "coding",
    "computer",
    "developer",
    "programming"
]

# Random word selection
secret_word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("      HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print()

# Game Loop
while wrong_guesses < max_wrong_guesses:

    # Display current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        break

    # Show guessed letters
    print("Guessed Letters:", guessed_letters)

    # User input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1:
        print("❌ Enter only ONE letter.")
        continue

    if not guess.isalpha():
        print("❌ Enter only alphabets.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check letter
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        remaining = max_wrong_guesses - wrong_guesses

        print("❌ Wrong Guess!")
        print("Remaining Chances:", remaining)

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)