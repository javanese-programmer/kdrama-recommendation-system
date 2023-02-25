
# Korean Drama Recommendation System

## Project Overview

*Korean Drama* (K-Drama) adalah salah satu komoditas ekspor Korea Selatan dalam bidang seni dan hiburan. K-Drama juga merupakan salah satu penyebab terjadinya *Korean Wave* (*Hallyu*) Jilid I pada tahun 2000-an [1]. Hallyu Jilid I ditandai oleh menyebarnya popularitas K-Drama ke luar negara Korea Selatan, yaitu ke negara Asia lainnya [2]. Pada tahun 2005, misalnya, K-Drama mengisi sebesar 96,2 persen dari keseluruhan ekspor program televisi Korea Selatan dalam bidang hiburan [3]. Hal ini menunjukkan bahwa K-Drama merupakan jenis hiburan yang disenangi pada masa itu.<br>

Meskipun demikian, memasuki tahun 2010-an terjadi penurunan popularitas dari K-Drama. Pada 2012, porsi K-Drama dalam ekspor program televisi Korea Selatan menurun menjadi sekitar 85 persen [3]. Meskipun mengalami penurunan, K-Drama tetap menjadi konten hiburan yang menarik konsumen di pasar internasional. Dalam *White Paper of the Korean Broadcast Industry*, pada 2015, lisensi K-Drama behasil dijual ke negara non-Asia seperti Amerika Serikat (4.291 judul), Romania (299 judul), dan Belgium (261 judul) [4]. 

Saat ini, dengan munculnya layanan *streaming* seperti Netflix, HBO Max, dan Disney Plus, K-Drama tetap menjadi konten hiburan populer dan menguntungkan. Satu contoh kasus adalah bagaimana K-Drama berjudul *Squid Game* dari Netflix berhasil menjadi salah satu konten paling ditonton di layanan tersebut pada 2021 [5]. K-Drama ini bahkan meninggalkan jejak kultural setelah penayangannya [6].

Berdasarkan latar belakang tersebut, dalam proyek ini akan dibuat sebuah sistem untuk merekomendasikan tayangan K-Drama. Rekomendasi akan membantu konsumen yang baru mencoba menonton K-Drama agar tidak kebingungan dalam memilih. Dengan begitu, hal ini akan membantu penyedia konten dalam memamerkan katalog K-Drama yang dimilikinya. 

## Business Understanding

### Problem Statement

K-Drama merupakan komoditas hiburan yang populer dan disukai oleh konsumen konten hiburan. Jumlah judul K-Drama, sejak awal penyebarannya di awal  2000-an, bisa mencapai ribuan. Hal ini tentu dapat membingungkan konsumen dalam memilih judul K-Drama. Oleh karena itu, diperlukan sebuah sistem untuk merekomendasikan judul K-Drama agar memudahkan konsumen dalam mengakses konten-konten tersebut.

### Goals

Pada proyek ini akan dibuat sebuah sistem rekomendasi yang akan merekomendasikan K-Drama berdasarkan *genre dan rating-nya* sehingga dapat membantu konsumen dalam memilih judul K-Drama yang akan ditonton.

### Solution Statement

Ada dua solusi yang diusulkan untuk menyelesaikan proyek ini:
1. Content Based Filtering
2. Collaborative Filtering

Pada solusi pertama, sistem rekomendasi akan dibangun berdasarkan karakteristik K-Drama yang telah dinilai atau diminati oleh konsumen. Sementara itu, pada solusi kedua, rekomendasi akan diberikan berdasarkan penilian dari seluruh konsumen yang pernah melihat dan menilai K-Drama.

## Data Understanding

Data yang digunakan adalah *IMDb Korean TV Series* yang dapat diunduh dari [Kaggle](https://www.kaggle.com/datasets/chanoncharuchinda/imdb-korean-tv-series?select=koreanTV.csv). Data ini berisi daftar seri televisi Korea yang diperoleh melalui proses *web scraping* dari situs IMDb. Situs ini memuat informasi dan rating dari film dan juga seri televisi.

Pada *dataset* tersebut, terdapat dua berkas *comma-separated value* (CSV). Berkas pertama bernama *koreanTV.csv* yang berisi informasi terkait seri televisi Korea di IMDB. Berkas ini berisi 1.989 data. Sementara itu, berkas kedua bernama *koreanTV_comment.csv* yang berisi komentar dan *rating* dari pengguna situs IMDb. Berkas ini berisi 8.275 data.

Pada berkas pertama, informasi dari masing-masing kolom adalah sebagai berikut:
* Title : judul seri televisi;
* Year : tahun rilis seri;
* Rating : rating yang diberikan pengguna;
* Votes : berapa banyak pengguna yang memberikan rating;
* Time : lama satu episode;
* Genre : daftar genre dari seri;
* Stars : daftar pemain dalam seri;
* Short Story : sinopsis dari seri.

Sementara itu, dalam berkas kedua, informasi dari masing-masing kolom adalah sebagai berikut:
* Title : judul seri televisi;
* Review Title : judul dari reviu pengguna;
* User Rating : rating yang diberikan pemberi reviu;
* Content: isi dari reviu pengguna
* Helpfullness Vote: berapa pengguna yang menganggap reviu tersebut membantu.

### Berkas Pertama
**Exploratory Data Analysis (EDA)**
Di sini, berkas pertama memiliki beberapa nilai yang tidak terdefinisi seperti "-". Oleh karena itu, hal pertama yang dilakukan adalah mendefinisikan nilai tersebut sebagai nilai hilang (*missing values*) saat melakukan *loading* data. 

Selain itu, nama dari beberapa kolom terlalu panjang dan kurang rapi. Oleh karena itu, dilakukan perubahan nama kolom menjadi 'Title', 'Year', 'Final Rating', 'Total Votes', 'Duration', 'Genre', 'Stars', dan 'Synopsis'.

![EDA1](https://drive.google.com/uc?export=view&id=1waWUBiL6Oq5BvhcX4REwZ75cy1U_k7AJ) 

Gambar 1. Jumlah Nilai yang Hilang pada Berkas Pertama

Saat melakukan pengecekan, diketahui bahwa beberapa kolom memiliki sejumlah nilai yang hilang. Hal ini dapat diamati pada Gambar 1. Meskipun demikian, karena sistem rekomendasi akan dibangun dengan mempertimbangkan *rating dan genre*, kolom dengan banyak nilai hilang akan dibuang terlebih dahulu. Setelah itu, baru dilakukan pembuatan data menurut baris dengan data yang hilang. Hasil akhirnya dapat dilihat pada Gambar 2.

![EDA2](https://drive.google.com/uc?export=view&id=12pDhrYImkqh1OTDY0e8CEOIcZZ6udylz) 

Gambar 2. Jumlah Nilai Hilang pada Berkas Pertama setelah Dibersihkan

**Visualization**
Setelah data cukup bersih, hal selanjutnya yang dilakukan adalah melakukan visualisasi pada data, Visualisasi dilakukan pada data yang bernilai numerik. Dalam berkas pertama ini, data yang dimaksud adalah data dalam kolom *Final Rating*. Hasilnya dapat diamati pada Gambar 3 dan Gambar 4.

![Distplot1](https://drive.google.com/uc?export=view&id=1JtVLENVWIbALJqia32Q1g7b0vU-jbRcu) 

Gambar 3. *Distribution Plot* dari *Final Rating*

![Boxplot1](https://drive.google.com/uc?export=view&id=1Xo-FDbrKNP_HRa2GzcTZ0Q4zr_ePomhZ) 

Gambar 4. *Boxplot* dari *Final Rating*

Dari visualisasi yang telah dilakukan, diketahui bahwa untuk berkas pertama, distribusi nilai *Final Rating* terpusat di sekitar angka 8. Hal ini dapat dilihat dari *distribution plot* pada Gambar 3. Selain itu, dari *boxplot* pada Gambar 4, diketahui bahwa data *Final Rating* juga memuat beberapa nilai *outliers*.

### Berkas Kedua
**Exploratory Data Analysis (EDA)**
Proses EDA yang dilakukan untuk berkas kedua tidak jauh berbeda dari berkas pertama. Beberapa hal yang dilakukan di antaranya adalah mendefinisikan beberapa nilai yang tidak terdefinisi sebagai nilai yang hilang. Selain itu, dari dilakukan juga perubahan nama kolom menjadi 'Title', 'Review Title', 'Rating', 'Review', dan 'Helpfulness' agar lebih singkat dan informatif. 

![Eda3](https://drive.google.com/uc?export=view&id=1qrn4MoOPknldX3vLAMzfqW3Fr7Sh91RB) 

Gambar 5. Jumlah Nilai Hilang pada Berkas Kedua

Proses pengecekan pada data juga menemukan data hilang pada berkas kedua. Dari Gambar 5, ditemukan nilai yang hilang pada kolom *Rating*. Oleh karena itu, di sini, baris dengan data yang hilang akan dibuang sehingga jumlah data hilang menjadi seperti pada Gambar 6.

![Eda4](https://drive.google.com/uc?export=view&id=1kGL3mV6DDJ7AinbgFqlA8gHU1Z47w04L) 

Gambar 6. Jumlah Nilai Hilang pada Berkas Kedua setelah Pembersihan

Pengecekan pada tipe data juga memberikan informasi bahwa tipe data pada kolom *Rating* masih bertipe *object*. Hal ini dapat diamati dari keluaran pada Gambar 7. Oleh karena itu, di sini, juga dilakukan proses konversi dari data *string* atau *object* ke tipe numerik yaitu *integer*. Hasilnya dapat diamati pada Gambar 8.

![Eda5](https://drive.google.com/uc?export=view&id=15kDVFh5m4gSVUNf5yqStdE7Hc_QS5_1N) 

Gambar 7. Tipe Data dan Jumlah Data Tidak Hilang pada Berkas Kedua

![Eda6](https://drive.google.com/uc?export=view&id=1LFyDcIib8Jj-g9kCQ47pJAVu7iip7X_j) 

Gambar 8. Tipe Data dan Jumlah Data Tidak Hilang pada Berkas Kedua setelah Konversi

**Visualization**
Proses visualisasi yang dilakukan juga mirip dengan berkas pertama. Karena nilai *Rating* adalah satu-satunya nilai numerik pada berkas kedua, visualisasi akan dilakukan untuk nilai pada kolom tersebut. Di sini, hasil visualisasi ditunjukkan oleh Gambar 9 dan Gambar 10. 

![Distplot2](https://drive.google.com/uc?export=view&id=14T9cTQ9r8LWX9TUJPnxEZAoLqha72v2E) 

Gambar 9. *Distribution Plot* dari *Rating*

![Boxplot2](https://drive.google.com/uc?export=view&id=1e_g77EmLMqqpDDpiD0b2yNJRwEy5ny2T) 

Gambar 10. *Boxplot* dari *Rating*

Dari Gambar 9,  diketahui bahwa nilai rating terpusat di angka 10 yang dapat diamati dari *distribution plot*. Sementara itu, dari Gambar 10, nilai rating pada berkas kedua juga memiliki beberapa *outliers*.

## Data Preparation

### Berkas Pertama
**Menghilangkan Outliers**
Seperti telah disebutkan, pada berkas pertama terdapat *outliers* pada nilai *Final Rating*. Oleh karena itu, di sini, data akan dibersihkan dengan *metode Inter-Quantile Range (IQR)*.

**Membuang Judul Duplikat**

![Prepare1](https://drive.google.com/uc?export=view&id=1RDst7ELd_gu3_dIzLtVefFiV6pSEchoG) 

Gambar 11. Jumlah Kemunculan Judul pada Berkas Pertama

Setelah dilakukan pengecekan, ternyata terdapat beberapa judul yang memiliki lebih dari satu entri. Hal ini dapat dilihat pada Gambar 11. Oleh karena itu, di sini, baris dengan judul duplikat akan dibuang. Hasilnya dapat diamati pada Gambar 12.

![Prepare2](https://drive.google.com/uc?export=view&id=17nk1XnAbMcIokeAlSQ1id2cO0pXnZqxA) 

Gambar 12. Jumlah Kemunculan Judul pada Berkas Pertama setelah Pembersihan

**Membuang Genre Non-Drama**
Ketika dilakukan pengecekan terhadap genre, data ternyata memuat beberapa acara non-drama. Acara tersebut seperti *talk-show*, *game-show*, *reality-TV*, *documentary*, dan *biography*. Pada tahap ini, acara dengan genre tersebut akan dibuang dari data. 

![Prepare3](https://drive.google.com/uc?export=view&id=1CK_j8lO2h6mPF_d2UAme6BVjoB4OytnV) 

Gambar 13. Genre Non-Drama pada Berkas Pertama

### Berkas Kedua
**Membuang Outliers**
Seperti pada berkas pertama, berkas kedua juga memiliki *outliers* pada nilai rating. Agar tidak menganggu pelatihan model sistem rekomendasi, nilai *outliers* akan dibuang dengan metode IQR.

**Membuat User ID**
Pada data yang digunakan, belum ada User ID dari pemberi reviu. Oleh karena itu, di sini, akan di-*generate* data baru untuk memenuhi kekosongan tersebut

**Encoding User dan Judul**
Sebelum dilakukan pelatihan model, data pengguna dan judul drama pada data akan dilakukan proses penyandian (*encoding*) agar memudahkan proses prediksi. Selain itu, akan dilakukan pemetaan pengguna dan judul ke sandi tersebut.

**Membagi Data Latih dan uji**
Pada tahap ini, data akan dibagi menjadi data latih dan data uji untuk keperluan melatih model. Rasio yang digunakan adalah sebesar *80:20*. Selain itu, data label yang digunakan, yaitu nilai rating, akan dilakukan normalisasi sehingga nilainya berada dalam rentang 0 dan 1. Hal ini akan memudahkan proses pelatihan model.

## Model Development
### Content-Based Filtering
Metode pertama yang digunakan untuk membuat sistem rekomendasi adalah *Content-Based Filtering*. Metode ini memberikan rekomendasi dengan mengamati kesamaan karakteristik dari suatu konten drama dan memberikan drama dengan kemiripan paling tinggi. Pada proyek ini, karakteristik yang dimaksud adalah *genre* dari K-Drama.

Untuk memperoleh nilai kemiripan tersebut, digunakan gabungan dua teknik. Teknik pertama adalah *TF-IDF vectorizer *dan teknik kedua adalah *cosine similarity*. Di sini, *TF-IDF Vectorizer* akan menghasilkan matriks berisi korelasi antar fitur penting dari data. Sementara itu, *cosine similarity* akan mengukur derajar kesamaan antar matriks tersebut. 

Kelebihan dari metode *Content-Based Filtering *ini adalah metode ini tidak membutuhkan data pengguna lain untuk memberikan rekomendasi. Selain itu, metode ini dapat memberikan rekomendasi konten yang bersifat *niche* dan tidak banyak disukai pengguna lain, tetapi diminati oleh pengguna spesifik.

Kekurangan dari metode ini adalah metode ini membutuhkan representasi fitur yang perlu diolah secara manual sehingga diperlukan pengetahuan terkait domain (bidang) tertentu. Selain itu, karena rekomendasi bersifat spesifik ke pengguna tertentu, metode ini sulit memberikan rekomendasi di luar minat pengguna yang telah diketahui.

Setelah sistem rekomendasi berhasil dibangun, hal selanjutnya adalah mengujinya untuk memberi rekomendasi berdasarkan masukan yang diberikan. Di sini, sistem diberi masukan K-Drama berjudul *Vincenzo* (2021) yang dipilih secara acak. K-Drama ini memiliki genre *Comedy*, *Crime*, dan *Drama*. Hasil rekomendasi yang diberikan dapat diamati di Tabel 1. Dari hasil tersebut, dapat diamati bahwa sistem rekomendasi telah berhasil memberi rekomendasi K-Drama dengan genre yang sama dengan judul masukan.

Tabel 1. Hasil Rekomendasi Sistem Berbasis *Content-Based Filtering*
|   | **Title**             | **Genre**            |
|---|-----------------------|----------------------|
| 1 |        Squad 38       | Comedy, Crime, Drama |
| 2 | Bing-ui               | Comedy, Crime, Drama |
| 3 | Live                  | Comedy, Crime, Drama |
| 4 | Strong Girl Bong-soon | Comedy, Crime, Drama |
| 5 | Player                | Comedy, Crime, Drama |

### Collaborative Filtering
Metode kedua yang digunakan untuk membangun sistem rekomendasi adalah *Collaborative Filtering*. Secara spesifik, metode pada proyek ini adalah metode berbasis model dengan jaringan saraf tiruan (*artificial neural network*). Jaringan saraf ini kemudian akan dilatih dengan data yang telah disiapkan, sebelum digunakan untuk memberikan rekomendasi berdasarkan identitas pengguna.

Kelebihan dari metode ini adalah metode tidak membutuhkan pengetahuan di domain (bidang) tertentu karena model akan mampu mempelajari fitur secara otomatis. Selain itu, model ini dapat merekomendasikan sesuatu di luar minat pengguna sehingga akan memperluas minat tersebut.

Kekurangan dari metode ini adalah metode ini tidak mampu memberikan rekomendasi bagi data (*item*) baru yang sebelumnya tidak termasuk dalam data latih. Selain itu, metode ini akan sulit menerima fitur tambahan (fitur samping) yang sebelumnya tidak ada di data latih seperti fitur jumlah *votes*, dll.

Sistem rekomendasi kedua ini juga diuji hasilnya. Di sini, akan diberi rekomendasi K-Drama untuk pengguna dengan identitas USER2087. Pengguna ini telah memberi rating tinggi untuk K-Drama berjudul *Record of Youth* yang bergenre *Drama* dan *Romance*. Sistem bertipe *Collaborative Filtering* menghasilkan rekomendasi seperti ditunjukkan pada Tabel 2.

Tabel 2. Rekomendasi untuk USER2087 dari Sistem Rekomendasi Kedua
|   | **Title**                            | **Genre**               |
|---|--------------------------------------|-------------------------|
| 1 | One Ordinary Day                     |      Crime, Mystery     |
| 2 | It's Okay Not to Be Okay             | Comedy, Drama, Romance  |
| 3 | The Flower of Evil                   | Crime, Mystery, Romance |
| 4 | Friend, Our Legend                   | Action, Crime, Drama    |
| 5 | Team Bulldog: Off-duty Investigation | Action, Crime, Drama    |
| 6 | On the Way to the Airport            | Drama, Romance          |

Dari Tabel 2 tersebut, dapat diketahui bahwa sistem rekomendasi memberikan beberapa K-Drama dengan genre yang mirip seperti yang telah dinilai pengguna, seperti *It's Okay not to Be Okay* dan *On the Way to the Airport*. Sistem juga memberi rekomendasi K-Drama dengan genre yang agak berbeda seperti *One Ordinary Day*. Hal ini sesuai dengan karakteristik *Collaborative Filtering* yang menjadi dasar sistem kedua. 

## Evaluation
Untuk mengukur keberhasilan sistem rekomendasi yang dibuat, digunakan dua metrik:
1. *Root Mean Squared Error* (RMSE) untuk Collaborative Filtering
2. Presisi untuk Content-Based Filtering 

RMSE memberi informasi terkait seberapa besar kesalahan prediksi (*error*) dari model. Kesalahan prediksi diperoleh dengan menghitung selisih dari data prediksi terhadap data sebenarnya. RMSE dihitung dengan mengikuti persamaan di bawah:

$$ MSE = \frac{1}{N} \sum (y_{true} - y_{pred})^2 $$<br>
$$ RMSE = \sqrt{MSE} $$ <br>

Sementara itu, presisi mengukur seberapa tepat sistem rekomendasi dalam menentukan jenis konten yang direkomendasikan. Presisi pada proyek ini diukur dengan melihat genre dari konten yang direkomendasikan dan membandingkannya dengan genre konten yang dimasukkan ke sistem. Apabila ada satu kecocokan, meskipun hanya pada satu genre, prediksi tersebut akan dianggap sebagai *positif*. Sementara itu, apabila tidak ada kecocokan sama sekali, maka prediksi dianggap *negatif*. Presisi kemudian dihitung dengan membandingkan jumlah prediksi positif terhadap total prediksi:

$$ Presisi = \frac{Total Prediksi Positif}{Total Prediksi} \times 100 $$ <br>

Pada proyek ini, sistem rekomendasi dengan tipe Collaborative Filtering memiliki nilai RMSE latih dan validasi masing-masing sebesar 0.043 dan 0.292, seperti dapat dilihat pada Tabel 3. Hal ini menunjukkan bahwa model belum memiliki kemampuan generalisasi yang baik dilihat dari RMSE validasi yang masih cukup besar. Hal ini membuka peluang peningkatan kinerja model. Meskipun demikian, model ini tetap mampu memberikan rekomendasi K-Drama meskipun dengan nilai kesalahan yang tidak kecil.

Tabel 3. Nilai Metric Evaluasi Model *Collaborative Filtering*
|                        | **Train**        | **Validation** |
|------------------------|------------------|----------------|
| **Collaborative RMSE** | 0.043502 | 0.29282 |

Sementara itu, untuk tipe Content-Based Filtering, sistem rekomendasi yang dibangun berhasil mencapai presisi sebesar 100 persen seperti dapat dilihat pada Tabel 4. Hal ini menunjukkan bahwa model ini memiliki kinerja yang sangat baik untuk memberikan rekomendasi konten K-Drama.

Tabel 4. Presisi untuk Sistem Berbasis *Content-Based Filtering*
|                       | **Positive** | **Negative** | **Precision** |
|-----------------------|--------------|--------------|---------------|
| **Content Precision** | 5            |       0      | 100           |

Dengan demikian, proyek ini dapat dikatakan telah mampu menghasilkan dua sistem rekomendasi yang fungsional meskipun dengan kinerja yang masih dapat ditingkatkan. Sistem rekomendasi ini dapat dimanfaatkan untuk berbagai layanan yang menyediakan konten hiburan berisi K-Drama.

## Conclusion
K-Drama merupakan komoditas hiburan yang populer dan disukai banyak orang. Hal ini menjadi alasan K-Drama menjadi salah satu konten utama yang disediakan oleh berbagai layanan *streaming* dan penyedia konten hiburan. Banyaknya judul K-Drama akan mempersulit konsumen dari layanan tersebut dalam membuat keputusan, sehingga dibutuhkan bantuan dari sistem rekomendasi. 

Karena alasan tersebut, dalam proyek ini, dibangun dua sistem rekomendasi berbasis *Content-Based Filtering* dan *Collaborative Filtering*. Kedua model ini memiliki kelebihan dan kekurangan tersendiri, serta cocok untuk kasus yang berbeda. Untuk *Content-Based Filtering*, sistem rekomendasi akan memberikan judul berdasarkan genre. Sementara itu, pada *Collaborative Filtering*, sistem akan memberi rekomendasi menurut rating.

Hasil evaluasi proyek menunjukkan bahwa kedua sistem rekomendasi yang dibuat telah bekerja secara fungsional. Pada sistem *Content-Based Filtering*, rekomendasi yang diberikan berhasil mencapai presisi 100 persen, sehingga sistem ini terbukti dapat memberikan rekomendasi K-Drama sesuai dengan genre-nya. Sementara itu, untuk sistem *Collaborative Filtering*, masih terdapat ruang untuk perbaikan. Hal ini dapat dilihat dari RMSE validasi yang bernilai 0.292. Meskipun demikian, sistem rekomendasi ini sudah mampu memberikan beberapa rekomendasi K-Drama yang relevan dengan K-Drama yang dinilai pengguna. 

Dengan begitu, dapat diketahui bahwa proyek ini telah mampu menghasilkan sistem rekomendasi yang memenuhi tujuan awal proyek, yaitu merekomendasikan K-Drama.


**Referensi:** <br>
[1] Jeong, J. (2012). Ethnoscapes, mediascapes, and ideoscapes: Socio-cultural relations between South Korea and China.
Journal of International and Area Studies, 19(2), 77–95. <br>
[2] Madrid-Morales, D., & Lovric, B. (2015). Transatlantic connection: K-pop and K-drama fandom in Spain and
Latin America. Journal of Fandom Studies, 3(1), 23–41. <br>
[3] Ju, H. (2017). National television moves to the region and beyond: South Korean TV drama production with a
new cultural act. Journal of International Communication, 23(1), 94–114. <br>
[4] Ministry of Science, ICT, and Future Planning & Korean Communication Commission. (2016). White paper of
Korean broadcast industry. Seoul, Korea: MSIF. <br>
[5] Solsman, J.E. (2021) Netflix's squid game was even bigger than you thought -- 2.1B hours big, CNET. CNET. Available at: https://www.cnet.com/culture/entertainment/netflix-squid-game-is-even-bigger-than-you-thought-2-billion-hours-big/#:~:text=Squid%20Game%2C%20at%201.65%20billion,anything%20else%20Netflix%20has%20released. (Accessed: October 24, 2022). <br>
[6] Siregar, N., Angin, A. B. P., & Mono, U. (2021). The Cultural Effect of Popular Korean Drama: Squid Game. IDEAS: Journal on English Language Teaching and Learning, Linguistics and Literature, 9(2), 445-451. <br>
