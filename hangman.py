import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

# Select a random word from the list
word = random.choice(word_list)

# Initialize the guess string with underscores for each letter in the word
guess = ["_" for letter in word]

# Number of incorrect guesses allowed
max_guesses = 6

# List to store the letters already guessed
guessed_letters = []

# Main game loop
while max_guesses > 0:
    # Print the current guess string and the letters already guessed
    print(" ".join(guess))
    print("Letters guessed: ", " ".join(guessed_letters))

    # Get a letter guess from the user
    letter = input("Guess a letter: ")

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add the letter to the guessed letters list
    guessed_letters.append(letter)

    # Check if the letter is in the word
    if letter in word:
        # Update the guess string with the new letter
        for i in range(len(word)):
            if word[i] == letter:
                guess[i] = letter

        # Check if the player has won
        if "_" not in guess:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        # Decrement the number of remaining guesses
        max_guesses -= 1
        print("Incorrect guess. You have", max_guesses, "guesses remaining.")

# Check if the player has lost
if max_guesses == 0:
    print("Sorry, you ran out of guesses. The word was:", word)
