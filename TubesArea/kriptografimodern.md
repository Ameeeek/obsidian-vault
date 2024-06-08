# Pendahuluan 
- Kriptografi modern adalah era kriptografi setelah penemuan komputer digital
- pengembangan teknologi komputer digital membuat ilmu kriptografi berkembangan dengan pesat
- komputer digital merepresentasikan data dan informasi dalam biner
- Algoritma kriptografi modern beroperasi dalam mode bit ataau byte (bandingkan dengan kriptografi klasik beropasi dalam mode karakter)
    Kunci, plainteks, cipherteks diproses dalam rangkaian bit/byte 
    operasi xor paling banyak digunakan di dalam algoritmanya
- meskipun disebut kriptografi modern, namun algoritmanya tetap menggunakan dua
  teknik dasar-dasar di dalam kriptografi klasik: teknik subtitusi dan teknik transposisi,
- tetapi operasinya dibuat lebih kompleks agar lebih dikript 
- selain teknik subtitusi dan transposisi, ada juga teknik lain seperti rotasi,
  kompresi, ekspansi, penjumlahan module, dan lain-lain
- Kriptografi modern melahirkan konsep baru seperti algoritma kunci-publik,
kunci simetris, fungsi hash, protokol kriptografi, tanda-tangan digital, generator bilangan acak, skema pembagian kunci dsb 

![DiagramBlokKriptografiModern.png](DiagramBlokKriptografiModern.png)

# Bit, Byte, dan Kode Heksadesimal
- Pesan di dalam cipher modern dienkripsi bit-per-bit atau byte-per-byte, atau
dalam kelompok bit. 1 byte = 8 bit. 
- Pada beberapa algoritma kriptografi, pesan direpresentasikan dalam kode
heksadesimal. 1 kode hex = 4 bit 
![hex.png](hex.png)
contoh: Pesan 100111010110 dalam kode hex dengan cara membagi pesan menjadi blok 4-bit: 
1001 1101 0110 = 9D6 
Jika pesan diproses dalam kelompok bit, maka rangkaian bit pesan dibagi menjadi blok-blok bit berukuran sama. 
Contoh: Plainteks 100111010110001011100001 bila dibagi menjadi blok 8-bit 
10011101 01100010 11100001 
atau dalam kode heksadesimal menjadi : 
9E 62 E12
- padding bits: bit-bit tambahan jika ukuran blok terakhir tidak mencukup
panjang blok 
- contoh: Plainteks 100111010110 
  bila dibagi menjadi blok 5-bit: 
  10011 10101 00010 
padding bits mengakibatkan ukuran cipherteks sedikit lebih besar daripada ukuran plainteks semula. 

dalam operasi kriptografi, operasi yang paling sering digunakan itu adalah operasi XOR
# Kategori cipher berbasis bit 
- Cipher Alir (Stream Cipher)
  - beroperasi pada bit tunggal atau byte tunggal
  - enkripsi/dekripsi pesan secara bit
- Cipher Blok (Block Cipher)
  - beroperasi pada blok bit atau blok byte (contoh: 64-bit/blok = 8
  karakter/blok)
  - enkripsi/dekripsi pesan secara blok per blok bit atau blok per blok byte

![diagramAlirSimetrikCiphers.png](diagramAlirSimetrikCiphers.png)
