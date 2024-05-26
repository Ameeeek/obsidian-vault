# Thread
Thread adalah sebuah alur kontrol dari sebuah proses. Kontrol thread tunggal ini hanya memungkinkan proses untuk menjalan satu tugas pada satu waktu. 
![[Pasted image 20240422085413.png]]
Multi-threading
![[Pasted image 20240422085653.png]]
Contoh Multi-Threading
- Banyak perangkat lunak yang berjalan pada PC Modern dirancang secara multi-threading
- sebuah aplikasi biasanya diimplementasi sebagai proses yang terpisah dengan beberapa thread yang berfungsi sebagai pengendali
- contohnya sebuah web browser mempunyai thread untuk menampilkan gambar atau tulisan sedangkan thread yang lain berfungsi sebagai penerima data dari network

## Thread dalam proses
Perbedaan antara proses dengan thread tunggal dengan proses dengan thread yang banyak adalah proses dengan thread yang banyak dapat mengerjakan lebih dari satu tugas pada satu satuan waktu

## Keuntungan thread
- responsi : membuat sebuah program terus berjalan meskipun sebagian dari program tersebut diblok atau melakukan operasi yang panjang.
- berbagai sumber daya : mengizinkan sebuah aplikasi mempunyai beberapa thread yang berbeda dalam lokasi memori yang sama
- ekonomi : lebih ekonomis
- utilisasi arsitektur multiprocessor : COPU dapat menjalankan setiap tbhnread secara bergantian tetapi hal ini berlangsung sangat cepat sehingga menciptakan ilusi paralel sedangkan pada kenyataanyna hanya satu thread yang dijalankan CPU pada satu satuan waktu 

## Multithreading
- Thread Pengguna : Thread yang pengaturannya dilakukan oleh pustaka thread pada tingkatan pengguna 
- Thread Kernel : Thread yang didukung langsung oleh kernel. 

### Model Multi Threading
- Many to One : 
	- memetakan banyak user-level thread ke satu kernel thread
	- pengaturan thread dilakukan di user space
	- efisien tetapi memiliki kelamahan yang sama dengan user thread
	- tidak dapat berjalan secara paralel pada multiprocessor 
- One to One : 
	- Memetakana setiap user thread ke kernel thread
	- meynediakan lebih banyak concurrency dibandingkan many to one 
	- kentungannya sama dengan kernel thread
	- kelemahannya, setiap pembuatan suer thread itbutuhkan pembuatan kernel thread yang dapat menurunakn performa
	- sistem operasi yang mendukung one to one : windows NT dan OS/2
- Many to Many : 
	- Multiplexes banyak user-level thread ke kernel thread yang jumlahnya lebih kecil atau sama banyaknya dengan user-level thread
	- jumlah kernel thread dapat spesifik untuk sebagiaan aplikasi atau sebagian mesin
	- developer dapat membuat user thread sebanyak yang diperlukan dan kernel thread yang bersangkutan dapat berjalan secara paralel pada multiprocessor
	- ketika suatu thread menajalnkan blocking sistem call maka kernel dapat menjadwalkan thread lain untuk melakuan eksekusi
	- sistem operasi yang mendukung model ini adalah solaris, irix dan digital UNIX