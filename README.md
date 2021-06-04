# TugasAkhir-Parktikum-Metnum
Nama Anggota Kelompok 5: 
1. Muhammad Athala Haykal	26050119130123
2. Ebenezer M.D			26050119130119
3. Farhan Satria		26050119130109
4. Kurnia Fajar Hidayat		26050119130104
5. Achmad Agung B		26050119130103
6. Syifa Saidatul Hasanah	26050119130101
7. Rina Hazrina Nusratina	26050119130098
8. Nurul Maratus Sholihah	26050118120035
9. Fressan Patrick		26050119130097
10. Muhammad Nur Alfajrin	26050119130096
11. Rayen Hanjaya 		26050119130094
12. Afisha Tiara Arbain		26050119130091

# Panduan dan Penjelasan Terkait Program Penyelesaian Masalah Metode Numerik
Berikut ini adalah beberapa permasalahan dalam metode numerik yang dapat diselesaikan menggunakan program tersebut, antara lain :
1. Akar-akar persamaan.
2. Sistem persamaan linier dan matriks.
3. Integrasi numerik
4. Persamaan diferensial biasa.

# Selanjutnya, kita akan membahas secara sekilas terkait beberapa permasalahan metode numerik di atas

## 1. Akar-Akar Persamaan
Dalam perhitungan numerik, persamaan polinomial sangat sulit untuk diselesaikan secara eksplisit. Dalam hal ini, metode yang digunakan untuk menyelesaikan persamaan tersebut adalah metode iterasi (pengulangan). Dengan demikian, setiap persamaan akan menghasilkan nilai yang lebih teliti dari perkiraan sebelumnya.Di lain pihak, nilai tolerasi kesalahan dapat dipilih sesuai keinginan. Selain itu, solusi dari metode numerik juga selalu menghasilkan angka. Ada beberapa metode untuk menyelesaikan masalah akar-akar persamaan. Contohnya, yaitu:

### * Metode Setengah Interval
Pada dasarnya, metode ini merupakan metode yang sederhana di antara metode-metode lainnya. Namun, metode ini tetap banyak digunakan karena hasilnya tidak memiliki banyak error. Artinya, metode ini selalu menemukan hasil walaupun caranya penyelesaiannya sederhana. Kelebihan dari metode ini adalah selalu menemukan solusi yang dicari (konvergen). Di lain pihak, kekurangannya adalah jika ada beberapa akar pada interval yang diberikan, hanya satu akar saja yang dapat ditemukan. Selain itu, proses iterasinya cukup lama.

### * Metode Interpolasi Linier
Metode ini dapat dikatakan mirip dengan metode setengah interval. Hal yang serupa terletak pada dua harga taksiran awal pada awal pengurungan akar persamaan. Perbedaannya terletak pada penyelesaiannya yang menggunakan interpolasi linier. Interpolasi linier dilakukan melalui dua titik pertama dengan garis interpolasi memotong sumbu x dan dititik perpotongan tersebut didapatkan pendekatan akar yang pertama.

### * Metode Newton-Rhapson
Metode Newton-Rhapson merupakan metode yang paling sering digunakan di antara metode pencarian akar persamaan yang lain. Metode ini dapat dikatakan sederhana, tetapi handal dalam menyelesaikan masalah akar persamaan nonlinier. Kelebihan metode ini adalah nilai konvergensi yang dihasilkan cukup cepat. Namun, kekurangannya adalah tidak selalu menemukan akar (divergen), sulit dalam mencari f(xn), dan penetapan harga (xn) yang sulit.

### * Metode Secant
Metode ini merupakan metode Newton-Rhapson yang turunan pertama fungsinya didekati dengan ungkapan yang berbeda. 

### * Metode Iterasi
Metode ini disebut sebagai metode tidak langsung (pengulangan/iteratif). Persamaan akan mengalami penyelesaian yang diulang-ulang hingga mencapai keadaan konvergen. Satu – satunya kelebihan dari penggunaan metode iterasi adalah sedikitnya memori computer yang digunakan sebagai akibat dari algoritma yang mendesain agar komputer hanya menyimpan koefisien – koefisien yang tidak nol. Di lain pihak, kekurangan dari metode ini adalah jika sistem persamaan tidak berada pada kondisi yang kondusif, konvergensi dari suatu sistem persamaan tidak dapat terjamin.


## 2. Sistem Persaman Linier dan Matriks
Sistem persamaan linier (SPL) adalah sistem operasi matematis yang terdiri dari dua atau lebih persamaan linier. Ada beberapa metode yang digunakan dalam memecahkan masalah numerik ini, yaitu:
   
### * Notasi Matriks
Matriks adalah himpunan skalar (bilangan riil atau kompleks) yang disusun atau dijajarkan secara empat persegi panjang menurut baris-baris dan kolom-kolom. Matriks adalah jajaran elemen (berupa bilangan) berbentuk empat persegi panjang. Matriks adalah susunan angka – angka (sering disebut elemen – elemen) yang diatur menurut basis dan kolom, berbentuk persegi panjang atau persegi dan ditulis diantara dua tanda kurung yaitu ( ) atau [ ]. Notasi matriks dinyatakan dalam huruf kapital.
     
### * Metode Eliminasi Gauss
Eliminasi Gauss adalah suatu cara mengoperasikan nilai-nilai di dalam matriks menjadi matriks yang lebih sederhana dan banyak digunakan dalam penyelesaian sistem persamaan linier. Prosedur penyelesaian dari metode ini adalah dengan melakukan operasi baris menjadi matriks eselon-baris. Metode ini mengubah persamaan linear tersebut ke dalam matriks augmentasi dan mengoperasikannya. Metode eliminasi gauss termasuk dalam metode penyelesaian persamaan linear dengan cara langsung. Inti dari metode ini adalah membawa persamaan kedalam bentuk matriks dan menyederhanakan matriks menjadi bentuk segitiga atas. Setelah mendapat bentuk matriks tersebut dilakukan subtitusi balik untuk mendapat nilai dari akar persamaan tadi.
     
### * Metode Eliminasi Gauss-Jordan
Eliminasi Gauss-Jordan adalah pengembangan dari eliminasi Gauss yang hasilnya lebih sederhana lagi. Caranya adalah dengan meneruskan operasi baris dari eliminasi Gauss sehingga menghasilkan matriks yang Eselon-baris. Ini juga dapat digunakan sebagai salah satu metode penyelesaian persamaan linear dengan menggunakan matriks. Metode ini digunakan untuk mencari invers dari sebuah matriks.Prosedur umum untuk metode eliminasi Gauss-Jordan ini adalah:
1. Ubah sistem persamaan linier yang ingin dihitung menjadi matriks augmentasi.
2. Lakukan operasi baris elementer pada matriks augmentasi (A|b) untuk mengubah matriks A menjadi dalam bentuk baris eselon yang tereduksi

### * Metode Iterasi Gauss-Seidel
Metode iterasi Gauss-Seidel adalah metode yang menggunakan proses iterasi hingga diperoleh nilai-nilai yang berubah-ubah dan akhirnya relatif konstan. Metode iterasi GaussSeidel dikembangkan dari gagasan metode iterasi pada solusi persamaan tak linier. Metode eliminasi gauss-seidel digunakan untuk menyelesaikan SPL yang berukuran kecil karena metode ini lebih efisien. Dengan metode iterasi Gauss-Seidel toleransi pembulatan dapat diperkecil karena iterasi dapat diteruskan sampai seteliti mungkin sesuai dengan batas toleransi yang diinginkan. Kelemahan dari metode ini adalah masalah pivot (titik tengah) yang harus benar–benar diperhatikan, karena penyusunan yang salah akan menyebabkan iterasi menjadi divergen dan tidak diperoleh hasil yang benar. 

### * Metode Iterasi Jacobian
Metode iterasi Jacobi ini digunakan untuk menyelesaikan persamaan linier yang proporsi koefisien nol nya besar. Metode ini ditemukan olek matematikawan yang berasal dari Jerman, Carl Gustav Jakob Jacobi. Penemuan ini diperkirakan pada tahun 1800-an. Iterasi dapat diartikan sebagai suatu proses atau metode yang digunakan secara berulang-ulang (pengulangan) dalam menyelesaikan suatu permasalahan matematika. Keuntungan metode ini adalah langkah penyelesaiannya yang sederhana, sedangkan kelemahannya adalah proses iterasinya lambat. 


## 3. Integrasi Numerik
Integrasi numerik merupakan cara alternatif dalam mengintegrasikan suatu persamaan, terutama integrasi analitis. Integrasi analitis merupakan cara integrasi yang rumit, terutama pada persamaan yang kompleks dan sulit sehingga memakan waktu lama dalam penyelesaiannya. Dalam hal ini, integrasi numerik menjadi bagian penting dari masalah sains dan teknik. Hal itu didukung oleh masalah dalam bidang sains yang ditemukan dalam ungkapan integral matematis yang sulit diselesaikan secara analitis. Dengan demikian, kehadiran analisis numerik menjadi bagian penting dalam pendekatan analitis. Di samping itu, beberapa metode yang digunakan dalam penyelesaian integrasi numerik antara lain:

### * Metode Trapesium Satu Pias
Metode trapesium merupakan metode pendekatan integral numerik dengan persamaan polinomial order satu. Dalam metode ini kurve lengkung dari fungsi f (x) digantikan oleh garis lurus. Seperti pada Gambar 1, luasan bidang di bawah fungsi f (x) antara nilai x = a dan nilai x = bdidekati oleh luas satu trapesium yang terbentuk oleh garis lurus yang menghubungkan f(a) dan f(b) dan sumbu-x serta antara x = a dan x = b. Pendekatan dilakukan dengan satu pias (trapesium).

### * Metode Trapesium Banyak Pias
Untuk mengurangi kesalahan yang terjadi maka kurva lengkung didekati oleh sejumlah garis lurus, sehingga terbentuk banyak pias. Luas bidang adalah jumlah dari luas beberapa pias tersebut. Semakin kecil pias yang digunakan, hasil yang didapat menjadi semakin teliti. Metode trapesium dapat digunakan untuk integral suatu fungsi yang diberikan dalam bentuk numerik pada interval diskret. Koreksi pada ujung-ujungnya dapat didekati dengan mengganti diferensial f '(a) dan f '(b) dengan diferensial beda hingga.

### * Metode Simpson 1/3
Di dalam aturan Simpson 1/3 digunakan polinomial order dua (persamaan parabola) yang melalui titik f(xi–1), f(xi) dan f(xi+1) untuk mendekati fungsi. Rumus Simpson dapat diturunkan berdasarkan deret Taylor.

### * Metode Simpson 3/8
Metode Simpson 3/8 diturunkan dengan menggunakan persamaan polinomial order tiga yang melalui empat titik. Metode Simpson 1/3 biasanya lebih disukai karena mencapai ketelitian order tiga dan hanya memerlukan tiga titik, dibandingkan metode Simpson 3/8 yang membutuhkan empat titik. Dalam pemakaian banyak pias, metode Simpson 1/3 hanya berlaku untuk jumlah pias genap. Apabila dikehendaki jumlah pias ganjil, maka dapat digunakan metode trapesium. Tetapi metode ini tidak begitu baik karena adanya kesalahan yang cukup besar. Untuk itu kedua metode dapat digabung, yaitu sejumlah genap pias digunakan metode Simpson 1/3 sedang 3 pias sisanya digunakan metodeSimpson 3/8

## 4. Persamaan Diferensial Biasa
Pada umumnya, persamaan disebut sebagai persamaan diferensial jika di dalam persamaan tersebut ada turunan seperti dy/dt atau dy/dx. Pada bentuk diferensial dy/dx, x adalah variabel bebas dan y adalah variabel tetap. Persamaan ini biasanya digunakan dalam memahami fenomena alam. Selanjutnya, jika fenomena tersebut ingin diprediksi, kita dapat menggunakan bentuk persamaan ini. Dengan demikian, dapat dikatakan bahwa persamaan diferensial sangat berpengaruh dalam bidang sains. Di dalam persamaan diferensial biasa (ordinary differential equations), persamaan hanya memiliki satut variabel bebas. Ada beberapa metode yanag digunakan dalam menyelesaikan persamaan diferensial biasa menggunakan metode numerik ini, yaitu :

### * Metode Satu Langkah
Metode satu langkah terdiri dari metode Euler, metode Heun, metode deret Taylor dan metode Runge-Kutta. Metode Euler mempunyai ketelitian paling rendah dari keseluruhan metode satu- langkah. Metode Heun merupakan perbaikan dari metode Euler tetapi memiliki iterasi lebih banyak dibandingkan dengan metode Euler. Metode deret Taylor memiliki kekurangan yaitu memerlukanperhitungan turunan dan tidak semua fungsi mudah dihitung turunannya.

### * Metode Euler
Metode Euler adalah salah satu dari metode satu langkah yang paling sederhana. Di banding dengan beberapa metode lainnya, metode ini paling kurang teliti. Namun demikian metode ini perlu dipelajari mengingat kesederhanaannya dan mudah pemahamannya sehingga memudahkan dalam mempelajari metode lain yang lebih teliti. Metode Euler dapat diturunkan dari Deret Taylor. Metode ini pada dasarnya adalah merepresentasikan solusinya dengan beberapa suku deret Taylor

### * Metode Heun
Metode Heun adalah salah satu metode numerik yang dapat digunakan untuk menyelesaikan berbagai persoalan matematika yang mempunyai masalah nilai awal. Masalah nilai awal merupakan masalah penyelesaian suatu persamaan diferensial dengan syarat awal yang telah diketahui.

## PLATFORM
Jadi pada modul 2 hingga modul 5 untuk berbagai metode penyelesaian numerik menggunakan bahasa phyton. Sedangkan, library yang digunakan adalah sebagai berikut:
1. sys
2. numpy 
3. matplotlib.pyplot
4. math
5. IPython
6. pprint
7. scipy.linalg

##CARA PENGGUNAAN
Tahapan pertama dengan memasukkan kode penggunaan modul, lalu masukkan kode penggunaan metode yang ada pada modul. 
### * Modul 2 (Akar-akar Persamaan )
1. Metode Setengah Interval, dengan memasukkan nilai perkiraan untuk kondisi awal yaitu nilai pertama dan akhir yaitu nilai kedua pada kolom input
2. Metode Interpolasi Linier, dengan memasukkan nilai pertama untuk kondisi awal pada kolom input
3. Metode Newton-Rhapson, dengan memasukkan nilai pertama untuk perkiraan kondisi awal pada kolom input
4. Metode Iterasi, dengan memasukkan nilai pertama untuk perkiraan kondisi awal pada kolom input
5. Metode Secant,dengan memasukkan nilai pertama untuk perkiraan kondisi awal pada kolom input
### * Modul 3 (Sistem Persamaan Linier dan Matriks)
Matriks 1 = [2, 4, 6, 8],[1, 4, 3, 4],[3, 9, 1, 2],[2, 9, 1, 3]
Matriks 2 = [24.097, 4.097, 0.4303, 0.5256]

1. Metode Gauss-Seidel, dengan memasukkan matriks 1 pada inputan matriks augmented dari SPL, dan mmemasukkan matriks 2 pada inputan nilai hasil dari SPL  
2. Metode Gauss-Jordan, dengan memasukkan matriks 1 pada inputan matriks augmented dari SPL, dan mmemasukkan matriks 2 pada inputan nilai hasil dari SPL
3. Metode Gauss, dengan memasukkan matriks 1 pada inputan matriks augmented dari SPL, dan mmemasukkan matriks 2 pada inputan nilai hasil dari SPL
4. Metode Jacobi, dengan memasukkan matriks 1 pada inputan matriks augmented dari SPL, dan mmemasukkan matriks 2 pada inputan nilai hasil dari SPL

### * Modul 4 (Integrasi Numerik)
1. Metode Satu Pias
2. Metode Banyak Pias
3. Metode Simpson 1/3 
4. Metode Simpson 3/8

### * Modul 5 (Persamaan Persamaan Differensial Biasa) 
1. Metode Euler, dengan memasukkan nama, nim, kelas, nilai H (banyak langkah yang digunakan), x0 (nilai x awal atau perkiraan kondisi awal), xn (sebagai nilai x akhir), y0 (sebagai kondisi awal untuk nilai y awal)
2. Metode Heun, dengan memasukkan nama, nim, kelas, nilai H (banyak langkah yang digunakan), x0 (nilai x awal atau perkiraan kondisi awal), xn (sebagai nilai x akhir), y0 (sebagai kondisi awal untuk nilai y awal)

## SARAN UNTUK PENGEMBANGAN
Sebagai praktikan mata kuliah Metode Numerik yang telah melaksanakan kegiatan praktikum modul 1 hingga modul 5 dan untuk saat ini masuk ke dalam tugas akhir, terdapat beberapa saran yaitu:
1. Kegiatan perkuliahan kedepannya agar dapat berjalan secara offline, sehingga disaat praktikan bingung dapat lebih mudah dalam sesi tanya-jawab dan antara asisten dan
praktikan dapat lebih terkoordinir. Namun, kondisi ini dapat menyesuaikan karena dapat dimaklumi
2. Pengenalan fungsi logika phyton lebih ditekankan karena ini sebagai dasar saat masuk ke modul-modul praktikum, sehingga praktikan dapat lebih mengerti
3. Script code tiap line untuk modul praktikum dapat lebih dijelaskan kegunaannya dan dijelaskan juga bentuk script code lain apabila ingin melakukan modifikasi pengerjaan
4. Praktikum kedepannya dapat menggunakan variasi bahasa pemrograman lainnya seperti C++, Java, HTML, dan lainnya

## UCAPAN TERIMA KASIH
Demikian dari Tugas Akhir Metode Numerik dari kami. Kami dari kelompok 11 mengucapkan permintaan maaf apabila terdapat kesalahan di dalam tugas akhir ini. Kami juga mengucapkan terima kasih kepada :
1. Seluruh Dosen Pengampu mata kuliah Metode Numerik
2. Tim asisten praktikum metode numerik 2021 yang telah mendampingi selama berjalannya praktikum hingga tugas akhir
3. Seluruh teman-teman yang membantu dan mendukung dalam penyusunan repositori ini
