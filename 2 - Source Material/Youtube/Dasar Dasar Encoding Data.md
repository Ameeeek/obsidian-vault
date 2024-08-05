---
Source: https://www.youtube.com/watch?v=6rVPJnf7Nng
tags:
  - CyberSecurity
---
# Dasar Dasar Encoding Data

seperti  yang diketahui, data terdiri dari masing masing byte, yang dimana 1 byte itu terdiri dari 8 bit. 

setiap data kita bisa melakukan ekstraksi kode hex, untuk mengecek representasi, hex, biner, dan ascii dari suatu file.

misal dari sebuah file text, biasanya, sebuah file akan memiliki ukuran n byte + 1 byte, 1 byte ini darimana? 1 bytenya berasal dari newline, karena dia otomatis menambahkan sebuah newline 

![[Pasted image 20240803171008.png]]

dari gambar diatas, dapat dilihat, 00000000 adalah offset pada memori, 6861 6c6f 0a adalah representasi hexadesimalnya, dan 0a adalah newline, halo adalah representasi asciinya

perlu diketahui juga bahwa, tidak semua hexcode itu dapat di print, rentang dari 0x00 - 0x20 adalah hexcode yang tidak bisa di print 0x70 - 0xff juga tidak bisa diprint, jika tetap dipaksakan, maka akan muncul karakter yang tidak dapat diketahui 

tipe tipe encoding seperti ini ada berbagai macam, kita juga terkadang menemukan encoding hexcode ini dalam bentuk url encoding, url encoding memiliki prefix % dan bukan 0x

encoding yang biasa digunakan juga adalah base64 encoding, dimana karakteristik dari base 64 adalah campuran huruf besar dan diakhiri dengan sama dengan yang merupakan padding/newline

### References