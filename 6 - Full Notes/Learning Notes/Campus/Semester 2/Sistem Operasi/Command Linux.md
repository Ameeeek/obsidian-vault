********### Melihat identitas diri 
$ id 
### Melihat tanggal dan kalender 
$ date 
$ cal -y 

### Melihat identitas mesin 
$ hostname 
$ uname 
$ uname -a 
### mengetahui siapa yang sedang aktif 
$ w 
$ who 
$ whoami

### mengetahui informasi finger
$ chfn <user/>

### melihat informasi finger
$ finger
$ finger <user/>

### menggunakn manual 
$ man ls 
$ man man 
$ man -k file 
$ man 5 passwd

### menghapus layar 
$ clear

### mencari perintah yang deskripsinya mengandung kata yang dicari
$ apropos date 
$ apropos mail
$ apropos telnet

### mencari perintah yang tepat sama dengan kunci yang dicari 
$ whatis date

### manipulasi file dari direktori 
$ ls 
$ ls -l (melihat semua file lengkap)
$ ls -a (melihat semua file atau direktori yang tersembunyi)
$ ls -f (melihat semua file atau direktori tanpa proses sorting)
$ ls /usr (melihat isi suatu direktori)
$ ls / (menampilkan isi direktori root)
$ ls -F /etc (menampilkan semua file atau direktori dengan menandai : tanda (/) untuk direktori, tanda asterisk (*\) untuk file yang bersifat excutable, tanda (@) untuk file symbolic link, tanda (=) untuk socket, tanda (%) untuk whitout dan tanda (|) untuk FIFO)
$ ls -l /etc
$ ls -R /usr (menampilkan semua file dan isi direktori. Argumen ini akan menyebabkan proses berjalan agak lama, apabila proses akan dihentikan dapat menggunakan ctrl + c)

### melihat tipe file 
$ file 
$ file *
$ file /bin/ls

### menyalin file 
$ cp folder file (menyali suatu file ke direktori tertentu, tambahkan -i untuk pertanyaan interaktif)

### mengkopi direktori
$ mkdir file 
$ cp folder file 

### melihat isi file 
$ cat file 

### memindahkan file 
$ mv folder file 

### menghapus file 
$ rm file 
$ rm direktori -r (menghapus direktori yang memiliki file didalamnya)

### mencari kata atau kalimat dalam file 
$ grep "text" file

### menambahkan pengguna
sudo adduser <user.> 

### memberikan hak akses ke pengguna 
$ sudo nano /etc/group
lalu cari sudo, dan tambahkan nama user

### pindah pengguna 
$ su <user.>