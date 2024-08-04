---
Platform: Gemastik2024
Category: Forensics
---
# Foren - baby structured
Diberikan sebuah file bernama zhezhi___ tanpa ekstensi, apapun saat ku cek data hexnya, ternyata merupakan file .png, dengan pngcheck saya coba untuk menganalisis lebih jauh file ini

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcf-GCUI_K6QyZSYkl8Q_L9kbFM9zkZCLd6FJuEAb2-glIFlkFyksfPjIfekANkEmK_2D7kzILgvIRBFtGHzy0BjRg2Glqj5Ji9ev2CIu13kUtaR2PSd-SIZWvOIJelZPf8yPmFB-peZXCOdKho50z2kvQ?key=AWPBkKEXxqQVaqwfeIovyw)

ternyata, ditemukan crc error, maka dari itu itu kode hexnya segera saya perbaiki dengan hexedit, kemudian dihasilkan gambar berikut.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcma1toXG7GRiCWU_3CCQNsag2lD3sAxZD0cRsy-txNzrZaQnwxzZkmUwxUsukaCdapdqhyYJPBg3xFx5LhuLvzKd6VetL-6Hlx4BSdrWzSlc2pXxlM2hV1jGGYlRPwLjPY698bEv3KXk0_EpGQRiffqMxi?key=AWPBkKEXxqQVaqwfeIovyw)

karena dari soal diberikan clue mengenai gambar yang di crop, maka saya langsung mengedit hex dari gambar tersebut, dan merubah heightnya menjadi lebih besar. mengingat ekstensi filenya adalah png, ini memberikan saya akses untuk mengedit panjang atau height dari gambar ini langsung melalui hexcode. dengan sedikit membaca mengenai struktur dari file png [https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73](https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73) saya dapat merubah panjangnya sehingga saya gambarnya dapat menjadi seperti berikut

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdo028yn-DuwEodBNOodPVdYQY1RJZ7nxRWSkg5-U4YSISdqxp8t5zeLsMCmstGMHddxOnakpVcDq58fnbV7SL0lvvzLYhbNtFI1jPrs6mtvdZDcIeQCn9h2VDul7hRIPBaPI53XsNlV66yhkaTgAaWpSI?key=AWPBkKEXxqQVaqwfeIovyw)

flag : gemastik{g0t_cr0pped_by_structur3}






### References 