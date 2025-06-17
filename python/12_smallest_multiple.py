i = 0
while True:
    i += 1
    j = 1
    count = 0
    while j <= 20:
        if i % j == 0:
            print("pass")
            count += 1
        j += 1
        
    if count == 20:
        print(i, "thats it")
        break
