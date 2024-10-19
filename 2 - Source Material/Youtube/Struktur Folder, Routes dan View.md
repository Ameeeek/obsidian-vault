---
Source: https://www.youtube.com/watch?v=u7zS2XpMpsc&list=PLFIM0718LjIWiihbBIq-SWPU6b6x21Q_2&index=3
tags:
  - webdev
---
Struktur folder pada laravel menggunakan MVC yaitu model view controller

untuk folder view, disitu ada semua file yang akan dikompilasi disitu mi keliatan semua folder yang muncul

untuk folder routes, disitu nanti semua penjaluran pada web kayak url, endpoint API dll

untuk folder public, tempatnya disitu ditaro file statis yang akan dipake kayak css , js, dan image

lebih lanjut bisa baca [disini](https://laravel.com/docs/11.x/structure#main-content)


 >Setiap url yang dimasukkan ke file apapun itu, dia akan relative pointing ke direktori public
 
 
## Routing 
```php
Route::get("/", function(){
	return view("welcome")
})
```

get itu routing basic, info lebih lanjut [disini](https://laravel.com/docs/11.x/routing#main-content)

## Mengirim data melalui routes
```php
Route::get("/about", function(){
	return view("welcome", [
		"name" => "Amek" // gunakan associative array, untuk memanggil cuku gunakan key dari value sebagai variable
	])
})
```

```php
<body>
	<h2><?= $name ?></h2> // sintaks php
	<h3>{{$name}} </h3> // sintaks dengan blade, menggunakan sintaks ini akan memprevent, serangan xss kraena diconvert menjadi htmlspecialchars
<body>
```

### References