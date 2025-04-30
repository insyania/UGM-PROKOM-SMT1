def penjumlahan (x,y):
    return x + y
def pengurangan (x,y):
    return x - y
def perkalian (x,y):
    return x * y
def pembagian (x,y):
    if y == 0:
        return ("Tidak dapat menghitung hasil")
    else:
        return(x / y)
def pangkat (x,y):
    return(x ** y)
def akar_kuadrat (x):
    if x < 0:
        return("Tidak ada hasil")
    else:
        return (x ** 0.5 )

def nama (mahasiswa):
    print("Nama: ", mahasiswa)
nama("Scarrlet Johanson")

def nim (mhs):
    print("NIM: ", mhs)
nim("30/100000/MK/90000")

while True:
    print("1. Menu penjumlahan")
    print("2. Menu pengurangan")
    print("3. Menu perkalian")
    print("4. Menu pembagian")
    print("5. Menu perpangkatan")
    print("6. Menu akar kuadrat")
    print("7. Keluar")
    
    operasi = int(input("Masukkan pilihan: "))

    if operasi == 7:
        break
    if operasi >=1 and operasi <= 6:
        x = float(input("Masukkan angka pertama yang diinginkan: "))
        y = float(input("Masukkan angka kedua yang diinginkan: "))
        if operasi == 1:
            result = penjumlahan (x,y)
        elif operasi == 2:
            result = pengurangan (x,y)
        elif operasi == 3:
            result = perkalian (x,y)
        elif operasi == 4:
            result = pembagian (x,y)
        elif operasi == 5:
            result = pangkat (x,y)
        else:
            result = akar_kuadrat (x)
        print("Hasilnya: ", result)
    else:
            print("Masukkan nilai yang valid")
    break        
    
    





