# LISTS HOLD THINGS

things = [1, 2.3, "my_str", [1, 2, 3], "Hello World", {"hats": 2000}]

for thing in things:
    print(thing)

# ADD SOMETHING TO YOUR LIST
things.append("ANOTHER THING")
print(things)

# REMOVE SOMETHING FROM YOUR LIST
things.remove([1, 2, 3])
print(things)
