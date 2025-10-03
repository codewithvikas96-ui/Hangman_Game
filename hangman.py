import random
from words import words

hangman_art = {
                0 : ("   ",
                     "   ",
                     "   "),
                1 : (" o ",
                     "   ",
                     "   "),
                2 : (" o ",
                     " | ",
                     "   "),
                3 : (" o ",
                     "/| ",
                     "   "),
                4 : (" o ",
                     "/|\\",
                     "   "),
                5 : (" o ",
                     "/|\\",
                     "/  "),
                6 : (" o ",
                     "/|\\",
                     "/ \\")
}


def display_man(wrong_guesses):
    print("-" * 60)
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-" * 60)


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def play_game():
    answer = random.choice(words)
    wrong_guesses = 0
    hint = ['-'] * len(answer)
    guessed_letters = set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        
        print()

        guess = input("Enter a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        print(f"Lives left: {6 - wrong_guesses}")


        if '-' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            break
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            break
        


def main():
    while True:
        play_game()
        play_again = input("Play again(y/n): ").lower()

        if play_again == 'n':
            print("Thanks for playing 👋")
            break

    

if __name__ == '__main__':
    main()