#Pembukuan part2
def daftar_pertanyaan_pembuatan_menu():
    respon_menu_barang = {}
    respon_menu_jasa = {}

    pengguna = input("Silahkan pilih jenis dagangan yang ingin dibuat (BARANG/JASA)").upper()
    if pengguna == "BARANG":
        while True:
            nama_barang = input("Masukkan nama barang yang ingin di daftarkan: ")
            harga_barang = input(f"Masukkan harga untuk {nama_barang}: ")
            respon_menu_barang[nama_barang] = harga_barang
            lanjut_pembuatan = input("Apakah ingin mendaftarkan barang lainnya? [Y/N]").upper()
            if lanjut_pembuatan == "N":
                break
    elif pengguna == "JASA":
        while True:
            nama_jasa = input("Masukkan nama barang yang ingin di daftarkan: ")
            harga_jasa = input(f"Masukkan harga untuk {nama_barang}: ")
            respon_menu_jasa[nama_jasa] = harga_jasa
            lanjut_pembuatan = input("Apakah ingin mendaftarkan barang lainnya? [Y/N]").upper()
            if lanjut_pembuatan == "N":
                break

daftar_pertanyaan_pembuatan_menu()
