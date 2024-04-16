import random
from words import wordList
from stages import displayHangman

def getWord():
    word = random.choice(wordList)
    return word.upper()

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Let's play Hangman!")
    print(displayHangman(tries))
    print(wordCompletion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print("Good job ", guess, "is in the word!")
                guessedLetters.append(guess)
                word_as_list = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                wordCompletion = "".join(word_as_list)
                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessedWords.append(guess)
        else:
            print("Not a valid guess.")
        print(displayHangman(tries))
        print(wordCompletion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word! you win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!...")

def main():
    word = getWord()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = getWord()
        play(word)

if __name__ == "__main__":
    main()