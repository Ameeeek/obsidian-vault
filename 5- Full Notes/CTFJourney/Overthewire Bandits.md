---
Platform: Overthewire
category: idk
---
Level 1 : Pw ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If didapat pas cat readme pas login ssh
level 2 : pw 263JGJPfgU6LtdEvgfWU1XP5yac29mFx didapat pas more - pas login ssh pake user bandit 1
level 2 : pw MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx didapat pas cat 'spaces in this file name' pas login ss pake user bandit 2 
level 3 : pw 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ didapat pas cat ... Hiding-From-You pas login pake user bandit3
leve 4 : pw 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw didapat pas cat file nya pas login pake user bandit4 
level 5 : pw HWasnPhtq9AVKe0dmk45nxy20cvUa6EG didapat pas cat filenya yang di maybehere07 yang .file2 pas login pake user bandit5
level 7 : pw HWasnPhtq9AVKe0dmk45nxy20cvUa6EG didapat pas cat filenya /var/lib/dpkg/info/bandit7.password, but how ? jadi disini level e belajar ka tentang penggunaan command find, karena ternyata command find ada argumennya -user dan -group untuk mengecek apakah suatu file itu belongs to a user or a group, terus ada juga argumen -type terus bisa dispesifikkan untuk cari suatu file, terus -size untuk tulis spesifikkan ukuran suatu file, jadi commandnya itu find / -type f -user bandit7 -group bandit6 -size 33c, tapi ternyata dengan itu masih terlalu bingung ki karena banyak permission denied errornya, makanya ditambahin diakhir perintah 2>/dev/null untuk hide i error messagenya,