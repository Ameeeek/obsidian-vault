---
Source: https://www.youtube.com/watch?v=ptWgufbjURA&list=PLFIM0718LjIWiihbBIq-SWPU6b6x21Q_2&index=5
tags:
  - webdev
---
Dalam laravel, dia juga menginclude eloquent ORM (Object Relational Mapper) dimana tersedia sebuah class yang akan berinteraksi dengan table pada database

dengan command 
```
php artisan make:model nama_model
```
akan otomatis meng generate sebuah model

## collection 
dengan membungkus sebuah array menjadi dengan collection, ini memberikan sebuah array sekumpulan method yang mempermudah, untuk lebih lanjut silahkan baca lebih lengkap mengenai method apa saja yang tersedia silahkan baca [disini](https://laravel.com/docs/11.x/collections#available-methods)

## controller 
daripada menghandle semua logic pada routes dengan menggunakan disclosure atau anonymous function, dapat dipermudah dengan menggunakan controller agar di handle disana. 

lebih lanjtu mengenai controller dapat dibaca [disini](https://laravel.com/docs/11.x/controllers#main-content)

logic yang dihandle pada disclosure function
```php
Route::get('/blog', function(){
	return view("posts", [
        "title" => "posts",
        "posts" => post::all()
    ]);
})
```          

untuk membuat controller cukup dengan command berikut 
> php artisan make:controller

### References