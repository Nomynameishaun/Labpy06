# Labpy06
# Program Input Data list Sederhana menggunakan fungsi def()
Program sederhana ini ditulis dalam Python untuk pengguna memasukkan data dan menghitung nilai akhir berdasarkan bobot nilai tugas, UTS, dan UAS, lalu menampilkan data tersebut dalam format tabel yang rapih.
```ruby
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
```
# Flowchart
![flow](</gambar/Flowchart.png>)
## Penjelasan Program
### 1. Membuat Struktur Menu Utama
Di awal program, ada menu utama yang memberikan pilihan kepada pengguna:

L: Melihat data.
T: Menambahkan data.
U: Mengubah data.
H: Menghapus data.
C: Mencari data.
K: Keluar.
Kode untuk menu utama:

```ruby
def menu():
    print("\nProgram Input Nilai")
    print("===================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilih = input("Pilih menu: ").lower()
    return pilih
```

### 2. Menambahkan Data
Ketika pengguna memilih opsi "T", program meminta pengguna untuk memasukkan NIM, Nama, Nilai Tugas, Nilai UTS, dan Nilai UAS. Nilai akhir dihitung secara otomatis.

Kode untuk menambahkan data:
```ruby
def tambah_data():
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
    print("Data berhasil ditambahkan!")
```

### 3. Melihat Data
Opsi "L" memungkinkan pengguna melihat semua data yang telah dimasukkan. Jika tidak ada data, program menampilkan pesan "Tidak ada data."

Kode untuk melihat data:
```ruby
def lihat_data():
    if mahasiswa:
        print("Daftar Nilai Mahasiswa:")
        print("===================================================")
        print("| NIM   | Nama      | Tugas | UTS  | UAS  | Akhir |")
        print("===================================================")
        for nim, data in mahasiswa.items():
            print(f"| {nim} | {data['nama']} | {data['tugas']} | {data['uts']} | {data['uas']} | {data['akhir']:.2f} |")
        print("===================================================")
    else:
        print("Tidak ada data.")
```

### 4. Mengubah Data
Opsi "U" memungkinkan pengguna untuk mengubah data berdasarkan NIM. Jika NIM tidak ditemukan, program akan memberi tahu pengguna.

Kode untuk mengubah data:
```ruby
def ubah_data():
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in mahasiswa:
        print(f"Data ditemukan: {mahasiswa[nim]}")
        nama = input("Nama baru: ")
        tugas = float(input("Nilai Tugas baru: "))
        uts = float(input("Nilai UTS baru: "))
        uas = float(input("Nilai UAS baru: "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
        print("Data berhasil diubah!")
    else:
        print("Data tidak ditemukan.")
```

### 5. Menghapus Data
Opsi "H" memungkinkan pengguna untuk menghapus data berdasarkan NIM.

Kode untuk menghapus data:
```ruby
def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan.")
```

### 6. Mencari Data
Opsi "C" memungkinkan pengguna mencari data berdasarkan NIM.

Kode untuk mencari data:
```ruby
def cari_data():
    nim = input("Masukkan NIM yang akan dicari: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print(f"Data ditemukan: {data}")
    else:
        print("Data tidak ditemukan.")
```

### 7. Keluar dari Program
Opsi "K" memungkinkan pengguna keluar dari program dengan menutup loop utama.

## Struktur Lengkap Program
Berikut adalah gambaran bagaimana semua fungsi tersebut terintegrasi:
```ruby
mahasiswa = {}

while True:
    pilihan = menu()
    if pilihan == 'l':
        lihat_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid!")
```

### Hasil Output
Berikut adalah Contoh Ouputnya:
```ruby
Halo selamat datang, silahkan masukan T untuk memulai input data!
[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:
Pilihan: t
Tambah Data
NIM        : 3124
Nama       : nana
Nilai Tugas : 80
Nilai UTS   : 90
Nilai UAS   : 75
Data berhasil ditambahkan!

[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:
Pilihan: t
Tambah Data
NIM        : 3215 
Nama       : none
Nilai Tugas : 60
Nilai UTS   : 59
Nilai UAS   : 100
Data berhasil ditambahkan!

[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:
Pilihan: C
Cari Data
Masukkan NIM yang dicari: 3215
Data ditemukan!
NIM        : 3215
Nama       : none
Nilai Tugas: 60.0
Nilai UTS  : 59.0
Nilai UAS  : 100.0
Nilai Akhir: 73.65

[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:
Pilihan: h
Hapus Data
Masukkan NIM yang akan dihapus: 3124
Data berhasil dihapus!

[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:
Pilihan: l
Daftar Nilai
============================================================
| NO |    NIM    |    NAMA    | TUGAS | UTS | UAS | AKHIR |
============================================================
| 1  | 3215      | none       | 60.0  | 59.0 | 100.0 | 73.65 |
============================================================
[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:
Pilihan: k
Keluar dari program.
```
