# Pakai For loop
print("==== For Loop ====")

for _ in iter(int, 1):  # infinite loop dengan for
    print("Hi")
    ask_user = input("shall we continue? ")

    if ask_user == "no":
        break





# Pakai While loop
print("==== While Loop ====")
while True:
    print("Hi")
    ask_user = input("shall we continue? ")

    if ask_user == "no":
        break