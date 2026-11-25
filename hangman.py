import random

word_bank = ["mango", "planet", "python", "garden", "rocket"]
secret = random.choice(word_bank)
guessed = set()
mistakes = 0
limit = 6

print("LETTER QUEST — Hangman")

while mistakes < limit:
    shown = " ".join(ch if ch in guessed else "_" for ch in secret)
    print(f"\nWord: {shown}   Misses left: {limit - mistakes}")

    if "_" not in shown:
        print("You solved it:", secret)
        break

    letter = input("Enter one letter: ").strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Type a single letter.")
        continue

    if letter in guessed:
        print("That letter was already tried.")
        continue

    guessed.add(letter)

    if letter not in secret:
        mistakes += 1
        print("No match.")
else:
    print("Out of tries! The word was:", secret)