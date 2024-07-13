## Proses 
Suatu proses adalah sebuah program yang sedang dalam eksekusi, eksekusi suatu proses harus berlanjtu secara berurutan. Ketika suatu program dimuat kedalam meori, dan itu menjadi suatu proses, itu dapat dibagi menajdi empat bagian yaitu: 
- Stack :  proses berisi data sementara seperti parameter metode/fungsi, alamat pengirim dan variabel lokal 
- Heap : memori yang dialokasikan secara dinamis untuk suatu proses selama waktu dijalankan
- Data : Berisi variabel global dan statis
- Text : aktivitas saat ini yang diwakili oleh program counter dan isi register prosesor![[Pasted image 20240422080400.png]]

## Siklus Hidup proses
Ketika proses dijalankan ia melewati berbagai kondisi yaitu: 
- Start : kondisi awal saat proses pertama kali dimulai/dibuat
- Ready : proses sedang menunggu untuk ditugaskan ke prosesor
- Running : Setelah proses ditetapkan ke prosesor oleh penjadwal OS, status proses sdiatur ke berjalan dan prosesor menjalankan instruksinya
- Waiting : Proses berpindah ke status menunggu jika perlu menunggu sumber daya, speerti menunggu input pengguna, atau menunggu file tersedia
- Terminated/exit : Setelah proses selesai dieksekusi, atau diakhiri oleh sistem operasi, ia dipindahkan ke status terminasi dimana ia menunggu untuk dihapus dari memori utama.![[Pasted image 20240422080700.png]]

## Blok Kontrol Proses (PCB)
Blok Kontrol Proses adalah struktur data yang dikelola oleh sistem operasi untuk setiap proses. 
Deskripsi Block Kontrol Proses: 
- Process state : keadaan proses saat ini yaitu apakah sudah siap, berjalan, menunggu atau apapun
- Process Privileges : ini diperlukan untuk mengizinkan / melarang akses ke sumber daya sistem
- ID Proses : identifikasi unik untuk setiap proses dalam sistem operasi
- Pointer : Proses penunjuk ke induk
- Program Counter : Penunjuk ke alamat instruksi berikutnya yang akan dieksekusi untuk proses ini
- CPU Registers : berbagai register CPU dimana proses perlu disimpan untuk eksekusi untuk menjalankan kondisi
- CPU Scheduling Information : Prioritas proses dan informasi penjadwalan lainnya yang diperlukan untuk menjadwalkan proses
- Memory management information : Ini termasuk informasi tabel halaman, batas memori, tabel Segmen tergantung pada memroi yang digunakan oleh sistem operasi
- Accounting Information : Ini termasuk informasi tabel halaman, batas memori, tabel Segmen tergantung pada memori yang digunakan oleh sistem operasi
- IO Status Information : ini termasuk daftar perangkat I/O yang dialokasikan untuk proses tersebut.