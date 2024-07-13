---
tags:
  - study
  - College
  - Notes
cssclasses:
  - note
DosenPengajar: ibu hera
MataKuliah: Struktur Data
Semester: "2"
---
# Algoritma
Suatu instruksi yang harus diikuti oleh komputer untuk memecahkan suatu masalah
### Perlu diingat: 
Algoritma tidak terikat pada programming language atau bahkan pardigma pemrograman

# Time Complexity
Pengukuran lamanya code dieksekusi (run time) disebut sebagai time complexity 

# Space Complexity 
Dengan mempertimbangkan ruang memori pada komputer, pengukuran yang digunakan adalah space complexity

# Analisis algoritma, kenapa perlu? 
- Perlu diketahui berapa banyak resource (time dan space) yang diperlukan oleh sebuah algoritma 
- Menemukan teknik-teknik untuk mengurangi waktu yang dibutuhkan oleh sebuah algoritma

# Apa itu analisis Algoritma
- mengukur jumlah sumber daya yang diperlukan oleh sebuah algoritma
- waktu yang diperlukan (running time) oleh sebuah algoritma cenderung tergantung pada jumlah input yang diproses 
	- running time dari sebuah algoritma adalah fungsi dar jumlah inputnya
- Ada algoritma yang running timenya tergantung pada jumlah outputnya 
- selalu tidak terikat pada platform (mesin + os), bahasa pemrograman, kualitas kompilator atau bahkan paradigma pemrograman seperti procedural atau object-oriented
# Bagaimana cara melakukan analisis algoritma
- Bagaimana jiak kita menggunakan jam ? 
	- Jumlah waktu yang kita gunakan bervariasi tergantung pada beberapa faktor lain: kecepatan mesin, sistem operasi, kualitas kompiler, dan bahasa pemrograman
	- sehingga kurang  memberikan gambaran yang tepat tentang algoritma
- Notasi O digunakan sebagai bahasa untuk membahas sebuah efisiensi dari sebuah algoritma seperti: Log n, linear, n log n, n2, n3, ...
- Dari hasil run-time, dapat kita buat grafik dari waktu eksekusi dan jumlah data

ketika berurusan dengan waktu, kompleksitas, dan kompleksitas ruang, ada tiga huruf yunani yang biasa digunakan yaitu, 
						$\omega = omega$  $\theta = theta$ $O = omicron$   
bayangkan ketika mencari sebuah angka yang ada didalam sebuah list (1-7), berapa banyak waktu yang dibutuhkan

1, merupakan waktu terbaik dalam menjalankan algoritma (base-case)
4, waktu rata-rata dalam menjalankan algoritma (average-case)
7, waktu terburuk dalam menjalankan algoritma (worst-case)

![[Pasted image 20240309000243.png]]

disaat kita berbicara tentang Big-O Notation, kita akan berfokus pada tipe worst case

# Big-O
Bahasa dan metik yang digunakan untuk menggambarkan efisiensi algoritma
seberapa efisien algoritma yang dibuat? 

1. Kompleksiti berdasarkan pada seberapa banyak input, N 
2. tidak memperdulikan mesin
3. langkah dasar dari komputer
4. waktu dan ruang sangat berpengaruh

```python
def print_items(n): # algoritmanya itu sequential output artinya, steps yang diperlukan untuk menyelsaikan algoritma diatas sesuai memiliki jumlah yang sama dengan loopingannya, jika loopingnya berulang sebanyak 10 kali maka langkah yang diperlukan untuk sampai ke n yaitu 10 algoritma ini lebih dikenal dengan O(n) - linear
	for i in range(n):
		print(n)
print_items(10)
```

```python
def print_items(n):
	for i in range (n):
		print(i)
	for j in range(n):
		print(j)
print_items(10)

# algoritma diatas terjadi dua proses linear maka n + n = 2n, sehingga algoritma ini lebnih dikenal dengan O(n) - drop constant
```

``` python
def print_items(n):
	for i in range(n):
		 for j in range(n):
			  print(i,j)
print_items(10)

# algoritma ini lebih dikenal dengan O^2 - squared, dimana terjadi n * n proses sehingga jadi O(n2)
```
``
```python
def add_items(n):
	return n+n
add_items(10)

# algoritma diatas dikenal dengan O(1) karena akan menampilkan output hanya satu proses, karena hanya terdapat satu proses maka disebut O(1) - constant time
```

# Bagaimana dengan kasus logaritmik? 
Logaritma adalah suatu invers atau kebalikan dari pemangkatan (eksponen) yang digunakan untuk menentukan besar pangkat dari suatu bilangan pokok.

![[Pasted image 20240309001146.png]]
## contoh kasus: 
![[Pasted image 20240309001213.png]]
```python
def logN(n):
	n = n//2
	if n > 0: return logN(n)
logN(8)
print(result)
```
![[Pasted image 20240309001314.png]]
![[Pasted image 20240309001343.png]]
![[Pasted image 20240309001352.png]]
![[Pasted image 20240309001413.png]]
![[Pasted image 20240309001604.png]]

# Dominant Term
- mengapa hanya suku yang memiliki pangkat tertinggi/dominan saja yang diperhatikan ? untuk n yang besar, suku dominan lebih mengindikasikan perilaku dari algoritma 
- untuk n yang kecil, suku dominan tidak selalu mengindikasikan perilakunya , tetapi program dengan input kecil umumnya berjalan sangat cepat sehingga kita tidak perlu perhatikan. 

```python
def print_items(a,b):
	for i in range (a):
		print(i)
	for j in range (b):
		print(j)
print_items(10,5)

# contoh diatas tidak termasuk O(2n) karena a tidak sama dengan b sehingga a + b jadi big o notation yang tepat ialah O(a+b)
```

```python
def print_items(a,b):
	for i i range (a):
		for j in (b):
			print(i,j)
print_items(10,5)

# contoh diatas juga tidak dapat disebt sebagai O(n^2) karena a tidak sama dengan b sehingga a * b dan menjadi O(ab)
```