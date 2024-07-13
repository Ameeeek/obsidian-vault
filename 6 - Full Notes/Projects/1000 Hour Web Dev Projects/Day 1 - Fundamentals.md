# Computer Science 
Computer Science atau ilmu komputer adalah bidang ilmu yang mempelajari segala sesuatu mengenai komputer baik dari komputasi, hingga subjek yang lebih konkret seperti bahasa pemrograman, perangkat lunak, dan perangkat keras
# Software Development
Proses membuat sebuah perangkat lunak
# Web Development
Proses membuat sebuah website atau suatu situs internet
## Perbedaan Software dan Web Development 
Software developer berfokus pada pengembangan software atau perangkat lunak pada desktop dan mobile, sedangkan web developer berfokus pada pengembangan situs internet atau website yang berjalan pada peramban atau browser 

# Bagaimana sebuah website bekerja ? 
sebelum terburu-buru memasuki kapan sebuah website itu bekerja, mari masuk ke sedikit pemahaman mendasar terlebih dahulu
## Apa itu website? 
website adalah kumpulan halaman web atau webpages yang saling terhubung dan dapat diakses melalui internet
## Lah, webpages itu apa lagi ? 
jika kita analogikan dengan buku, website dapat kita sebut sebagai buku, selayaknya buku, tiap buku memiliki jumlah halaman yang berbeda, dan isi konten yang berbeda. Webpages pun demikian, kita dapat menganalogikan webpages sebagai sebuah halaman dari suatu web, dengan isi konten tertentu. 

# Web host atau Hosting server 
setiap website yang ada di internet, berada pada sebuah komputer fisik yang ada terletak entah dibelahan bumi bagian mana. Agar pengguna dapat mengakses website kapan saja, komputer tersebut harus dipastikan selalu menyala kapanpun itu. Tentu saja ini tidak memungkinkan bagi semua orang, oleh karena itu muncul sebuah jasa hosting dimana pihak penyedia jasa akan menghosting atau menaruh website kita diinternet agar dapat diakses oleh pengguna yang lain, dan pastinya kita akan dikenakan biaya oleh pihak penyedia jasa 

## Domain Name 
sekarang kita sudah tahu bahwa website pasti akan berada di entah dimana, kita ingin mengaksesnya tapi kita tidak tau alamatnya ada dimana, disini lah nama domain bekerja, setiap domaiin memiliki IP addressnya tersendiri. Dan pastinya kita tidak mungkin menghafal semua IP address dari masing masing website. sebuah nama domain perlu diregistrasi oleh pemilik website terlebih dahulu sehingga pengguna dapat mengaksesnya dengan mengetikkan nama domainnya pada search bar yang ada di sebuah peramban, seperti facebook.com, youtube.com, you name it.

## DNS Server 
DNS server adalah singkatan dari domain name system, DNS berfungsi untuk mengkonversi nama domain yang yang dimasukkan oleh pengguna pada address bar menjadi IP address, sesuai yang telah diregistrasi oleh pemilik website. karena saat kita memasukkan nama domain yang tidak teregistrasi, tentunya peramban atau browser akan kebingungan website mana yang ingin di akses oleh pengguna

# Proses sebuah website bekerja
untuk mempersingkat saja, dia dapat diringkas seperti berikut
Pengguna menulis nama domain di address bar, dan browser melakukan request ke DNS server untuk mencari IP address sesuai dengan domain name yang dimasukkan, setelah didapatkan maka dilakukan request lagi ke server utama, dan dikirimkan response ke browser lagi kembali, dan website pun dapat diakses oleh sisi pengguna

# Apa itu HTTP 
HTTP adalah protokol jaringan lapisan aplikasi yang dikembangkan untuk membantu proses transfer antar komputer. Protokol ini berguna untuk mentransfer informasi seperti dokumen, file, gambar, dan viddeo antar komputer

Sesuai dengan namanya, penggunaan Protokol HTTP (Hypertext Transfer Protocol) berhubungan dengan hypertext sehingga banyak mengambil sumber daya dari sebuah tautan - sebuah jenis berkas yang bertindak sebagai referensi ke berkas lainnya atau direktori. 

Protokol HTTP menyediakan kumpulan perintah di dalam komunikasi antar jaringan. 
![[Pasted image 20240605232137.png]]
komputer client melakukan permintaan menggunakan browser ke webserver, kemudian webserver menanggapi permintaan tersebut denga nmengirimkan data/dokumen yang tersedia didalam webserver sesuai dengan permintaan komputer client. 
Sebenarnya ada protokol lain untuk bertukar data dan informasi seperti SMTP, FTP, IMAP, atau POP3. Namun protokol HTTP yang paling banyak digunakan dengan yang lainnya. Alasannya karena HTTP pertama kali memang didesain untuk mengelola dokumen HTML dan mengirimkannya kepada client.

Selain itu, protokol HTTP cukup fleksibel dan sampai saat ini tersu dikembangkan dengan penambahan beberapa fitur baru. Hal ini membuat protokol HTTP menjadi protokol yang paling dapat diandalkan dan paling cepat memprose pertukaran data

# Fungsi HTTP 

Fungsi HTTP yaitu mengatur format dan bagaimana data ditransmisikan. HTTP juga berfungsi untuk mengatur bagaiman webserver dan browser memproses berbagai macam perintah yang masuk

Contohyna, ketika kita memasukkan domain URL di dalam browser. URL yang dimasukkan tersebut merupakan sebuah perintah ke dalam webserver untuk memberikan data halaman website sesua dengan alamat yang diakses, hasil dari perintah adalah tampilkan website yang muncul melalui web browser. 

Fungsi lain HTTP adalah mengamankan data dari pencurian dan hacker. Hal ini ditangan idengan muncul HTTPS atau Hypertext protocol secure yang secara fungsi itu sama untuk mengatur bagaimana data di proses, hanya saja HTTPS adalah protokol yang lebih aman ketimbang HTTP 

# Cara Kerja HTTP 
- HTTP client mengirimkan request ke webserver
- HTTP Server memproses request client, kemudian mengirimnya kembali ke HTTP Client

# Apa itu Server
dalam jaringan komputer istilah server berfungsi menjadi pelayan untuk memenuhi request atu permintaan dari pelanggan atau client.

# Apa itu client
Sementara client merupakan komputer lain yang bertindak sebagai penerima layanan dari server atas permintaan yang diiberikan

## Apa perbedaan HTTP Server dan HTTP Client
HTTP Server adalah pelayan yang akan memenuhi dan memprose request yang dikirim oleh HTTP Client setelah itu, data yang yang direquest dan telah dirpsoses akan dikirim lagi ke HTTP Client disebut dengan response, sedangkan HTTP Client adalah komputer pengguna yang akan memproses response dari HTTP Server untuk menampilkan apa yang baru saja diminta atau di request 