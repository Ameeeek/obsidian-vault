---
tags:
  - study
  - College
  - Notes
cssclasses: 
DosenPengajar: ibu hera
MataKuliah: Struktur Data
Semester: "2"
---
# Definisi 
## Data 
- keterangan yang benar dan nyata 
- keterangan atau bahan nyata yang dapat dijadikan dasar kajian 
- informasi dalam bentuk yang dapat diproses oleh komputer seperti representasi digital dari teks, angka, gambar grafis, atau suara
## Struktur 
- cara sesuatu disusun atau dibangun; susunan; bangunan
- yang disusun dengan pola tertentu
- pengaturan unsur atau bagian suatu benda 
- ketentuan unsur-unsur dari suatu benda
- pegnaturan pola dalam bahasa secara sintagmatis 
# Apa yang membuat algoritma dapat dikatakan baik? 
- Kebenaran dan ketepatan 
- Efisiensi
## Semua program berurusan dengan data 
- Sistem Informasi: Informasi, Laporan, User, ...
- Game: Posisi & Status pemain, Musuh, Skor, ...
- Search Engine: URL, isi, hyperlink, bobot, ...
## Mengapa data itu disimpan ? 
- Supaya bisa diakses/diproses di kemudian waktu
## Mengapa dalam penyimpanan data diperlukan sebuah struktur? 
- Supaya lebih mudah/efisien dalam pengaksesan/pemrosesan data tersebut

# Fungsi Strkutur data
## Sebagai Look-up Table: 
Struktur dibentuk untuk memungkinkan pencarian data dengan tingkat efisiensi yang baik 
## Sebagai representasi semantik dari Data: 
Struktur dibentuk sesuai dengan keterkaitan satu data dengan data lainnya. 

# Ruang Lingkup
- Struktur data Linier 
	- Array (unsorted, sorted), linked-list, Stack, Queue, Hash Tables 
- Struktur data hirarkis 
	- Tree, Binary Tree, Binary Search Tree, B+Tree
- Struktur data graph: 
	- Graph dengan varian-varian: Edge-list, vertex-list, adjacent list, adjacent matrix


![[Pasted image 20240308215413.png]]

# Struktur Data Primitif 
| Struktur Data |                           Deskripsi |              Contoh |
| ------------: | ----------------------------------: | ------------------: |
|       Integer |           Angka tanpa angka desimal |   1,2,3,4,5,6,7,... |
|         Float |          Angka dengan angka desimal |      2.5,4.3,6.3132 |
|     Character |                    Karakter Tunggal |           A,B,C,a,d |
|        String |                                Teks | Halo, Struktur Data |
|       Boolean | Nilai Logika antara true atau false |      True dan False |
# RPS
![[Pasted image 20240308215713.png]]

# Python Objek 
## Identifiers / Variable
Bersifat case/sensitive , Penamaan variabel dapat menggunakan kombinasi huruf maupun angka, tapi tidak menggunakan special keywords berikut 

|    and |    del |     from |     not | while |     as | elif |
| -----: | -----: | -------: | ------: | ----: | -----: | ---: |
| global |     or |     with |  assert |  else |     if | pass |
|  yield |  break |   except |  import | print |  class | exec |
|     in |  raise | continue | finally |    is | return |  def |
|    for | lambda |      try |    true | false |   none |      |
## Tipe Data
- Teks: str
- Numerik : int, float, complex
- Urutan : list, tuple, range
- pemetaan : dict
- set : set, frozenset
- Boolean : bool
- Binary : bytes, bytearray, memoryview
- None Type : NoneType

## ekspresi, operator, dan urutan
![[Pasted image 20240308220113.png]]

# Control Flow
## Percabangan
Proses pentnuan keputusan berdasrkan kondisi, hanya akan dieksekusi satu kali saja, syntax yang digunakan untuk melakukan percabangan adalah: 
- **if** kondisi utama,
- **elif** kondisi kedua atau ketiga hingga ke-x,
- dan **else** kondisi terakhir jika kondisi sebelumnya tidak terpenuhi 
## perulangan
perintah akan dilakukan seterusnya berulang-ulang dengan jumlah tertentu atau selama kondisi tertentu terpenuhi.

Terdapat dua konstruksi perulangan: 
- Perulangan **for** : kasus yang berkaitan dengan data sequence pada python, tau untuk kasus yang sudah jelas jumlah perulangannya
- perulangan **while** : perulangannya tidak jelas berapa banyak yang akan dilakukan 

## Fungsi
kumpulan perintah atau baris kode yang dikelompokkan menjadi satu kesatuan yang kemudian bisa dipanggil atau digunakan berkali-kali
```python
def nama_fungsi (parameters):
	#code
```
dimana 
- kata kunci **def** menjadi tanda blok kode merupakan sebuah fungsi
- nama_fungsi, nama dari fungsi
- parameters, nama variabel dimana data dapat diterima pada fungsi dibuat (opsional)
- code, isi dari fungsi
# Input dan Output 
## Input
merupakan suatu data atau sesuatu yang dimasukkan ke dalam program komputer untuk diproses.
```python
input(prompt)
```
dimana prompt merupakan string dimana data akan diambil
## output
merupakan informasi atau data yang dihasilkan setelah dilakukan pemrosesan oleh komputer
contoh 
output yang diinginkan "saya punya 3 pulpen"

```python
# cara 1:
print('Saya punya %d %s', %(a,b))
# cara 2
print('Saya punya ', a,b)
# cara 3 
print('Saya punya {} {}'.format(a,b))
# cara 4 
print('Saya punya ' + str(a) + ' ' + b)
# cara 5 
print(f'Saya punya {a} {b}')
```

# Exception Handling 
Kesalahan yang terdeteksi saat menjalakan program komputer disebut Error. 
Error mengakibatkan berhentinya sebuah program komputer. 
Pada python terdapat dua jenis error yaitu, 
- Syntax errors: kesalahan yang muncul karena penalasan sintaks yang tidak sesuai aturan dalam program
- exceptions: kesalahan yang tetap muncul padahal syntax sudah benar.
Python menyediakan metode untuk menangani error 
## penanganan
- try : memungkinkan dalam menguji blok kode untuk sebuah error 
- except : memungkinkan dalam menangani error
- else : memungkinkan dalam mengksekusi kode saat tidak ada kesalahan
- finally : memungkinkan dalam mengeksekusi kode, baik itu blok try atau except telah dieksekusi
- raise : melemapr suatu pesan pengecualian
