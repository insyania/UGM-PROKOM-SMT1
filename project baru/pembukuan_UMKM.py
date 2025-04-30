import menu_utama
menu_barang = []
menu_jasa = []
pembukuan_bulanan = {}

def pembuatan_menu_barang_dan_jasa():
    pembuatan_menu_barang = [
        "Nama barang",
        "Harga barang"
    ]

    pembuatan_menu_jasa = [
        "Nama jasa",
        "Harga jasa (tanpa harga barang yg dijual)"
    ]

    pengguna = input("Silahkan pilih jenis dagangan yang ingin dibuat (BARANG/JASA)").upper()
    if pengguna == "BARANG" or pengguna == "B":
        data_barang = {}
        for pertanyaan_b in pembuatan_menu_barang:
            if pertanyaan_b == "Harga barang":
                while True:
                    try:
                        jawaban = int(input(f"{pertanyaan_b}: "))
                        data_barang[pertanyaan_b] = jawaban
                        break
                    except ValueError:
                        print("Masukkan nilai angka untuk harga")
            else:
                jawaban = input(f"{pertanyaan_b}: ")
            data_barang[pertanyaan_b] = jawaban
        menu_barang.append(data_barang)    

    elif pengguna == "JASA" or pengguna == "J":
        data_jasa = {}
        for pertanyaan_j in pembuatan_menu_jasa:
            if pertanyaan_j == "Harga jasa (tanpa harga barang yg dijual)":
                while True:
                    try:
                        jawaban = int(input(f"{pertanyaan_j}: "))
                        data_jasa[pertanyaan_j] = jawaban
                        break
                    except ValueError:
                        print("Masukkan nilai angka untuk harga")
            else:
                jawaban = input(f"{pertanyaan_j}: ")
            data_jasa[pertanyaan_j] = jawaban
        menu_jasa.append(data_jasa)

    lanjutan_pembuatan = input("Apakah ingin membuat menu yang lain? [Y/N]").upper()
    if lanjutan_pembuatan == "Y":
        pembuatan_menu_barang_dan_jasa()
    elif lanjutan_pembuatan == "N":
        menu_utama_fitur_pembukuan()
    else: 
        print("Input tidak valid")
    

def daftar_menu_kasir_online():
    print("========== DAFTAR BARANG ==========")
    if menu_barang:
        for i, item in enumerate(menu_barang):
            print(f"{i}. {item['Nama barang']} - Rp{item['Harga barang']}")
    else:
        print("Tidak ada barang yang tersedia.")

    print("\n========== DAFTAR JASA ==========")
    if menu_jasa:
        for i, item in enumerate(menu_jasa):
            print(f"{i}.{item['Nama jasa']} - Rp{item['Harga jasa (tanpa harga barang yg dijual)']}")
    else:
        print("Tidak ada jasa yang tersedia.")

def kasir_online():
    total_harga = 0
    while True:
        daftar_menu_kasir_online()
        
        jenis_dagangan = input("Apakah Anda ingin membeli BARANG atau JASA? (ketik 'selesai' untuk keluar): ").upper()
        
        # Berhenti jika pengguna mengetik "selesai"
        if jenis_dagangan == "SELESAI":
            break
        
        # Memilih barang berdasarkan indeks
        if jenis_dagangan == "BARANG" and menu_barang:
            try:
                indeks = int(input("Masukkan indeks barang yang ingin dibeli: "))
                if indeks < 0 or indeks >= len(menu_barang):
                    print("Indeks tidak valid. Silakan masukkan indeks yang benar.")
                    continue
                
                # Menambah harga barang yang dipilih ke total harga
                barang_terpilih = menu_barang[indeks]
                print(f"Anda memilih: {barang_terpilih['Nama barang']} dengan harga Rp{barang_terpilih['Harga barang']}")
                total_harga += barang_terpilih['Harga barang']
            
            except ValueError:
                print("Masukkan angka yang valid.")
        
        # Memilih jasa berdasarkan indeks
        elif jenis_dagangan == "JASA" and menu_jasa:
            try:
                indeks = int(input("Masukkan indeks jasa yang ingin dibeli: "))
                if indeks < 0 or indeks >= len(menu_jasa):
                    print("Indeks tidak valid. Silakan masukkan indeks yang benar.")
                    continue
                
                # Menambah harga jasa yang dipilih ke total harga
                jasa_terpilih = menu_jasa[indeks]
                print(f"Anda memilih: {jasa_terpilih['Nama jasa']} dengan harga Rp{jasa_terpilih['Harga jasa (tanpa harga barang yg dijual)']}")
                total_harga += jasa_terpilih['Harga jasa (tanpa harga barang yg dijual)']
            
            except ValueError:
                print("Masukkan angka yang valid.")
        
        else:
            print("Pilihan tidak valid atau daftar barang/jasa kosong.")

    print(f"\nTotal harga semua barang dan jasa yang dibeli hari ini: Rp{total_harga}")

    # Meminta pengguna memilih bulan untuk menyimpan transaksi
    bulan = input("Masukkan bulan untuk transaksi ini (misalnya: Januari, Februari, dst.): ").capitalize()
    if bulan not in pembukuan_bulanan:
        pembukuan_bulanan[bulan] = []  # Jika bulan belum ada, buat list baru untuk bulan tersebut
    pembukuan_bulanan[bulan].append(total_harga)  # Menambahkan total transaksi ke bulan yang dipilih

def laporan_bulanan():
    print("\n========== LAPORAN PENJUALAN BULANAN ==========")
    for bulan, transaksi_list in pembukuan_bulanan.items():
        total_bulanan = sum(transaksi_list)  # Menjumlahkan semua transaksi dalam satu bulan
        print(f"\nBulan: {bulan}")
        for i, transaksi in enumerate(transaksi_list, start=1):
            print(f"  Transaksi {i}: Rp{transaksi}")
        print(f"  Total pendapatan bulan {bulan}: Rp{total_bulanan}")
    print("===============================================")

def menu_utama_fitur_pembukuan():
    while True:
        print("======= Manage your shop and become a successful entrepreneur!!! =======")
        print("[1] Pembuatan Menu Barang/Jasa UMKM")
        print("[2] Kasir Online")
        print("[3] Laporan Keuangan Bulanan")
        print("[4] Kembali ke menu utama")
        input_pengguna = int(input("Masukkan indeks fitur yang ingin dipilih: "))
        if input_pengguna == 1:
            pembuatan_menu_barang_dan_jasa()
        elif input_pengguna == 2:
            kasir_online()
        elif input_pengguna == 3:
            laporan_bulanan()
        elif input_pengguna == 4:
            menu_utama.menu_utama_sahabat_usaha()
        else:
            print("Input tidak valid")

#menu_utama_fitur_pembukuan()