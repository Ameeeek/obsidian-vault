---
id: kriptografi
aliases: 
tags:
  - CyberSecurity
  - tugasAkhir
---

# Kriptografi 
- informasi yang tidak dapat dimengerti disebut dengan ciphertext
- informasi yang dapat dimengerti oelh manusia disebut plaintext
- plaintext dapat dirubah ke ciphertext dan sebaliknya, prosesnya dilakukan
melalui kriptografi
- secara etimologi, kriptografi berasal dari bahasa yunani, kryptos artinya
hidden or secret dan graphein artinya to write. jika digabungkan artinya secret writing
- secara definisi, kriptografi artinya men cipher dan men de-cipher suatu pesan
  dari kode rahasia.
- cipher - sandi, ciphertext - teks sandi
- kriptografi adalah ilmu dan seni untuk menjaga kerahasiaan pesan dengan cara
menyandikannya ke dalam bentuk yang tidak dapat dimengerti maknanya. 
- istilah kriptografi dalam Bahasa Indonesia: Ilmu Persandian

# Proses Kriptografi 
Kriptografi terdiri dari dua proses: 
1. Enkripsi: Transformasi dari plainteks menjadi cipherteks
2. Dekripsi: Transformasi dari cipherteks menjadi plainteks
kedua proses memerlukan kunci rahasia 
![encrypt-decrypt.png](encrypt-decrypt.png)

# Mengapa Kriptografi saat ini sangat penting? 
- Untuk menjaga kerahasiaan informasi 
    - data/informasi rahasia negara
    - data/informasi rahasia organisasi
    - data/informasi personal 
- Pada era digital saat ini, pertukaran informasi rawan terhadap penyadapan oleh
  pihak ketiga
- kriptografi berguna untuk melakukan pengamanan informasi yang rahasia agar tidak bocor kepada publik
Dengan ilmu dan teknologi kriptografi, informasi disajikan dalam bentuk ciphertext sehingga pihak ketiga tidak dapat memahami artinya.

# Status Data 
Data digital memiliki banyak tipe dan tujuan. Akan tetapi data dapat diklasifikasikan menjadi tiga status yaitu: 
    - Data yang beristirahat (at rest)
    - Data yang sedang dalam pergerakan (in motion)
    - Data yang sedang digunakan
masing masing status merepresentasikan, dimana letak data didalam sistem, dan bagaimana data itu digunakan saat itu juga. 
Perlu diketahui juga bahwa, status dari suatu data akan berubah dengan sangat cepat dan perlu dipahami secara mendalam masing masing status guna memilih strategi enkripsi yang tepat. untuk pembahasan mengenai status data dan penjagaannya dapat dilihat [[statusDataDanPencegahannya|disini ]]

# Elemen Kriptografi 
- Algoritma Kriptografi (cipher)
  Aturan untuk enkripsi dan dekripsi atau fungsi matematika yang digunakan untuk enkripsi dan dekripsi
- kunci
  Parameter yang digunakan untuk transformasi enkrips dan dekripsi. Kunci bersifat rahasia, sedangkan algoritma kriptografi tidak rahasia 
- Pesan 
  Informasi yang di enkripsi/Dekripsi

![prosesEncryptDecrypt.png](prosesEncryptDecrypt.png)

# Algoritma Kriptografi
1. Algoritma Kriptografi Kunci-Simetri (symmetric-key cryptography)
2. Algoritma Kriptografi Kunci-publik (public-key cryptography)
3. Fungsi Hash

# Kriptografi Kunci-Simetri
- symmetric-key cryptography 
- kunci enkripsi = kunci dekripsi
![prosesEncryptDecrypt.png](prosesEncryptDecrypt.png)
- contoh algoritma kriptografi kunci-simetri: 
  - DES (Data Encryption Standard)
  - AES 
  - Blowfish
  - SEED
  - IDEA
  - GOST 
  - Serpent 
  - RC4, RC5

# Kriptografi Kunci-publik
- kunci enkripsi != kunci dekripsi 
- kunci enkripsi bersifat publik, sedangkan kunci dekripsi bersifat rahasia
![cryptoKeyPublic.png](cryptoKeyPublic.png)
- Contoh algoritma kunci-publik:
  - RSA 
  - ELGamal
  - Rabin 
  - Diffie-Helamn Key Exchange 
  - DSA 
  - Elliptic Curve Cryptography (ECC)
![keyPublicIllust.png](keyPublicIllust.png)

# Fungsi Hash 
- Mengkompresi pesan menjadi ukuran sangat kecil dan fixed 
- Sensitif terhadap manupulasi sekecil apapun
![hash.png](hash.png)

# Kegunaan Kriptografi 
1. Kerahasiaan 
Layanan apapun yang digunakan untuk menjaga isi pesan dari siapapun yang tidak berhak untuk membacanya
2. Integritas Data 
Layanan yang menjamin bahwa pesan masih asli/utuh atau belum pernah dimanupulasi selama pengiriman3. Otentikasi
Layanan yang untuk mengidentifkasi kebenaran pihak-pihak yang berkomunikasi 
4. Nirpenyangkalan
Layanan untuk mencegah entitas yang berkomunikasi melakukan penyangkalan, yaitu pengirim pesan menyangkal melakukan pengiriman atau penerima pesan menyangkal telah menerima pesan
