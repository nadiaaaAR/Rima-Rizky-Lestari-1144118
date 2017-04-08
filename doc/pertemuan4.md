**Ruang Keadaan**
<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/4-4.jpg" width="400px">
</p>
**Latar Belakang**

Di dalam Kecerdasan Buatan terdapat Masalah, Ruang Keadaan, dan Pencarian. Tetapi pada pertemuan kemarin di bahas mengenai Ruang Keadaan atau State Space. Pada pembahasan kali ini akan dijelaskan tentang Ruang Keadaan.

**Pembahasan**

Ruang Keadaan atau State Space adalah suatu ruang yang berisikan semua keadaan yang memungkinkan terjadi. Cara mendeskripsikan masalah adalah

**a.** Menetapkan kumpulan aturan
**b.** Menetapkan satu atau lebih keadaan awal
**c.** Menetapkan satu atau lebih tujuan
**d.** Mendefinisikan suatu ruang keadaan

Contoh:

Masalah Petani, Kambing, Serigala, dan Kambing
<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/4.jpg" width="400px">
</p>
- Seorang petani akan menyebrangkan sayuran, seekor kambing dan seekor serigala menggunakan sebuah perahu pada sebuah sungai.
- Namun, perahu hanya bisa menampung petani dan penumpang lainnya.
- Jika petani pergi, maka sayuran akan dimakan oleh kambing dan kambing akan di makan oleh serigala.

Penyelesaian:

1. Identifikasi ruang keadaan

Permasalahan ini dapat dilambangkan dengan (jumlah kambing,jumlah serigala,jumlah sayuran,jumlah perahu).

Contoh : daerah asal (0,1,1,1) = daerah asal, kambing tidak ada, serigala ada, sayuran ada, dan perahu ada.

2. Keadaan awal dan tujuan
Keadaan awal, pada kedua daerah :
daerah asal = (1,1,1,1)
daerah seberang = (0,0,0,0)

Keadaan tujuan, pada kedua daerah :
daerah asal = (0,0,0,0)
daerah seberang = (1,1,1,1)

3. Aturan – aturan
<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/4-1.jpg" width="400px">
</p>
4. Solusi dan Hasil Program yang telah dibuat
<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/4-2.jpg" width="400px">
</p>
**Hasil**
<p align="center">
  <img src="https://github.com/D4TI3C/Rima-Rizky-Lestari-1144118/blob/master/img/4-3.png" width="400px">
</p>
**Penutup**

1. **Kesimpulan :** Ruang Keadaan adalah ruang yang berisi sega kemungkinan yang terjadi, pedeskripsian sebuah masalah berdasarkan definisi ruang keadaan, menetapkan kumpulan aturan dan lainnya. Contohnya seperti kasus petani, sayur, kambing dan serigala.
2. **Saran :** Sebaiknya mencari referensi lain yang lebih lengkap dan diadakannya percobaan atau praktek sendiri.

