daftar = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

genap = 0
ganjil = 0
for row in daftar:
    for col in row:
        if col % 2 == 0:
            genap += 1
        else:
            ganjil += 1

print("Jumlah elemen genap:", genap)
print('Jumlah elemen ganjil:', ganjil)