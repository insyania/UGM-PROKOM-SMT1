print('SELAMAT DATANG DI PRAKTEK DOKTER TEDUH'.center(40))
print(40 * '-')
print()

def pengguna ():            #untuk mengetahui apakah pengguna seorang dokter, pasien, perawat, ataupun staff
    print('1. dokter')      
    print('2. apoteker') 
    print('3. perawat')
    print('4. staff')
    print('5. pasien')  
    while True:             # akan melakukan perulangan apabila jawaban tidak sesuai
        user = str(input('Siapakah anda? '))        #pengguna diminta untuk memasukkan apakh dia seorang dokter, apoteker, perawat, ataupun staff
        if user == ('dokter'):
            print('Harap masuk ke laman dokter!')
            exit()
        elif user == ('apoteker'):
            print('Harap masuk ke laman apoteker!')
            exit()
        elif user == ('perawat'):
            print('Harap masuk ke laman perawat!')
            exit()
        elif user == ('staff'):
            print('Harap masuk ke laman staff!')
            exit()
        elif user == ('pasien'):
            print(' Selamat datang di laman pasien')
            break
        else:
            print('Harap masukkan data sesuai data diatas!')

def patient():      #untuk mengetahui data pasien yang dibutuhkan dokter
    while True:     # akan melakukan perulangan apabila jawaban tidak sesuai
        kunjungan = str(input('Apakah ini kunjungan pertama anda? '))   #pengguna diminta untuk memasukkan kunjungan ke berapa
        if kunjungan == ('iya'):
            print('Isi data berikut!') 
            nama = str(input('Masukkan nama anda: '))
            usia = int(input('Berapa usia anda? (dalam tahun): '))
            alamat = (input('Masukkan alamat anda: '))
            contact = int(input('Masukkan nomor handphone yang bisa dihubungi: '))
            alergi = str(input('Alergi obat apa yang anda miliki? (jika tidak ada boleh diisi null): '))    
            asuransi = str(input('Masukkan nama asuransi anda jika ada (ketik null jika tidak ada): '))
            gula_darah = str(input('Kapan terakhir anda memeriksa gula darah? '))
            keluhan = str(input('Keluhan apa yang anda rasakan? '))
            diet = str(input('Apakah anda sedang melakukan diet? '))
            rujukan = str(input('Apakah anda bersedia dirujuk jika memerlukan pemeriksaan lanjutan? '))
            break
        elif kunjungan == ('tidak'):
            while True:
                janji = str(input('Apakah sudah ada janji temu sebelumnya? '))
                if janji == ('sudah'):
                    nama=str(input('Silahkan masukkan nama anda: '))
                    usia = int(input('Silahkan masukkan umur anda(dalam tahun): '))
                    handphone = int(input('Silahkan masukkan nomor handphone yang sudah terdaftar: '))
                    antrian = int(input('Masukkan nomor antrian yang sudah didapatkan'))
                    print('Terimakasih sudah mengkonkfirmasi! Jadwal dan data anda akan kami proses')
                    print()
                    print('SEMOGA LEKAS SEMBUH'.center(40))
                    print(40 * '-')
                    exit()
                elif janji == ('belum'):
                    nama=str(input('Silahkan masukkan nama anda: '))
                    usia = int(input('Silahkan masukkan umur anda(dalam tahun): '))
                    handphone = int(input('Silahkan masukkan nomor handphone yang sudah terdaftar: '))
                    print(40 * '-')
                    print()
                    jadwal()
                    print('Terimakasih sudah mengkonkfirmasi! Jadwal dan data anda akan kami proses')
                    print()
                    print('SEMOGA LEKAS SEMBUH'.center(40))
                    print(40 * '-')
                    exit()
                else:
                    print('Jawaban hanya "sudah" atau "belum"!')
        else:
            print('Jawaban hanya "iya" atau "tidak"!')
    
def jadwal():               #untuk memilih jadwal kunjungan ke dokter
    print('Berikut jadwal dokter yang tersedia: ')
    print('1. Senin - Jumat pukul 17.00 - 21.00')
    print('2. Selasa, Kamis, Sabtu pukul 10.00 - 16.00')
    print('3. Sabtu dan Minggu pukul 09.00 - 15.00')
    while True:          # akan melakukan perulangan apabila jawaban tidak sesuai
        pilihan = int(input('Masukkan pilihan jadwal! '))        #pengguna diminta untuk memasukkan jadwal kunjunungan yang dipilih berdasarkan jadwal yang sudah ada
        if pilihan == 1: 
            hari = str(input('Masukkan hari pilihan anda: '))
            if hari == ('senin'):
                print('Datanglah di hari Senin antara pukul 17.00 - 21.00')
            elif hari == ('selasa'):
                print('Datanglah di hari Selasa antara pukul 17.00 - 21.00')
            elif hari == ('rabu'):
                print('Datanglah di hari Rabu antara pukul 17.00 - 21.00')
            elif hari == ('kamis'):
                print('Datanglah di hari Kamis antara pukul 17.00 - 21.00')
            elif hari == ('Jumat'):
               print('Datanglah di hari Jumat antara pukul 17.00 - 21.00')
            else:
                print('Sepertinya anda salah jadwal')
            break
        elif pilihan == 2:
            hari = str(input('Masukkan hari pilihan anda: '))
            if hari == ('selasa'):
                print('Datanglah di hari Selasa antara pukul 10.00 - 16.00')
            elif hari == ('kamis'):
                print('Datanglah di hari Kamis antara pukul 10.00 - 16.00')
            elif hari == ('sabtu'):
                print('Datanglah di hari Sabtu antara pukul 10.00 - 16.00')
            else:
                print('Sepertinya jadwal yang anda pilih salah')
            break
        elif pilihan == 3:
            hari = str(input('Masukkan hari pilihan anda: '))
            if hari == ('sabtu'):
                print('Datanglah di hari Sabtu antara pukul 09.00 - 15.00')
            elif hari == ('minggu'):
                print('Datanglah di hari Minggu antara pukul 09.00 - 15.00')
            else:
                print('Tidak ada jadwal yang sesuai!')
            break
        else:
            print('Pilih sesuai jadwal')
            
pengguna()
print(40 * '-')
print()
patient()
print(40 * '-')
print()
jadwal()
print(40 * '-')
print()
print('SEMOGA LEKAS SEMBUH'.center(40))
print(40 * '-')
