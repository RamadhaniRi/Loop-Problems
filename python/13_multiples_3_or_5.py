i = 1
num = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        num += i
    i += 1
print(num)