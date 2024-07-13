---
tags:
  - study
  - College
  - Notes
cssclasses:
  - note
DosenPengajar: 
MataKuliah: Matematika Diskrit
Semester: "2"
---
# Matematika Diskrit
Matematika Diskrit adalah cabang ilmu matematika yang mengkaji objek objek yang bersifat diskrit atau diskontinu.

Pada kalkulus saya mempelajari simbol integral $\int$ 
sedangkan pada matematika diskrit, kita akan berfokus pada penggunaan simbol $\Sigma$ 
```
Fun fact:
Komputer digital beroperasi secara diskrit dengan unit terkecil yang disebut bit atau binary digit atau angka biner 

Struktur dan juga operasi komputer dapat dijelaskan dengan menggunakan konsep matematika diskrit
```

# Kenapa harus belajar matematika diskrit? 
1. Dengan belajar matematika diskrit mahasisa dapat berpikir secara matematis
	1. Dapat mengasah pemahaman argumen matematika
	2. mampu membuat argumen matematika
2. Matematika diskrit memberikan landasan sistematis untuk kuliah-kuliah lain di sistem informasi seperti
	1. algoritma, struktur data, basis data, otomata dan teori bahasa formal, jaringan komputer, keamanan komputer, sistem operasi dan sebagainya


## Kapan sesuatu di sebut diskrit
   Sesuatu dapat dikatakan sebagai diskrit apabila terdiri dari sejumlah berhingga elemen yang berbeda atau elemen elemennya tidak berasmbungan
![[Pasted image 20240221191902.png]]

# Bahan kajian matematika diskrit 
1. Logika dan penalaran
2. Teori himpunan 
3. Relasi 
4. Fungsi 
5. Aljabar Boolean 
6. Kombinatorial 
7. Teori Graf

![[Pasted image 20240221191957.png]]

![[Pasted image 20240221192007.png]]

# Referensi buku yang digunakan pada matematika diskrit
https://repository.bbg.ac.id/bitstream/602/1/Matematika_Diskrit.pdf

# Logika Dasar
## Apa itu logika? 
Logika = Penalaran/Reasoning = Cara berpikir 

Pengembangan alur berpikir berdasarkan akal budi dan bukan berdasarkan pengalaman ataupun perasaan

Logika Berfokus pada **hubungan** antara pernyataan-pernyataan

## Fungsi Logika Secara Umum 
- Membantu kita membedakan antara argumen yang valid dan tidak valid
- Membuktikan teorema-teorema dalam matematika 
# Bidang Ilmu Komputer 
- Bidang Pemrograman 
- Analisis kebenaran algoritma
-  Kecerdasan Buatan 
- Perancangan komputer 
- dsb
![[Pasted image 20240221192456.png]]

## Logika Proposisi 
**Proposisi** adalah kalimat deklaratif yang bernilai benar atau salah, tapi tidak dapat bernilai keduanya

contoh: 
1. Indonesia terletak di benua asia (benar)
2. Bilangan benar digunakan dalam sistem digital (benar)
3. Sistem analog lebih akurat dari sistem digital (salah) 
4. 2 + 2 = 4 (benar)
5. besok hari hujan (bukan sebuah proposisi, karena tidak dapat langsung ditetapkan kebenarannya, namun satu hal yang pasti yaitu tidak mungkin benar dan salah sekaligus)
kalimat yang bukan proposisi:
1. Astaga! mahal sekali harga laptop itu
2. Tolong ambilkan buku itu!
3. Apakah buku ini sangat bagus? 
4. Semoga hari ini tidak hujan 

kalimat keheranan, perintah, pertanyaan dan harapan bukan proposisi karena tidak dapat dinyatakan benar atau salah

Secara simbolik, biasanya dilambangkan dengan huruf kecil seperti p,q,r,s dsb 
contoh:

> p: 6 adalah bilangan genap 

p hanya  bertindak sebagai simbol, dan 6 adalah bilangan genap adalah proposisi 

## Latihan proposisi 
Di bawah ini manakah yang dapat dinyatakan sebagi sebuah proposisi dalam logika proposisi? 
	a. Jakarta adalah ibu kota indonesia (benar)
	b. Semarang adalah ibu kota provinsi jawa barat (salah)
	c. 2 + 3 = 5 (benar)
	d. 4 + x = 12 (tidak dapat ditarik kesimpulan, karena nilai x masih dapat bernilai apa saja, tapi yang pasti hanya bisa benar atau salah)
	e. Jawablah pertanyaan ini (bukan proposisi, karena merupakan kalimat perintah)
	d. Jam berapa ini? (merupakan kalimat tanya)

# Proposisi Gabungan 
Beberapa pernyataan dapat digabungkan dengan menggunakan kata penghubung dan, atau, tidak/bukan serta variatifnya yang selanjutnya disebut pernyataan gabungan atau compound statement. 

Macam-macam pernyataan gabungan: 
1. Konjungsi 
2. Disjungsi 
3. Negasi 
4. Disjungsi Ekslusif 

## Disjungsi 
Konjungsi adalah 2 atau lebih pernyataan yang digabung menggunakan "And"
Notai konjungsi
$p \land q$ 
dimana p dan q adalah pernyataan 

tabel kebenaran 

| p     | q     | $p\land q$     |
|-----:|-----:|-----:|
| T     | T     | T     |
| T     | F     | F     |
| F     | F     | F     |
## Disjungsi 
Disjungsi adalah 2 atau lebih pernyataan yang menggunakan "OR"
Notasi Disjungsi 
$p\lor q$ 

tabel kebenaran 


| p     | q     | $p \lor q$     |
|-----:|-----:|-----:|
| F     | T     | T     |
| T     | F     | T     |
| F     | F     | F     |

## Negasi 
Negasi adalah pernyataan yang meniadakan pernyataan yang ada, dapat digunaka ndengan menyisipkan kata "tidak/bukan" pada pernyataan positif atau sebaliknya, menghapus kata "tidak/bukan" pada pernyataan negatif. 

Notasi negasi 
~p


| p     | ~p     |
|-----:|-----:|
| T     | F     |
| F     | T     |

## Disjungsi Eksklusif
Cara kedua menggunakan **atau** yang artinya hubungan antara dua proposisi dapat dikatakan benar jika hanya salah satu dari proposisi benar tapi bukan keduanya

Notasi Disjungsi Ekslusif
$p \oplus q$ atau p xor q atau $p \veebar q$

# Tautologi dan Kontradiksi 
Proposisi dapat dipandang dari nilai kebenarannya, dapat dibagi menjadi 2 yaitu tautologi dan kontradiksi

## Tautologi 
Proposisi yang selalu benar apapun pernyataannya

Notasi Tautologi 
$p \land ~p$ 

## Kontradiksi
Proposisi yang selalu salah apapun pernyataannya 

Notasi Kontradiksi 
$p \lor q$ 