def input_word():
    return input("For the HOST!\nEnter a word: ").lower()

def letter_guess():
    return input("For the PLAYER!\nEnter a Guess a character: ").lower()

def show_game(word,correct_chars):
    for char in word:
        if char in correct_chars:
            print(char.upper(),end="")
        else:
            print("_ ",end="")
    print()
def main():
    word = input_word()
    print("\n"*50)  # Clear the screen for the player
    guessed_chars=[]
    correct_chars=[]
    lives=10

    while lives>0 and len(correct_chars)<len(word):
        show_game(word,correct_chars)
        print(f"Lives left: {lives}")
        print(f"Guessed chars: {guessed_chars}")
        guess = letter_guess()
        if guess in guessed_chars:
            print("You already guessed that letter!")
            continue
        if guess in word:
            print("Correct!")
            correct_chars.append(guess)
        if guess not in word:
            print("Wrong!")
            lives-=1
        guessed_chars.append(guess)

    if lives>0:
        print("You won!")
    else:
        print("You lost!")
    print(f"The word was: {word}")





    pass

if __name__ == "__main__":
    main()