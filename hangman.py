import random
def hangman():
    words = ["python", "hangman", "program", "intern", "codealpha"]
    word = random.choice(words) 
    guessed_word = ["_"] * len(word) 
    attempts = 6  
    guessed_letters = [] 
    print("🎮 Welcome to Hangman Game!")
    print("Guess the word: ", " ".join(guessed_word))
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(guessed_letters))
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n😢 Game Over! The word was:", word)
hangman()
