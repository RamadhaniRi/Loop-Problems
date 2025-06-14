# kita akan membuat persegi
# caranya kita pakai for loop
# kemudian baris dan kolom jumlahnya harus sama
# disini kita pakai 5 kolom dan 5 baris

print("for loop")

for i in range(5):
    for i in range(5):
        print(".", end=" ")
    print()

print()
print()


print("while loop")

j = 0
while j < 5:
    j += 1
    i = 0
    while i < 5:
        print("#", end=" ")
        i += 1
    print()