Deadlock dalam arti sebenarnya adalah kebuntuan, artinya dalam sistem operasi adalah kebuntuan proses, deadlock adalah kondisi dimana proses tidak berjalan lagi atau tidak komunikasi lagi antar poroses, disebabkan karena proses yang satu menunggu sumber daya yang sdang dipegang oleh proses lain. 

## Kondisi untuk terjadinya deadlock
- Mutual Ekslusif: Hanya ada satu proses yang boleh memakai sumber daya, dan proses lain yang ingin memakai sumber daya tersebut harus menunggu hingga sumber daya tadi dilepaskan atau tidak ada prosese yang memakai sumber daya tersebut 
- Memegang dan menunggu : proses yang sedang memakai sumber daya boleh meminta sumber daya lagi maksudnya menunggu hingga benar-benar sumber daya yang diminta tidak dipakai oleh proses lain, hal ini dapat menyebabkan kelaparan sumber daya sebab dapat saja sebuah proses tidak mendapat sumber daya dalam waktu yang sama
- tidak ada preemption : sumber daya yang ada pada sebuah proses tidak boleh diambil begitu saja oleh proses lainnya 
- circular wait : kondisi seperti rantai, yaitu sebuah proses membutuhkan sumber daya yang dipegang proses berikutnya

## Cara menanggulai deadlock
- mengabaikan masalah deadlock : berpura pura bahwa tidak akan ada  amsaalh apapun, seakan akan melakukan ssesuatu hal yang fatal, tetapi sistem operasi UNIX menanggulangi deadlock dengan cara ini dengan tidak mendeteksi deadlock dan membiarkannya secara otomatis mematikan program sehingga seakan akan tidak apapun. terdapat beberapa jalan untuk kembali dari deadlock : 
	- lewat preemtion 
	- lewat melacak kembali
	- lewat membunuh proses yang menyebabkan deadlock
- mendeteksi dan memperbaiki : caranya ialah mendeteksi jika terjadi deadlock pada suatu proses maka didteksi sistem mana yang terlibant didalamnya 
- penghidaran yang terus menerus dan pengalokasian yang baik dengan menggunakan protokol untuk memastikan sistem tidak pernah memasuki keadaan deadlock 
- pencegahan yang terstruktu bertentangan dengan empat kondisi yang terjadinya deadlock sehingga deadlock preventiopn sistem untuk memastikan bahwa salah satu kondisi yang penting tidak dapat menunggu

