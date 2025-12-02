import random

HANGMAN_PICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

WORDS = {
    "easy": ["apple", "ball", "chair", "school", "laptop", "mouse"],
    "medium": ["python", "college", "hangman", "project", "network"],
    "hard": ["algorithm", "asynchronous", "microscope", "javascript"]
}

def choose_difficulty():
    while True:
        level = input("Choose difficulty (easy / medium / hard): ").lower()
        if level in WORDS:
            return level
        print("Invalid choice! Try again.")

def hangman_game():
    level = choose_difficulty()
    word = random.choice(WORDS[level])
    guessed = []
    wrong = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("\n HANGMAN GAME START\n")

    while wrong < max_wrong:
        print(HANGMAN_PICS[wrong])

        display = " ".join([letter if letter in guessed else "_" for letter in word])
        print("Word:", display)
        print("Guessed:", guessed)

        if "_" not in display:
            print("\n You WON! The word was:", word)
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Enter a single valid letter!")
            continue

        if guess in guessed:
            print(" You already guessed this letter.")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print(" Wrong guess!")
        else:
            print(" Correct!")

    print(HANGMAN_PICS[-1])
    print(" GAME OVER! The word was:", word)

hangman_game()