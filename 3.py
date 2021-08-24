def first():
    X = input('enter 1st number')
    Y = input('enter 2nd number')
    z = int(X) + int(Y)
    print (z)

    is_hot = True
    is_cold = False

    if is_hot:
        print("its's a hot day")
        print ("drink plenty of water")
    elif is_cold:
        print("it's a cold day")
        print("wear warm clothes")
    else:
        print("it's a lovely day")

    print ("enjoy yur day")


def second():
    name = ""
    if len(name) < 3:
        print("name must be at least 3 characters long")
    elif len(name) > 50:
        print("name must be maximum of 50 characters")
    else:
        print("name looks good")


def third():
    weight = int(input('weight'))
    unit = input('(L)bs or(k)g:')
    if unit.upper() == "L":
        converted = weight * 0.45
        print("you are " + str(converted) + " kilos")
    else:
        converted = weight / 0.45
        print("you are " + str(converted) + " pounds")


def fourth():
    print("Guess a number until you get it right or 3 tries are up.")
    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input('guess: '))
        guess_count += 1
        if guess == secret_number:
            print('you won!')
            break
        else:
            print("Nope.")
    else:
        print("sorry, you have failed, loser.")


fourth()
