# Program Input Nilai Mahasiswa lebih lanjut
print("Halo selamat datang, silahkan masukan T untuk memulai input data!")
data_mahasiswa = {}

def tambah_data():
    print("Tambah Data")
    nim = input("NIM        : ")
    nama = input("Nama       : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
    print("Data berhasil ditambahkan!\n")

def tampilkan_data():
    print("Daftar Nilai")
    print("=" * 60)
    print("| NO |    NIM    |    NAMA    | TUGAS | UTS | UAS | AKHIR |")
    print("=" * 60)
    if len(data_mahasiswa) == 0:
        print("|                     TIDAK ADA DATA                     |")
    else:
        for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:<2} | {nim:<9} | {data['nama']:<10} | {data['tugas']:<5} | {data['uts']:<3} | {data['uas']:<3} | {data['akhir']:<5.2f} |")
    print("=" * 60)

def ubah_data():
    print("Ubah Data")
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in data_mahasiswa:
        print("Masukkan data baru:")
        nama = input("Nama       : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
        print("Data berhasil diubah!\n")
    else:
        print("NIM tidak ditemukan!\n")

def hapus_data():
    print("Hapus Data")
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!\n")
    else:
        print("NIM tidak ditemukan!\n")

def cari_data():
    print("Cari Data")
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print("Data ditemukan!")
        print(f"NIM        : {nim}")
        print(f"Nama       : {data['nama']}")
        print(f"Nilai Tugas: {data['tugas']}")
        print(f"Nilai UTS  : {data['uts']}")
        print(f"Nilai UAS  : {data['uas']}")
        print(f"Nilai Akhir: {data['akhir']:.2f}\n")
    else:
        print("NIM tidak ditemukan!\n")

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:")
    pilihan = input("Pilihan: ").lower()
    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!\n")
