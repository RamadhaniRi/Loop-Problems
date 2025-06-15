print("Math Game!")
number = int(input("Name your multiples: "))

count = 0
true_count = 0
false_count = 0

while count < 10:
    count = count + 1
    total = int(input(f"{count} x {number} = "))
    if total == count * number:
      print("Awesome!")
      true_count += 1
    else:
      print(f"Nope. The answer is {count * number}")
      false_count += 1

print("==========")
print(f"You got {true_count} correct and {false_count} incorrect.")