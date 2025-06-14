# nested loop adalah loop didalam loop
# Untuk membuat nested loop, buat dulu dari Inner loop (loop di dalam)
# baru buat outer loop

# kita akan buat matriks seperti ini
# 11, 12, 13, 14
# 21, 22, 23, 24
# 31, 32, 33, 34

# angka akan pake outer loop
# huruf akan pake inner loop

# outer loop untuk baris
# inner loop untuk kolom



for j in range(1, 4): #outer loop untuk membuat angka di dalam dari 1-3 dan membuat 3 baris
    for i in range(1, 5): #inner loop untuk membuat angka kedua dari 1-4 dan membuat 4 kolom
        print(f"{j}{i}",end=" ") #print j dan i, kemudian end=" " untuk jarak
    print() # print kosong untuk baris baru