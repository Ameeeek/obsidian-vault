---
Source: https://www.youtube.com/watch?v=ptWgufbjURA&list=PLFIM0718LjIWiihbBIq-SWPU6b6x21Q_2&index=7
tags:
  - webdev
---
## Migration 
migrasi ini sama seperti version control e.g git tapi untuk database 
untuk membuat migrasi bisa dengan command 

> php artisan make:migration nama_tabel

untuk menambahkan data pada database, laravel menyediakan aplikasi bernama tinker, nah disini itu dia nanti bisa berinteraksi dengan database, daripada pakai gui app nya database atau cli nya bisa langsung pake tinker dan nda perlu bikin form lagi di laravel. 
Dia juga itu eloquent jadi ada mi method tertentu yang sudah tersedia

tinker bisa dipake dengan 
> php artisan tinker

dan ingat buat save() terlebih dahulu bair tersubmit i datanya

## Mass Assignment
dengan menggunakan fitur mass assignment, kita jadi tidak perlu lagi memasukkan satu persatu, data di tinker, tapi bisa langsung memasukkan semuanya seperti berikut 
```php
App\Models\post::create([
'title' => "judul Ketiga",
'excerpt' => "Lorem, ipsum dolor.",
'body' => "<p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
<p>Sit aliquid animi officiis? Nisi modi aliquam, ratione iste optio quam consectetur.</p>"
])
```

tapi perlu memrpotect field tertentu dulu, untuk memaksimalkan keamanan, karena apabila tidak memprotect field tertentu, maka akan muncul error 

```php

    /*dengan menggunakan kode dibawah ini, kita bisa melakukan mass assignment agar tidak ribet di tinkernya*/
    protected $fillable = ['title', 'excerpt', 'body'];
    /*dengan menggunakan guarded, semua yang ada dalam array itu boleh diisi, tapi diluar dari itu tidak boleh.*/
    protected $guarded = ['id'];
```

## Routes Model Binding 
daripada mengirim id dari suatu post kemudian melakukan query di controller, laravel menyediakan fitur bernama routes model binding, jadi simpelnya kita bsia langsung mengirim instance yang sesuai yang kita perlukan melalui routes. lebih lanjut baca [disini](https://laravel.com/docs/11.x/folio#route-model-binding) 
dengan menggunakan routes model binding ini membuat aplikasi jadi lebih aman.

### References