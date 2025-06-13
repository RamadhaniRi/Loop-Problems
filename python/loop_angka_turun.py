number = int(input("Give me number:")) #meminta input angka ke pengguna

# Pakai For loop
print("==== For Looop ====")

for i in range(number, 0, -1): #disini i mewakili angka 
            #range(angka mulai, angka stop, dan angka dtwp jadi kayak mau ditambah atau dikurang)
            #disini kita mulai dari number, kemudian berakhir sebelum angka 0 dan stepnya -1
    print(i) 

print()

# Pakai While loop
print("==== While Looop ====")

while number > 0: #jadi selama number lebih dari 0 maka akan terus loop dan berhenti nanti di angka 1
    print(number)
    number -= 1 #jadi number akan berkurang terus seiring loop
