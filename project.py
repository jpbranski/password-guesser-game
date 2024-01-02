# TODO
# ✔ Start the game
# ✔ Get user's name
# ✔ Get desired difficulty
# ✔ Get words
# ✔ Set what the password is
# ✔ Display guessing board
# ✔ Get user guesses
# ✔ Replace guesses with punctuation characters
# ✔ Calculate score on correct guess


import random
import string
import sys
import textwrap


def main():
    while True:
        username, difficulty = get_user_data()
        file_name = get_file_name(difficulty)
        wlist = get_word_list(file_name)
        pword = random.choice(wlist).upper()
        game_board = generate_gboard(wlist)
        total_guesses = playgame(game_board, pword)
        print(game_win(username, difficulty, total_guesses))
        playing = play_again(input("Play again? (Y/n): "))
        if playing == False:
            break


def get_user_data():
    usr = ""
    diff = 0

    while True:
        try:
            usr = input("Username: ")
            if not 3 < len(usr) < 17:
                raise ValueError
            else:
                break
        except ValueError:
            print("Username must be between 4-16 characters.")

    while True:
        try:
            diff = int(input("Difficulty (1-5): "))
            if not 0 < diff < 6:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid difficulty.")

    return usr, diff


def get_file_name(difficulty):
    match difficulty:
        case 1:
            return "words1.txt"
        case 2:
            return "words2.txt"
        case 3:
            return "words3.txt"
        case 4:
            return "words4.txt"
        case 5:
            return "words5.txt"
        case _:
            sys.exit("Fatal error: please try again later.")


def get_word_list(f):
    word_list = open_word_list(f)
    return random.sample(word_list, 9)


def open_word_list(txt):
    with open(txt) as file:
        list = file.readlines()
        list = list[0].rstrip().split(', ')
        return list


def generate_gboard(l):
    gboard = []
    fill_amnt = random.sample(range(15,30), 10)

    for i in range(len(fill_amnt)):
        gboard.append(''.join(random.choice(string.punctuation) for j in range(fill_amnt[i])))
        if i < 9:
            gboard.append(l[i].upper())

    gboard = ''.join(gboard)

    return "\n".join(textwrap.wrap(gboard, 20))


def playgame(gb, p):
    guesses = 1

    print("\nFind the password!\n")
    while True:
        print(f"{gb}\n")
        guess = input(f"Guess {guesses}: ").upper()
        if len(guess) == len(p):
            if guess == p:
                return guesses
            else:
                gb = gb.replace("\n", "")
                similar_letters = 0
                guesses = guesses + 1
                if gb.find(guess) > 0:
                    gb = gb.replace(guess, ''.join(random.choice(string.punctuation) for i in range(len(guess))))
                    gb = "\n".join(textwrap.wrap(gb, 20))
                for j in range(len(p)):
                    if guess[j] == p[j]:
                        similar_letters = similar_letters + 1

            print(f"{similar_letters} Similarities.\n")


def game_win(u, d, g):
    new_score = (5000 - ((g - 1) * 475)) * d
    return(f"{u} has beaten difficulty {d} with a score of {new_score}!")

def play_again(response):
    if response.lower() == "y":
        return True
    elif response.lower() == "n":
        return False


if __name__ == "__main__":
    main()