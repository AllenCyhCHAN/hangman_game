import requests

"""
max no of tiral = 
get a word > display the number of letter in it 
ask user for first input 
check if the letter is in the answer 
if yes,
    display the letter and the position 
if no,
    tries -= 1 
    hangman show one more component


ask if user wanna play again

"""


def get_word():
    response = requests.get("https://random-words-api.vercel.app/word")
    data = response.json()
    data = data[0]["word"]
    if len(data) > 6:
        return get_word()
    else:
        return data.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8

    print("Lets play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        # guessing the letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed_letters", guess)

            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        # guessing the word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word")
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print("guessed letter: ", guessed_letters)
        print("guessed words: ", guessed_words)
        print("remaining tries", tries)
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word, you win!")
    else:
        print(
            "Sorry, you ran out of tries, the word was " + word + ". Maybe next time!"
        )


def display_hangman(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /|\\
                          |
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /|\\
                   -
                """,
        # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    game_status = True
    while game_status:
        user_input = input("Play Again? (Y/N) ").upper()
        if user_input == "Y":
            game_status = True
        else:
            game_status == False
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
