stuffs = {
    "1": ("Pensil", 2000),
    "2": ("Buku", 15000),
    "3": ("Penghapus", 5000),
    "4": ("Rautan", 3000),
}

def menentukan_kode(kode):
    return kode in stuffs

def main():
    print("Selamat datang di Toko Kami!")
    jenis_barang = int(input("Berapa jenis barang yang ingin Anda beli? "))

    belanja = []
    total_harga = 0

    for _ in range(jenis_barang):
        while True:
            kode_barang = input("Masukkan kode barang: ")
            if menentukan_kode(kode_barang):
                break
            else:
                print("Kode barang salah, silakan coba lagi.")

        nama_barang, harga = stuffs[kode_barang]
        jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))
        subtotal = harga * jumlah

        belanja.append((nama_barang, jumlah, harga, subtotal))
        total_harga += subtotal

    # Diskon jika total harga lebih dari 50000
    diskon = 0
    if total_harga > 50000:
        diskon = total_harga * 0.1  # diskon 10%

    total_harga_setelah_diskon = total_harga - diskon

    # Mencetak struk belanja
    print("\n--- Struk Belanja ---")
    for item in belanja:
        print(f"{item[0]} x {item[1]}: {item[3]} IDR")

    print(f"Total Harga: {total_harga} IDR")
    if diskon > 0:
        print(f"Diskon: {diskon} IDR")
    print(f"Total Setelah Diskon: {total_harga_setelah_diskon} IDR")

if __name__ == "__main__":
    main()
