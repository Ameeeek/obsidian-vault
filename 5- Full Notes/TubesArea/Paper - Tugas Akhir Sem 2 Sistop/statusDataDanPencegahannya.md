---
id: 1716813286-PRNO
aliases:
  - visini
tags:
  - CyberSecurity
  - tugasAkhir
---
# Klasifikasi Status Data dan Perlindungannya.
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
## Proteksi Data in Motion, Data at Rest, dan Data in Use
melindungi masing masing tipe data, akan memerluka perlindungan yang berbeda juga, oelh karena itu kunci dari melindungi data adalah mengetahui pendekatan yang akan digunakan untuk melindungi masing masing tipe data

sebelum masuk lebih dalam, ada 2 hal yang perlu diketahui, yaitu. 

## Perlindungan data secara reaktif itu tidak efektif. 
disaat data perusahaan sudah terserang, fokusnya akan berubah dari perlindungan to manajemen resiko dan meminimalisir dampak serangan

tentu saja kita tidak menginginkan hal tersebut, oleh karena itu kita harus memastikan dan mengecek mana data yang dalam bahaya, dan perlu di implementasikan perlindungan secara proaktif untuk menghindari terjadinya serangan pada saat itu juga. 

## Pengklasifikasian data itu sangat penting untuk proteksi yang baik
Perusahaaan akan sangat diuntungkan apabila perusahaan menggunakan metode sekuritas yang efektif, jika mereka menggunakan semua data dan memahami apa resiko yang ada pada masing masing status data.

# Perlindungan Data 
## Perlindungan Data in Motion
### Ciptakan Pondasi yang kuat
    Autentikasi dan firewall adalah hal mendasar pada perlindungan data akan tetapi merupakan teknologi perlindungan jaringan yang sangat untuk menjaga data dari penyerangan dari pihak yang tidak terotorisasi dan percobaan pembobolan 
### Implementasikan kebijakan kontrol otomatis 
    kebanyakan solusi yang ditawarkan saat ini mencakup dengan membuat aturan otomatis yang mencegah file yang berbahaya, memperingati pengguna ketika mereka dalam bahaya, dan secara otomatis mengenkripsi data yang sedang dalam transit atau dalam proses perpindahan. Ini membantu bisnis dengan aman untuk mengatur jumlah lampiran email yang meningkat, menjaga penyimpanan dan perpindahan informasi
### Implementasikan enkripsi Email 
    dengan mengenkripsi email, maka semua isi dari email akan terjaga dan baik karena isi dan lampirannya telah ter encode dengan baik. 
### Implementasikan pencegahan data DLP
    Data Loss Prevention atau DLP adalah solusi untuk membantu bisnis kehilangan IP, data customer dan mencegah kebocoran data yang sensitif. DLP mengawasi semua email yang berpotensi membocorkan email dengan menentukan kata kunci tertentu, hash dan dictionaries. Email yang mencurigakan akan di larang atau dikirim melalui gerbang pesan yang aman, bergantung dengan regulasi atau aturan yang diterapkan disuatu perusahaan. 

## Perlindungan data in use
### Implementasikan kontrol data digunakan
    sebelum orang bisa mengakses informasi itu sendiri kontrol data seharusnya sudah digunakan, sebelum data itu dapat diakses oleh pengguna. Karena Peretas tidak dapat diregulasikan mengenai apa yang boleh dan tidak boleh dia lakukan terhadap data yang sudah dia retas

### tingkatkan manajemen identitas 
    pencurian identitas sedang marak terutama bagi orang yang sering membagikan informasi perrsonal di internet secara cuma-cuma. Dengan memanage sistem identitas dengan pada suatu organisasi, maka informasi sensitif dapat lebih terjaga 

### Atur Hak Akses 
    dengan menggunakan hak akses digital, Information rights management, atau yang seperti yang fisebutkan, akses terhadap suatu file dapat dilimitasi atau dibatasi, sehingga menjamin kemanan suatu file. 

## Perlindungan data at Rest
### Gunakan enkripsi disket yang lengkap untuk keamanan 
    laptop yang disalah letakkan mungkin hanya akan menyebabkan kerugi berapa ratus ribut, tetapi data didalam disketnya berharga jauh dari itu, sehingga perlu untuk mengenkripsi nya agar pengguna yang tidak bertanggung jawab tidak dapat mengakses disket dengan begitu saja tanpa adanya login dengan baik apabila enkripsi disket dilakukan dengan benar 
### Implementasikan DLP
    Sebagai tambahan dari melindungi data yang sedang in motion, DLP juga memberikan organisasi fasilitas untuk mencari dan menemukan data yang sensitif di jaringan mereka, dan juga mencegah akses dari user yang mencurigakan
### perluas pencegahan ke cloud
    Clous access security Brokers (CASBs) memfasilitasi bisnis untuk mengaplikasikan kebijakan DLP ke data yang disimpan dan dibagikan di clodu. ini dapat dilihat di sistem back-end dan platform kolaborasi seperti slack dan microsoft 365. CASB berfungsi mirip seperti DLP, tapi kebijakan dan aturannya di khususkan untuk penyimpanan cloud
### Peranti mobile yang aman 
    Peranti telepon genggam dan tablet sangat umum di tempat kerja yang modern, mobile device management atau MDM adalah metode yang populer untuk digunakan untuk menjaga data di peranti telepon genggam. teknologi MDM membatasi akses data ke aplikasi korporat, mencegah dan melarang peranti yang telah dipegang oleh orang yang tidak bertanggung jawab dan semua data yang ada akan di enkripsi dan tidak dapat di decipher atau di decrypt oleh orang lain selain user yang telah diberi akses
