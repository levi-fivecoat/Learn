# STEP 1 : DEFINE A FUNCTION THAT  PRINTS A NAME
# remember

def print_name(name):
    print(name)


def get_name():
    name = input("WHAT IS YOUR NAME?: ")
    return name


def main():
    name = get_name()
    print_name(name)


# CALL THE FUNCTION
main()
