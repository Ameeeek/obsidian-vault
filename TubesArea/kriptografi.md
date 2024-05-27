---
id: kriptografi
aliases: []
tags: []
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
![encrypt-decrypt.png](assets/imgs/encrypt-decrypt.png)

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
Perlu diketahui juga bahwa, status dari suatu data akan berubah dengan sangat cepat dan perlu dipahami secara mendalam masing masing status guna memilih strategi enkripsi yang tepat
## Data at rest
data yang sedang beristirahat artinya, data sedang tidak aktif berpindah antar peranti, atau jaringan, atau tidak digunakan sama sekali. Biasanya data yang dalam status ini disimpan didalam harddrive, komputer personal atau basis data. 
Karena data sering kali di simpan di penyimpanan yang pasif, atau di server yang terlindungi, data yang dalam status ini paling jarang di retas, atau di akses oleh orang yang tidak memiliki akses. Tapi data yang paling krusial dan berharga, biasanya berada pada status at rest, maka peretas biasanya lebih mencari data tersebut untuk melancarkan aksinya 
## Data in motion
data yang sedang dalam pergerakan itu berarti datanya sedang berpindah dari satu titik ke titik yang lain, baik itu email, sms, alat kolaboratif atau bentuk saluran komunikasi apapun.
Karena sifatnya yang sedang berpindah, data ini akan sangat rentan terhadap penyadapan, yang dimana penyadapan adalah bentuk paling umum bagaimana suatu data dapat dicuri
oleh karena itu, data yang sedang dalam pergerakan memerlukan algoritma enkripsi terbaik 
## Data in use
Data in use merujuk pada data yang sedang aktif digunakan dan di proses oleh pengguna atau perangkat lunak. Data akan menjadi sangat rentan di tahap ini, mau itu dia sedang di baca, di proses atau dipperbarui, karena saat data sedang diakses, dia sedang dalam bentuk plaintext, ini memungkinkan peretas dapat langsung mengaksesnya, yang akan memberikan dampak yang cukup serius apabila tidak ditangani dengan baik 
sementara beberapa perangkat lunak sudah memiliki metode enkripsinya tersendiri, sangat penting untuk pengguna memastikan bahwa datanya tetap aman dari akses yang tidak memiliki hak atau otoritas. 
