import webbrowser
import menu_utama
def pengisian_data():
    daftar_pertanyaan = [
        "Nama Lengkap",
        "NIK",
        "Nomor Hp",
        "Alamat penjual",
        "Alamat tempat usaha",
        "Jenis usaha (Barang/Jasa)",
        "Deskripsi usaha",
        "Modal usaha",
        "Target pemasaran usaha"
    ]

    respon_pengguna = {}

    for pertanyaan in daftar_pertanyaan:
        jawaban = input(f"{pertanyaan}: ")
        respon_pengguna[pertanyaan] = jawaban

def menu_utama_registrasi_umkm():
    link_template_surat = "https://bit.ly/Template_Surat_UMKM"
    link_pengajuan_berkas_pendukung = "https://bit.ly/Pengajuan_Berkas_Pendukung"
    link_upload_berkas_pendukung = "https://bit.ly/Upload_Berkas_Pendukung_UMKM"
    print("========== Pendaftaran UMKM ==========")
    print("Isi pertanyaan dibawah ini: ")
    pengisian_data()
    print("\n")
    print("Terima kasih telah mendaftar melalui program sahabat usaha !!!")
    print("Permintaan anda akan segera diverifikasi dan diproses setelah anda mengupload beberapa berkas pendukung. ")
    print("\n")
    print("Berikut ini daftar berkas pendukung yang dibutuhkan: ")
    print("1. Surat Keterangan Usaha (SKU)")
    print("2. Surat Keterangan Nomor Induk Berusaha (NIB)")
    print("3. Surat Izin Usaha Mikro-Kecil (IUMK)")
    print("4. Surat HKI Merek (Jika usaha memiliki merek)")
    print("5. Surat Izin Usaha Perdagangan (SIUP)")
    print("\n")
    while True:
        pilihan_upload_berkas = input("Sudah punya berkas-berkas pendukung? [Y/N]")
        if pilihan_upload_berkas.upper() == "Y":
            webbrowser.open(link_upload_berkas_pendukung)
            print("Membuka link di browser...")
            break
        elif pilihan_upload_berkas.upper() == "N":
            print("\n")
            print("Jika para pendaftar belum memiliki beberapa berkas yang dibutuhkan di atas dapat memembuat dan mengajukan pada linak berikut: ")
            print(link_pengajuan_berkas_pendukung)
            webbrowser.open(link_pengajuan_berkas_pendukung)
            print("Untuk template surat permohonan pembuatan berkas-berkas yang dibutuhkan dapat di download  pada link berikut: ")
            webbrowser.open(link_template_surat)
            print(link_template_surat)
            print("Segera siapkan semua berkas yang dibutuhkan !!!") 
        else:
            print("Pilihan tidak valid, pilih [Y/N]")
    webbrowser.open(link_upload_berkas_pendukung)
    menu_utama.menu_utama_sahabat_usaha()
    
menu_utama_registrasi_umkm()