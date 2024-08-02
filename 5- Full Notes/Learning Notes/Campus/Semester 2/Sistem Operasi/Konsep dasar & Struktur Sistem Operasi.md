# Sistem Komputer 
terbagi atas 3 yaitu:
- **Hardware** yang menyediakan sumber daya komputasi dasar seperti CPU, I/O Device, Memori 
- **Sistem Operasi** yang mengontrol dan mengoordinasikan penggunaan hardware diantara berbagai aplikasi dan pengguna
- **Software** menentukan cara bagaimana sumber daya sistem digunakan untuk memecahkan masalh pada komputasi dari pengguna 
- **Brainware** pengguna mesin, bisa orang, mesin atau komputer lain 
- **Resource manager** Pengelola sumber daya yang terdapat pada sistem komputer
- **Extended Machine** Menyediakan sekumpulan layanan ke pemakai sehingga memudahkan dan menyamankan penggunaan serta pemanfaatan sumber daya sistem komputer. 

# Manajemen Proses 
Proses adalah program yang dieksekusi - memerlukan sumber daya, contoh : waktu CPU, memory, file, I/O Device 
OS bertanggung jawab dalam: 
- Create & Delete ; baik proses user maupun sistem 
- Suspend & Meneruskan Proses 
- Mendukung mekanisme-mekanisme sinkronisasi proses 
- Mendukung mekanisme komunikasi prosers 
- mendukung mekanisme penanganan deadlock 

# Manajemen Memori Utama 
Memori merupakan array (susunan) word/byte dalam jumlah besar dan memiliki alamatnya sendiri, dan bersifat volatile
OS bertanggung jawab dalam: 
- keep track bagian mana dari memori yang sedang digunakan dan oleh siapa
- memilih program yang akan di load ke memori
- alokasi dan dealokasi ruang memori 

# Manajemen Sistem Berkas 
Berkas atau file adalah kumpulan informasi yang berhubungan dan biasanya merepresentasikan program dan data
OS bertanggung jawab dalam: 
- Pembuatan dan penghapusan file 
- pembuatan dan penghapusan direktori
- meandukung manipulasi file dan direktori
- pemetaan file dalam secondary storage
- backup file dalam media yang stabil (non-volatile)

# Manajemen I/O 
Sering disebut dengan device manager, dia bertugas untuk menyediakan device driver yang umum sehingga operasi I/P dapat seragam (Create, Read, write, close/delete)
Contoh: User menggunakan operasi yang sama untuk membaca berkas pada CD Rom dan flashdisk 
Komponen OS untuk sistem I/O 
- Penyangga: Menampung sementara data dari/ke perangkat I/O
- Spooling : Melakukan penjadwalan pemakaian I/O Supaya lebih efisien 
- Menyediakan driver 

# Manajemen Secondary Storage 
Backup main memory, non-volatile
Data dan progarm disimpan dalam secondary storage (penyimpanan sekunder; disk)
OS bertanggung jawab dalam: 
- mengelola ruang yang kosong dalam storage 
- alokasi penyimpanan
- penjadwalan disk 

# Sistem Proteksi
Mekanisme untuk mengatur/mengendalikan akses yang dilakukan oleh program, prosesor atau user ke sumber daya yang ada dalam sistem koomputer 
Mekanisme Proteksi : 
- Dapat membedakan pemakaian yang sah dan tidak sah
- spesifikasi kendali yang dikenakan

# Jaringan (Distributed System)
Sekumpulan proses yang tidak berbagi memory atau clock dimana tiap prosesor memiliki memori lokal masing masing 
prosesor dalam sistem terhubung dalam jaringan komunikasi 
distributed system bertugas sebagai:
- pengatur atau protokol dalam komunikasi data 
- menentukan strategi-strategi menangani masalah-masalah komunikasi 
- mengatur network file system
Dengan adanya shared resource: 
- Peningkatan kecepatan komputasi
- Peningkatan penyediaan data
- Meningkatkan reliabilitas (Kehandalan)

# Command Interpreter 
Memungkinkan sistem berkomunikasi dengan user melalui perintah perintah tertentu untuk menjalankan proses yang telah didefinisikan beserta parameternya kemudian melakukan respon 
OS menunggu perintah/instruksi dari user (Command-Driven)
Contoh Command Interpreter : 
- Command-Line Interpreter (CLI)
- Shell 
Command-interpreter system sangat bervariasi dari satu sistem operasi ke sistem operasi yang lain semuanya disesuaikan dengan tujuan dan teknologi I/O yang ada seperti :
- DOS, windows, dll

# Layanan Sistem Operasi 
- Eksekusi program : Load program user ke memori dan menjalankannya (RUN)
- Operasi I/O : Pengguna tidak bisa mengendalikan I/O Secara langsung (untuk efisiensi dan keamanan), sistem harus bisa menyediakan mekanisme untuk melakukan operasi I/O
- Manipulasi file system : read, write, create & delete
- Komunikasi antar proses : baik yang di run komputer yang sama atau berlainan via jaringan. Implementasinya melalui shared memory atau message passing 
- error detection
- menjamin komputasi yang benar dengan mendeteksi error : CPU, memori, I/o device, atau user program
- Resource allocation : mengalokasi sumber daya bagi sejumlah user atau job yang running pada saat yang sama
- Accounting : Mencatat jumlah pengguna yang menggunakan sumebr daya, dan jenis sumber dayanya 
- Protection : Menjamin agar semua akses ke sumber daya terkendali contoh: menyediakan password jika akan akses ke sumber daya

# Sistem Program 
Menyediakan lingkungan yang memungkinkan pengembangan program dan eksekusi berjalan dengan baik 
Dapat dikategorikan: 
- Manipulasi Berkas (File)
- Informasi Status : tanggal, jam, jumlah memori, disk, dll
- Modifikasi Berkas 
- Mendukung bahasa pemrograman : Kompilator, assembly, interpreter 
- Loading dan Eksekusi program
- Komunikasi : menyediakan mekanisme komunikasi antara proses, user dan sistem komputer yang berbeda

# Sistem Call
Permintaan yang dilakukan oleh proses aktif melalui software interrupt/execption untuk mendapatkan layanan kernel
Single prosesor menjalankan satu instruksi setiap waktu, jika sebuah proses yang berjalan di user mode dan membutuhkan layanan sistem, harus melakukan sistem call. Contoh : membaca data dari file
OS kemudian mengenali keinginian proses dengan memeriksa parameter yang diberikan oleh proses 
Tigas metode untuk passing parameter antara running program dan OS : 
- Melalui register 
- Menyimpan parameter dalam bnlok atau tabel pada memori, dan alamat blok tsb diberikan sebagai parameter dalam register
- Menyimpan paramter (Push) ke dalam Stack (oleh program), dan pop off pada parameter stack (oleh OS)

- Proses Kontrol : Load, execute, create/terminate process , get/set process attributes, wait dll 
- File management : Create/Delete file, open/close, read/write, get/set file attributes, dll 
- Device Management : Request/Release device, get/set devce attributes, dll 
- Information Maintanance : Get/set time, dll 
- Communication : create/delete connection, send/receive message, dll

# Struktur Sistem Operasi
## Monolithic 
Struktur Sederhana, OS Ditulis sebagai kumpulan prosedure, masing-masing dapat memanggil prosedur yang lain jika dibutuhkan 
dengan struktur berikut : 
- Main procedure yang memanggil service procedure
- Service procedure yang menangani sistem call
- Utility procedure yang mendukung service procedure
## Layered / berlapis 
OS Dibagi menjadi sejumlah lapisan yang masing-masing dibangun di atas lapisan yang lebih rendah, lapisan yang lebih rendah menyediakan layanan untuk lapisan yang lebih tinggi.
Lapisan paling bawah : perangkat keras
Lapisan paling atas : antarmuka pengguna 

tingkatan layered: 
Level 5 : Operator/User
Level 4 : User Program, menangani kompilasi, eksekusi dan printing user program
Level 3 : I/O Management
Level 2 : Operator-proses communication
Level 1 : Memory Management, alokasi memori untuk proses 
Level 0 : Processor allocation dan multiprogramming, menentukan alokasi proses ke CPU, menangani interupsi dan perpindahan proses sebagai scheduler

## Virtual Machine 
Implementasi software dari sebuah mesin yang menjalankan program seperti mesin secara fisik 
yang merupakan duplikat dari mesin yang sebenarnya. 
Masing masin VM mempunyai prosesor, memori dan sumber daya lain secara terpisah di dalam satu mesin host. 
Contoh VM Software: 
- VirtualPC 
- VMWare
- VirtualBox

## MikroKernel
Kernel yang menyediakan hanya sekumpulan kecil abstraksi perangkat keras sederhana, dan menggunakan aplikasi-aplikasi yang disebut sebagai server untuk menyediakan fungsi-fungsi lainnya.
Mikrokernel bekerja dengan cara menyusun sistem operasi dengan menghapus semua komponen yang tidak esensial dri kernel, dan mengimplementasikannya sebagai ssitem program dan level pengguna 

## Exokernel
Kernel yang hampir tidak menyediakan sama sekali abstraksi hardware, tapi ia menyediakan sekumpulan library yang menyediakan fungsi-fungsi akses ke perangkat keras secara langsung 

# Kesimpulan :
- Sistem Operasi adalah perangkat lunak yang bertindak sebagai antarmuka pengguna antara pengguna komputer dan perangkat keras komputer serta mengontrol pelaksanaan semua jenis program yang berfungsi untuk mengelola seluruh komponen dan sumber daya komputer, fisik maupun non fisik seperti data agar dapat digunakan secara optimal 
- Sistem Operasi terdiri dari beberapa komponen antara lain manajemen proses, manajemen memori utama, manajemen file, manajemen sistem I/O, manajemen penyimpanan sekunder, sistem jaringan, sistem proteksi dan sistem command interpreter 
- Struktur sistem operasi sendiri terbagi atas monolitik, layered, virtual machine, mikro dan exokernel