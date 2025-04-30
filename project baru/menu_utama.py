import pembukuan_UMKM
#import pendaftaran_UMKM

def menu_utama_sahabat_usaha():
    while True:
        print("========== SAHABAT USAHA ==========")
        print("[1] Level Up Your Enterpreunurship Skills !!!")
        print("[2] Create Your Own Shop !!!")
        print("[3] Manage your shop and become a successful entrepreneur!!!")
        print("[4] Exit")
        pilihan_pengguna = int(input("Masukkan fitur yang ingin diakses: "))
        if pilihan_pengguna == 1:
            print()
        elif pilihan_pengguna == 2:
            pendaftaran_UMKM.menu_utama_registrasi_umkm()
        elif pilihan_pengguna == 3:
            pembukuan_UMKM.menu_utama_fitur_pembukuan()
        elif pilihan_pengguna == 4:
            exit()
        else:
            print("Pilihan pengguna tidak valid")

menu_utama_sahabat_usaha()