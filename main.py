import country

country_detail = country.random_country()

class YouWonException(Exception):
    pass

def get_random_country_name():
    return country_detail['name'].lower()


def print_rules():
    print("Welcome to guess my country? ")
    print("#############################")
    print("Rules: ")
    print("#############################")
    print("Rule #1: You will get 5 chances to guess")
    print("Rule #2: You can guess a charater and I will \n tell you if it exists in the name or not and its position")
    print("Rule #3: You can enter the whole word any point you want.")
    print("#############################")
    print("Let's start the game! \m/")

def print_with_guess(name, char_guess):
    name_copy = ['_']*len(name)
    for ch in char_guess:
        for i,n in enumerate(name):
            if ch.upper() == n:
                name_copy[i] = ch

    print(' '.join(name_copy))
    if ''.join(name_copy).count('_') == 0:
        raise YouWonException('Yay!! You Won.')

def provide_hint(max_tries, try_count):
    if max_tries - try_count <= max_tries//2:
        print("HINT: Capital of country is : ", country_detail['capital'])
    if max_tries - try_count == 1:
        print("HINT: This country is in ", country_detail['region'], ' region')

def print_correct_answer(name):
    print(" Correct answer is : ", ' '.join(name))

def start_hangman(country_detail):
    try_count = 0
    max_tries = 5
    char_guess = list()
    name = list(country_detail['name'].upper())
    print("You country name has "+str(len(name))+' characters')
    print_with_guess(name, char_guess)
    while try_count < max_tries:
        print("Remaining Try Count(s) : ", (max_tries - try_count))
        print("#############################")
        provide_hint(max_tries, try_count)
        guess = input("Enter your guess : ").strip()
        if len(guess) > 1:
            if guess == ''.join(name):
                print("Yay! you won")
                return
            else:
                try_count+=1
        else:
            try:
                if name.index(guess) > -1:
                    char_guess.append(guess)
                    print_with_guess(name, char_guess)
            except ValueError as err:
                print("Nope! Try again!")
                try_count+=1
                print_with_guess(name, char_guess)
            except YouWonException as ywe:
                print("Yay! You won!!!!")
                return
    print_correct_answer(name)
def play():
    print_rules()
    start_hangman(country_detail)




play()