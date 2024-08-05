---
Source: https://www.youtube.com/watch?v=HiHyeaY0NLE
tags:
  - CyberSecurity
---
# Binary data dan endianness
Dalam menyimpan data komputer, kita dapat langsung menyimpan data misal 31337, hexcode dari data tersebut ialah 31 33 33 37. akan tetapi, ada beberapa moment, data yang tersimpan di suatu file, saat kita extract hexcodenya, biner yang muncul tidak dalam direpresentasikan dalam bentuk hex akan tetapi dalam bentuk representasi endian. 

dalam komputasi, endian sendiri merupakan urutan dari bytes dari sebuah data yang di transmisikan pada memori. endian terbagi ata little endian dan big endian

![[Pasted image 20240803165201.png]]

dalam ctf, untuk mengekstrak endian, kita dapat menggunakan package bernama struct yang berguna untuk menginterpretasikan sebuah data ke dalam bentuk biner endian, menggunakan pack, dan unpack. untuk lebih lanjut silahkan baca disini [dokumentasi struct](https://docs.python.org/3/library/struct.html)
endianness, biasanya ada pada kategori, pwning, web exploitation, dan forensics

### References