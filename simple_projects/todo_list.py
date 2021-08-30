def add_something_to_do(existing_things_to_do):
    thing_to_do = input("Type something you want to do: ")
    existing_things_to_do.append(thing_to_do)
    return existing_things_to_do


def main():
    things_to_do = [
        "wake up",
        "eat bfast",
        "ride bike",
        "write code",
        "step 5: profit"
    ]
    number_added = 0
    number_of_things = int(input("ENTER NUMBER OF THINGS YOU WANT TO ADD: "))
    while number_added < number_of_things:
        things_to_do = add_something_to_do(things_to_do)
        number_added += 1
    for num, activity in enumerate(things_to_do):
        print(num + 1, activity)


main()
