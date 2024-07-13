---
Ticket: "[[Go]]"
---
# Package
Sama seperti C, golang mengorganisir setiap function yang diperlukan pada sebuah Package. sehingga saat sebuah package di import, setiap entitas baik itu fungsi, variabel dan class yang dapat dipanggil atau diakses hanya entitas yang diawali dengan huruf kapital. Thus, naming convention yang widely used in golang is PascalCase sedangkan untuk identifier pada package dapat menggunakan camelCase

# Variables 
Go sebagai bahasa yang statis, mewajibkan programmer untuk menentukan tipe data sebuah variabel seperti berikut 
```go
var explicit int // di tentukan tipe nya secara eksplisit
```
meskipun begitu, golang juga memiliki initializer yang memungkinkan compiler untuk menyesuaikan tipe data variabel sesuai dengan isinya. 
```go
implicit := 10 // di tentukan secara implisit
```
selain itu, sebuah variabel tidak bisa di reassign tipe nya, tapi nilainya ya bisa
```go
nilai := 10
nilai = "halo" // ini akan menyebabkan error karena tipe data yang digunakan tidak sesuai dengan tipe data awal saat inisialisasi
```

# Constants 
konsepnya sama seperti bahasa pemrograman yang lain, variabel dengan nilai konstan tidak bisa dirubah nilainya 

# Functions 
Ini juga sama seperti bahasa pemrograman lainnya, fungsi pada golang menerima ada atau tidak ada parameter sama sekali, tetapi parameter harus di tulis tipenya secara spesifik, dan tidak ada inference seperti di python atau javascript

```go
package greeting 
// a good function 
func hello (name string) string{
	return "hi " + name 
}
// a bad function 
func hello (name){
	return "hi " + name
}
```

# Arithmetic Operations 
Operasi aritmatika di Golang juga tidak berbeda jauh dengan bahasa pemrograman lainnya, saam sama punya +, -, *, % (di go ini itu jatuhnya operasi remainder, dan bukan modulo, untuk modulo dia terletak di package main/math)

