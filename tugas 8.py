random_number = 8
while True :
    bingo = int(input('Masukkan angka pilihan: '))
    if bingo == random_number :
        print('Tebakan benar!')
        break
    elif bingo > random_number :
        print('Terlalu besar!')
    else :
        print('Telalu kecil!')