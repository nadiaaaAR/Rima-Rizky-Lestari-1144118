**REPRESENTASI PENGETAHUAN II**

<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/3.jpg" width="400px">
</p>

**Latar Belakang**

Di dalam Kecerdasan Buatan terdapat berbagai macam cara salah satunya untuk menyajikan atau mepresentasikan suatu pengetahuan. Pada penjelasan kali ini akan dijelaskan mengenai Representasi Pengetahuan berupa Penalaran (Reasoning), Semantic Network, dan Frame.

**Pembahasan**

1. **Reasoning**

Logika yang dikembangkan Aristoteles menjadi bagian dari studi pengacara dan politik dan digunakan untuk membedakan argumen yang valid dan yang tidak.

Untuk Aristoteles, logika merupakan alat yang diperlukan dalam semua penyelidikan/penelitian, dan silogisme merupakan hasil dari semua buah pemikiran. Silogisme adalah sebuah argumen yang dibentuk oleh dua pernyataan yang disebut premis (premis mayor dan premis minor), yang diikuti dengan sebuah kesimpulan atau konklusi. Untuk semua premis yang diberikan, jika kesimpulan dalam argumen terjamin (dalam pengertian tidak ditemukan suatu sanggahan dengan cara bagaimanapun), argumen tersebut valid. Jika kesimpulan tidak terjamin (dalam pengertian minimal terdapat satu sanggahan yang tidak membenarkan kesimpulan), argumen tersebut tidak valid.

Salah satu silogisme populer Aristoteles adalah sebagai berikut:

- Semua pria meninggal

- Socrates adalah seorang pria

2. **Semantic Network**

Semantic network adalah representasi yang mengekspresikan solusi permasalahan dengan menggunakan network (graph berarah). Di dalamnya menggunakan node(simpul) untuk merepretasikan suatu kondisi, dan arc(link) untuk merepretasikan relasi antar simpul

**Contoh:**

<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/3-2.PNG" width="400px">
</p>

Permasalahan pertani, serigala, angsa dan padi. Seorang petani ingin memindahkan dirinya sendiri, seekor serigala, seekor angsa gemuk, dan seikat padi yang berisi menyeberangi sungai. Sayangnya, perahunya sangat terbatas; dia hanya dapat membawa 1object dalam 1 penyeberangan. Dan lagi, dia tidak bisa meninggalkan angsa dan serigala dalam satu tempat, karena serigala akan memangsa angsa. Demikian pula dia tidak bisa meninggalkan angsa dan padi dalam satu tempat.

Mendeskripsikan permasalahan di atas dengan menggunakan bahasa natural bukanlah cara yang tepat. Dalam hal ini, kita dapa menggunakan Semantic Network untuk merepretasikannya.

Untuk membuat graph-nya, maka kita harus membangun node(simpul) untuk setiap kondisi yang memungkinkan bagi petani tersebut. Dengan memperhatikan petani dan tiga barangnya yang kemungkinan berada pada 2 seberang sungai, maka kita dapat menghitung jumlah simpul secara keseluruhan adalah 2^1+3= 2^4=16, dimana 10 simpul adalah kondisi yang aman (tidak ada satu barangpun yang termakan).

Langkah kedua dan merupakan langkah terakhir adalah membentuk link dari masing-masing perjalanan perahu. Pasangan dari dua buah node(simpul) dapat digabungkan dengan menggunakan link jika dan hanya jika bertemu pada 2 kondisi, yaitu: petama, petani berubah tempat, salah satu barang dari petani berubah tempat. Karena terdapat 10 buah simpul yang masuk dalam batasan (aman), dimungkinkan adanya 10 x 9 = 90 pasangan, akan tetapi hanya 20 link yang dapat terbentuk karena batasan sepertu yang disebut di atas.

3. **Frame**

Frame ditemukan oleh marvin Minsky pada tahun 1974 merupakan kumpulan pengetahuan tentang suatu object tertentu, peristiwa, lokasi, situasi, dll.

Frame memiliki slot yang menggambarkan rincian (atribut) dan karakteristik obyek. Frame biasanya digunakan untuk merepretasikan pengetahuan yang didasarkan pada karakteristik yang sudah dikenal, yang merupakan pengalaman-pengalaman. Dengan menggunakan frame, sangat mudah membuat inferensi tentang obyek, peristiwa atau situasi baru, karena frame menyediakan basis pengetahuan yang ditarik dari pengalaman. Ide hirariki dari frame sama dengan ide hirarki class yang terdapat pada pemrograman berorientasi obyek.

**PENUTUP**

**a.** Kesimpulan :** Respresentasi Pengetahuan merupakan sebuah penyajian sebuah pengetahuan ke dalam skema tertentu agar dapat diakui penalarannya.

**b.** Saran :** disarankan mencari referensi dari sumber lain agar lebih dalam mempelajari tentang pembahasan ini.
