Menjaga agar data tetap konssiten dan mengatur urutan jalannya proses-proses sehingga dapat berjalan dengan lancar dan terhindar dari deadlock atau starcvation 

## Race condition
kondisi dimana dua atau lebih proses mengakses sumber daya secara bersamaan, hasil akhir dari data tersebut tergantung dari proses mana yang terakhir selesai dieksekusi, untuk mencegahnya diperlukan sinkronisasi

## Critical Section 
Solusi critical section harus memenuhi 3 yaitu 
- Mutual Exclution : kondisi dimana tidak ada dua proses yang menjalankan critical selection bersamaan
- terjadi kamjuan (progress) : proses yang sedang menjalankan remainder sectionnya, tidak boleh menjalankan critical setcion berikutnya sebelum proses lain menyelesaikan critical sectionyna
- Ada batas waktu (bounded waiting) : ada batas waktu suatu proses dapat menjalankan critical sectionnya 
Solusi critical section : 
- perangkat lunak : emnggunakan algoritma algoritma untuk mengatasi masalah critical section seperti : 
- Sinkronisasi 2 proses : 
	- Algoritma turn 
	- Algirtma Dekker/Algoritma flag
	- Algoritma Peterson/Algoritma turn-flag
- Sinkronisasi banyak proses :
	- Algoritma bakery
- perangkat keras : bergantung pada instruksti mesin tertentu, misalnya dengan menonatkfikan interupsi, mengunci suatu variabel tertentu atau menggunakan instruksi level mesin seperti tes dan set 

# Perangkat sinkronisasi 
- Semaphore : Sistem sinyal yang digunakan untuk berkomunikasi secara visual
- Visual : Suatu tipe data abstrak yang dapat mengatur aktviitas serta penggunaan resource oleh beberapa thread

### Semaphore 
Operasi standaar dalam semaphore : 
- Proberen : Test, decrement, release, buka, dll
- verhogen : increase, acquire, kunci dll 

Fungsi semaphore : 
- menangani mutual exclution
- sebagai resource controller
- komunikasi antar proses

readers/writes problems:
syarat : 
- reader menjadi prioritas
- writer menjadi prioritas
- reader dan writer menjadi prioritas dan memiliki prioritas yang sama

![[Pasted image 20240422093237.png]]

![[Pasted image 20240422093245.png]]

![[Pasted image 20240422093253.png]]