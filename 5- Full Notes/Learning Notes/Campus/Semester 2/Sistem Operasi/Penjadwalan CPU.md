Penjadwalan proses adalah aktivitas manajer proses yang menangani penghapusan proses yang berjalan dari CPU dan pemilihan proses lain berdasarkan strategi tertentu. 

## Antrian Penjadwalan proses
Sistem operasi memelihara semua PCB dalam antrian penjadwalan proses. Ketika status proses diubah, PCB-nya tidak terhubung dar antrian saat ini dan dipindahkan ke antrian status baru.
Sistem Operasi mempertahankan antrian penjadwalan proses penting sebagai berikut;
- Job Queue - Antrian ini menyimpan semua proses dalam sistem
- Ready Queue - Antrian ini menyimpan satu set semua proses yang berada di memori utama, siap dan menunggu untuk dieksekusi. Proses baru selalu dimasukkan ke dalam antrian ini 
- Antrian Perangkat - proses yang diblokir karena tidak tersedia perangkat I/O merupakan antrian ini ![[Pasted image 20240422081410.png]]

### Model Proses Two state
mengacu pada kondisi berjalan dan tidak berjalan yang dijelaskan sebagai berikut: 
- running : ketika proses baru dibuat, itu masuk ke dalam sistem seperti dalam kondisi berjalan
- not running : proses yang tidak berjalan disimpan dalam antrian, menunggu giliran mereka untuk dieksekusi

### Penjadwal 
Penjadwal / scheduler adlaah perangkat lunak sistem khsusu yang menangani penjadwalan proses dengan berbagai cara .Tugas utama mereka adalah memilih pekerjaan yang akan diserahkan ke dalam sistem dan memutuskan proses mana yang akan dijalankan dan terbagai atas tigas jenis: 

- Penjadwal jangka panjang / penanjadwal pekerjaan : menentukan program mana yang dimasukkan ke sistem untuk diproses
- Penjadwal jangka pendek / penjadwal CPU : meningkatkan kinerja sistem sesuai dengan kriteria yang dipilih 
- Penjadwal jangka menengah : bagian dari swapping yang menghapus proses dari memori

perbandingan antar penjadwal 

|  No |                                              Penjadwalan jangka Panjang |                                      Penjadwalan J. Pendek | Penjadwalan J. Menengah                                                           |
| --: | ----------------------------------------------------------------------: | ---------------------------------------------------------: | --------------------------------------------------------------------------------- |
|   1 |                                                   Penjadwalan pekerjaan |                                              Penjadwal CPU | Penjadwal proses swapping                                                         |
|   2 |                           Kecepatan kurang dari penjadwal jangka pendek |                                     Kecepatan paling cepat | Kecepatan ada di antara penjadwal jangka pendek dan jangka panjang                |
|   3 |                                     Mengontrol tingkat multiprogramming | memberikan kontrol yang lebih rendah pada multiprogramming | mengurangi tingkat multiprogramming                                               |
|   4 |              Hampir tidak ada atau minimal dalam sistem pembagian waktu |                            sistem berbagi waktu juga minim | bagian dari sistem pembagian waktu                                                |
|   5 | memilih proses dari pool dan memuatnya ke dalam memori untuk dieksekusi |                  memilih proses-proses yang siap dijalnakn | dapat memperkenalkan kembali proses ke dalam memori dan ekskusi dapat dilanjutkan |

# Algoritma Penjadwalan proses 
Penjadwalan proses menjadwalkan proses yang berbeda untuk ditugaskan ke CPU berdasarkan algoritma tertentu diantaranya yaitu: 
- First Come, First Served (FCFS)
	- Pekerjaan dieksekusi berdasarkan yang pertama datang, maka diluan dilayani
	- algoritam penjadwalan non-preemptive, pre-emptive
	- mudang dimengerti dan diimplementasikan
contoh algoritma FCFS

| Proses | Waktu Tiba | Lama Proses |
| -----: | ---------: | ----------: |
|      A |          0 |           4 |
|      B |          1 |           7 |
|      C |          3 |           3 |
|      D |          7 |           8 |


| Proses | Waktu Tiba WT | Lama Proses LP | Saat Rampung SR                      | Lama Tanggap LT = SR - WT |
| :----- | :------------ | :------------- | :----------------------------------- | ------------------------- |
| A      | 0             | 4              | 4                                    | 4                         |
| B      | 1             | 7              | 11                                   | 10                        |
| C      | 3             | 3              | 14                                   | 11                        |
| D      | 7             | 8              | 22                                   | 15                        |
|        |               |                | Jumlah                               | 40                        |
|        |               |                | rerata = jumlah/banyak proses = 40/4 | 10                        |

![[Pasted image 20240422083038.png]]
- Short-Job-Next (SJN): 
	- Dikenal juga dengan proses terpendek dipertamakan (PTD)
	- Pendekatan terbaik untuk meminmalkan waktu tunggu
	- mudah diimplementasikan dalam sistem batch di mana waktu cpu yang diperlukan diketahui sebelumnya
	- tidak mungkin diterapkan dalam sistem interaktif dimana waktu CPU yang dibutuhkan tidak diketahui
	- prosesor harus tau sebelumnya berapa banyak waktu proses akan memakan waktu
Contoh algoritma 

| Nama Proses | Saat Tiba | Lama Proses |
| ----------: | --------: | ----------: |
|           A |         0 |           5 |
|           B |         3 |           7 |
|           C |         5 |           2 |
|           C |         5 |           2 |
|           D |         6 |           4 |

| Nama Proses | Saat Tiba | Lama Proses | Saat Mulai | Saat Rampung | Lama Tanggaop |
| ----------: | --------: | ----------: | ---------- | ------------ | ------------- |
|           A |         0 |           5 | 0          | 5            | 5             |
|           B |         3 |           7 | 11         | 18           | 15            |
|           C |         5 |           2 | 5          | 7            | 2             |
|           D |         6 |           4 | 7          | 11           | 5             |
|             |           |             |            | Jumlah 27    | 27            |
|             |           |             |            | Rerata       | 6,75          |
|             |           |             |            |              |               |

- Penjadwalan prioritas
	- Algoritma non-preemtive dan salah satu algoritma paling umum digunakan dalam sistem batch
	- setiap proses diberi prioritas
	- proses dengan prioritas yang sama dijalankan berdasarkan fcfs
	- prioirtas diputuskan berdasarkan persyaratan memori, eprsyaratan waktu, atau sumber daya lainnya
- Waktu Tersisa Ringkat
	- Waktu terpendek (SRT) adalah versi preemptive dari SJN 
	- Prosesor dialokasikan untuk pekerjaan yang paling dekat dengan penyelesaian tetapi dapat didahului oleh pekerjaan siap yang lebih baru dengan waktu penyelesaian yang lebih singkat 
	- tidak mungkin diterapkan dalam sistem interaktif dimana waktu CPU yang dibutuhkan tidak diketahui 
	- Ini sering digunakan dalam lingkungan batch dimana pekerjaan pendek perlu memberikan preferensi 
- Round Robin
- Antrian bertingkat 
