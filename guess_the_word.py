# Ryder Brown
# CIS256 Fall 2024
# EX 4

import random

def select_word():
    words = ["python", "programming", "testing", "debugging", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    word = select_word()
    guessed_letters = set()
    attempts = 8
    print("Welcome to the Word Guessing Game!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word:", word)
                return
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Incorrect guess.")
    
    print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    play_game()