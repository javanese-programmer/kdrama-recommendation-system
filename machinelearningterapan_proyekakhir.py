# -*- coding: utf-8 -*-
"""MachineLearningTerapan_ProyekAkhir.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oE1O43gTzl6OiTjKB271laSyb9RYadt8

# K-Drama Recommendation System

## Project Overview

*Korean Drama* (K-Drama) adalah salah satu komoditas ekspor Korea Selatan dalam bidang seni dan hiburan. K-Drama juga merupakan salah satu penyebab terjadinya *Korean Wave* (*Hallyu*) Jilid I pada tahun 2000-an [1]. Hallyu Jilid I ditandai oleh menyebarnya popularitas K-Drama ke luar negara Korea Selatan, yaitu ke negara Asia lainnya [2]. Pada tahun 2005, misalnya, K-Drama mengisi sebesar 96,2 persen dari keseluruhan ekspor program televisi Korea Selatan dalam bidang hiburan [3]. Hal ini menunjukkan bahwa K-Drama merupakan jenis hiburan yang disenangi pada masa itu.<br>

Meskipun demikian, memasuki tahun 2010-an terjadi penurunan popularitas dari K-Drama. Pada 2012, porsi K-Drama dalam ekspor program televisi Korea Selatan menurun menjadi sekitar 85 persen [3]. Meskipun mengalami penurunan, K-Drama tetap menjadi konten hiburan yang menarik konsumen di pasar internasional. Dalam *White Paper of the Korean Broadcast Industry*, pada 2015, lisensi K-Drama behasil dijual ke negara non-Asia seperti Amerika Serikat (4.291 judul), Romania (299 judul), dan Belgium (261 judul) [4]. 

Saat ini, dengan munculnya layanan *streaming* seperti Netflix, HBO Max, dan Disney Plus, K-Drama tetap menjadi konten hiburan populer dan menguntungkan. Satu contoh kasus adalah bagaimana K-Drama berjudul *Squid Game* dari Netflix berhasil menjadi salah satu konten paling ditonton di layanan tersebut pada 2021 [5]. K-Drama ini bahkan meninggalkan jejak kultural setelah penayangannya [6].

Berdasarkan latar belakang tersebut, dalam proyek ini akan dibuat sebuah sistem untuk merekomendasikan tayangan K-Drama. Rekomendasi akan membantu konsumen yang baru mencoba menonton K-Drama agar tidak kebingungan dalam memilih. Dengan begitu, hal ini akan membantu penyedia konten dalam memamerkan katalog K-Drama yang dimilikinya. 

**Referensi** <br>
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

## Business Understanding

### Problem Statements

K-Drama merupakan komoditas hiburan yang populer dan disukai oleh konsumen konten hiburan. Jumlah judul K-Drama, sejak awal penyebarannya di awal  2000-an, bisa mencapai ribuan. Hal ini tentu dapat membingungkan konsumen dalam memilih judul K-Drama. Oleh karena itu, diperlukan sebuah sistem untuk merekomendasikan judul K-Drama agar memudahkan konsumen dalam mengakses konten-konten tersebut.

### Goals

Pada proyek ini akan dibuat sebuah sistem rekomendasi yang akan merekomendasikan K-Drama berdasarkan *genre dan rating-nya* sehingga dapat membantu konsumen dalam memilih judul K-Drama yang akan ditonton.

### Solution Approach

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
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Required Library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


import os
from google.colab import drive
import warnings
warnings.filterwarnings("ignore")

# Mount Gdrive
drive.mount('/content/gdrive/', force_remount=True)

# Unzip dataset
!unzip /content/gdrive/MyDrive/Training/Dicoding/Dataset/Korean_Drama/archive.zip

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""### Berkas Pertama

**Exploratory Data Analysis (EDA)**

Di sini, berkas pertama memiliki beberapa nilai yang tidak terdefinisi seperti "-". Oleh karena itu, hal pertama yang dilakukan adalah mendefinisikan nilai tersebut sebagai nilai hilang (*missing values*) saat melakukan *loading* data. 

Selain itu, nama dari beberapa kolom terlalu panjang dan kurang rapi. Oleh karena itu, dilakukan perubahan nama kolom menjadi 'Title', 'Year', 'Final Rating', 'Total Votes', 'Duration', 'Genre', 'Stars', dan 'Synopsis'.
"""

# Define Missing Values
missing_values = ["?", "--", '!', '^', '-', '_', ' ']

# Load data
data1 = pd.read_csv("koreanTV.csv", na_values = missing_values)
data1.head()

# Rename columns
data1.columns = ['Title', 'Year', 'Final Rating', 'Total Votes', 'Duration', 'Genre', 'Stars', 'Synopsis']
data1.head()

data1.info()

data1.isna().sum()

"""Pada data di atas, diketahui bahwa beberapa kolom memiliki sejumlah nilai yang hilang. Meskipun demikian, karena sistem rekomendasi akan dibangun dengan mempertimbangkan *rating dan genre*, kolom dengan banyak nilai hilang akan dibuang terlebih dahulu. Setelah itu, baru dilakukan pembuangan data menurut baris dengan data yang hilang."""

# Drop columns with large missing values
data1.drop(['Duration', 'Stars'], axis = 1, inplace=True)

data1.isna().sum()

# Drop the remaining rows with missing values
data1.dropna(axis=0, how='any', inplace=True)

data1.isna().sum()

# Check the data
data1.info()

# Check the final rating distribution
data1.describe()

"""**Visualization**"""

plt.figure(figsize=(10,10))
sns.distplot(data1["Final Rating"])
plt.xlabel("Final Rating")
plt.legend()

plt.tight_layout()
plt.savefig('finalrating_distribution.png')
plt.plot()

plt.figure(figsize=(10,10))
sns.boxplot(data1["Final Rating"])
plt.xlabel("Final Rating")
plt.legend()

plt.tight_layout()
plt.savefig('finalrating_box.png')
plt.plot()

"""Dari visualisasi yang telah dilakukan, diketahui bahwa untuk berkas pertama, distribusi nilai *Final Rating* terpusat di sekitar angka 8. Hal ini dapat dilihat dari *distribution plot*. Selain itu, dari *boxplot*, diketahui bahwa data *Final Rating* juga memuat beberapa nilai *outliers*.

### Berkas Kedua

**Exploratory Data Analysis (EDA)**
"""

# Define Missing Values
missing_values = ["?", "--", '!', '^', '-', '_', ' ']

# Load data
data2 = pd.read_csv("koreanTV_comment.csv", na_values = missing_values)
data2.head()

# Rename columns
data2.columns = ['Title', 'Review Title', 'Rating', 'Review', 'Helpfulness']
data2.head()

data2.info()

data2.isna().sum()

"""Pada data di atas, ditemukan nilai yang hilang pada kolom *Rating*. Oleh karena itu, di sini, baris dengan data yang hilang akan dibuang."""

# Drop the remaining rows with missing values
data2.dropna(axis=0, how='any', inplace=True)

data2.isna().sum()

data2.info()

"""Pada data di atas, nilai pada kolom *Rating* masih bertipe object. Oleh karena itu, di sini, akan dilakukan konversi menjadi tipe data integer."""

data2['Rating'].unique()

data2.reset_index(inplace = True, drop = True)

rat_arr = []
for i in range(len(data2['Rating'].tolist())):
  rat_arr.append(data2.loc[i, 'Rating'].replace('/10', ''))

data2['Rating'] = pd.Series(rat_arr)

# Convert to integer
data2['Rating'] = pd.to_numeric(data2['Rating'])
data2.head()

data2.info()

data2.describe()

"""**Visualization**"""

plt.figure(figsize=(10,10))
sns.distplot(data2["Rating"])
plt.xlabel("Rating")
plt.legend()

plt.tight_layout()
plt.savefig('rating_distribution.png')
plt.plot()

plt.figure(figsize=(10,10))
sns.boxplot(data2["Rating"])
plt.xlabel("Rating")
plt.legend()

plt.tight_layout()
plt.savefig('rating_box.png')
plt.plot()

"""Sementara itu, untuk berkas kedua, nilai rating terpusat di angka 10 yang dapat diamati dari *distribution plot*. Nilai rating pada berkas kedua juga memiliki beberapa *outliers*.

## Data Preparation

### Berkas Pertama

**Menghilangkan Outliers**

Seperti telah disebutkan, pada berkas pertama terdapat *outliers* pada nilai *Final Rating*. Oleh karena itu, di sini, data akan dibersihkan dengan *metode Inter-Quantile Range (IQR)*.
"""

Q1 = data1.quantile(0.25)
Q3 = data1.quantile(0.75)
IQR=Q3-Q1
data1=data1[~((data1<(Q1-1.5*IQR))|(data1>(Q3+1.5*IQR))).any(axis=1)]
 
# Cek ukuran dataset setelah kita drop outliers
data1.shape

data1.reset_index(inplace = True, drop = True)

"""**Membuang Judul Duplikat**"""

data1.info()

len(data1.Title.unique())

"""Setelah dilakukan pengecekan, ternyata terdapat beberapa judul yang memiliki lebih dari satu entri. Oleh karena itu, di sini, baris dengan judul duplikat akan dibuang."""

data1['Title'].value_counts().head(12)

# Cari baris dengan judul berlebih
row_to_drop = ['Teenage Mutant Ninja Turtles', 'Running Man', 'Punch', 'Smile Again', 'Iljimae', 'Happy Together']
data1.loc[data1["Title"].isin(row_to_drop)]

data1.drop(index=[60, 747, 1403, 849, 948, 1284], inplace=True)
data1['Title'].value_counts().head(12)

data1.reset_index(inplace = True, drop = True)

"""**Membuang Genre Non-Drama**

Ketika dilakukan pengecekan terhadap genre, data ternyata memuat beberapa acara non-drama. Acara tersebut seperti *talk-show*, *game-show*, *reality-TV*, *documentary*, dan *biography*. Pada tahap ini, acara dengan genre tersebut akan dibuang dari data. 
"""

# Cek jenis genre
data1.Genre.unique()

# Cek jumlah genre
len(data1.Genre.unique())

# Cari baris dengan genre non-drama
data1_new1 = data1.copy()
non_drama = ['Documentary', 'Reality-TV', 'Game-Show', 'Talk-Show', 'Biography']

for i in range(len(data1['Genre'].tolist())):
  count = 0
  for j in non_drama:
    if (data1.loc[i, 'Genre'].find(j) >= 0):
      count += 1
  
  if (count > 0):
    data1_new1.drop(index=[i], inplace=True)

# Cek jumlah genre
len(data1_new1.Genre.unique())

# Cek jenis genre
data1_new1.Genre.unique()

data1_new1.reset_index(inplace = True, drop = True)
data1_new1.info()

"""### Berkas Kedua

**Membuang Outliers**

Seperti pada berkas pertama, berkas kedua juga memiliki *outliers* pada nilai rating. Agar tidak menganggu pelatihan model sistem rekomendasi, nilai *outliers* akan dibuang dengan metode IQR.
"""

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR=Q3-Q1
data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
 
# Cek ukuran dataset setelah kita drop outliers
data2.shape

data2.reset_index(inplace = True, drop = True)

"""**Membuat User ID**

Pada data yang digunakan, belum ada User ID dari pemberi reviu. Oleh karena itu, di sini, akan di-*generate* data baru untuk memenuhi kekosongan tersebut.
"""

len(data2['Rating'].tolist())

user_num = np.arange(1, 7533, 1)
user_id = []

for i in user_num.tolist():
  id = 'USER' + str(i)
  user_id.append(id)


data2['User ID'] = user_id
data2.head()

data2.info()

"""**Encoding User dan Judul**

Sebelum dilakukan pelatihan model, data pengguna dan judul drama pada data akan dilakukan proses penyandian (*encoding*) agar memudahkan proses prediksi. Selain itu, akan dilakukan pemetaan pengguna dan judul ke sandi tersebut.
"""

# Mengubah userID menjadi list tanpa nilai yang sama
user_ids = data2['User ID'].unique().tolist()
print('list User ID: ', user_ids)
 
# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)
 
# Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

# Mengubah Title menjadi list tanpa nilai yang sama
drama_ids = data2['Title'].unique().tolist()
 
# Melakukan proses encoding Title
drama_to_drama_encoded = {x: i for i, x in enumerate(drama_ids)}
 
# Melakukan proses encoding angka ke Title
drama_encoded_to_drama = {i: x for i, x in enumerate(drama_ids)}

# Mapping userID ke dataframe user
data2['user'] = data2['User ID'].map(user_to_user_encoded)
 
# Mapping placeID ke dataframe resto
data2['drama'] = data2['Title'].map(drama_to_drama_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
 
# Mendapatkan jumlah resto
num_drama = len(drama_encoded_to_drama)
 
# Mengubah rating menjadi nilai float
data2['Rating'] = data2['Rating'].values.astype(np.float32)
 
# Nilai minimum rating
min_rating = min(data2['Rating'])
 
# Nilai maksimal rating
max_rating = max(data2['Rating'])
 
print('Number of User: {}, Number of Drama: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_drama, min_rating, max_rating
))

"""**Membagi Data Latih dan uji**

Pada tahap ini, data akan dibagi menjadi data latih dan data uji untuk keperluan melatih model. Rasio yang digunakan adalah sebesar 80:20. Selain itu, data label yang digunakan, yaitu nilai rating, akan dilakukan normalisasi sehingga nilainya berada dalam rentang 0 dan 1. Hal ini akan memudahkan proses pelatihan model.
"""

# Mengacak dataset
data2 = data2.sample(frac=1, random_state=42)
data2

# Membuat variabel x untuk mencocokkan data user dan drama menjadi satu value
x = data2[['user', 'drama']].values
 
# Membuat variabel y untuk membuat rating dari hasil 
y = data2['Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
 
# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * data2.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)
 
print(x, y)

"""## Modeling and Result

### Content-Based Filtering

Metode pertama yang digunakan untuk membuat sistem rekomendasi adalah *Content-Based Filtering*. Metode ini memberikan rekomendasi dengan mengamati kesamaan karakteristik dari suatu konten drama dan memberikan drama dengan kemiripan paling tinggi. Pada proyek ini, karakteristik yang dimaksud adalah *genre* dari K-Drama.

Untuk memperoleh nilai kemiripan tersebut, digunakan gabungan dua teknik. Teknik pertama adalah *TF-IDF vectorizer *dan teknik kedua adalah *cosine similarity*. Di sini, *TF-IDF Vectorizer* akan menghasilkan matriks berisi korelasi antar fitur penting dari data. Sementara itu, *cosine similarity* akan mengukur derajar kesamaan antar matriks tersebut. 

Kelebihan dari metode *Content-Based Filtering *ini adalah metode ini tidak membutuhkan data pengguna lain untuk memberikan rekomendasi. Selain itu, metode ini dapat memberikan rekomendasi konten yang bersifat *niche* dan tidak banyak disukai pengguna lain, tetapi diminati oleh pengguna spesifik.

Kekurangan dari metode ini adalah metode ini membutuhkan representasi fitur yang perlu diolah secara manual sehingga diperlukan pengetahuan terkait domain (bidang) tertentu. Selain itu, karena rekomendasi bersifat spesifik ke pengguna tertentu, metode ini sulit memberikan rekomendasi di luar minat pengguna yang telah diketahui.
"""

df1 = data1_new1.copy()
df1.info()

"""**TF-IDF Vectorizer**"""

# Inisialisasi TfidfVectorizer
TF = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data Genre
TF.fit(df1['Genre']) 
 
# Mapping array dari fitur index integer ke fitur nama
TF.get_feature_names()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = TF.fit_transform(df1['Genre']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis genre
# Baris diisi dengan nama drama
 
pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=TF.get_feature_names(),
    index=df1.Title
)

"""**Cosine Similarity**"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama drama
cosine_sim_df = pd.DataFrame(cosine_sim, index=df1['Title'], columns=df1['Title'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap drama
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""**Dapatkan Rekomendasi**"""

def kdrama_recommendations(nama_drama, similarity_data=cosine_sim_df, items=df1[['Title', 'Genre']], k=5):
    """
    Rekomendasi K-Drama berdasarkan kemiripan dataframe
 
    Parameter:
    ---
    Title : tipe data string (str)
                Judul Drama (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan resto sebagai 
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---
    """
 
 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_drama].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_drama agar nama drama yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_drama, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

# random choice the title
idx = np.random.choice(np.arange(0, len(df1.Title.unique())+1, 1))
title_idx = df1.loc[idx, 'Title']

df1[df1.Title.eq(title_idx)]

# Mendapatkan rekomendasi KDrama yang mirip dengan judul yang dimasukkan
kdrama_recommendations(title_idx)

"""### Collaborative Filtering

Metode kedua yang digunakan untuk membangun sistem rekomendasi adalah *Collaborative Filtering*. Secara spesifik, metode pada proyek ini adalah metode berbasis model dengan jaringan saraf tiruan (*artificial neural network*). Jaringan saraf ini kemudian akan dilatih dengan data yang telah disiapkan, sebelum digunakan untuk memberikan rekomendasi berdasarkan identitas pengguna.

Kelebihan dari metode ini adalah metode tidak membutuhkan pengetahuan di domain (bidang) tertentu karena model akan mampu mempelajari fitur secara otomatis. Selain itu, model ini dapat merekomendasikan sesuatu di luar minat pengguna sehingga akan memperluas minat tersebut.

Kekurangan dari metode ini adalah metode ini tidak mampu memberikan rekomendasi bagi data (*item*) baru yang sebelumnya tidak termasuk dalam data latih. Selain itu, metode ini akan sulit menerima fitur tambahan (fitur samping) yang sebelumnya tidak ada di data latih seperti fitur jumlah *votes*, dll.

**Train an Neural Network**
"""

class KDramaRecommendNet(tf.keras.Model):
 
  # Insialisasi fungsi
  def __init__(self, num_users, num_drama, embedding_size, **kwargs):
    super(KDramaRecommendNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_drama = num_drama
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.drama_embedding = layers.Embedding( # layer embeddings resto
        num_drama,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.drama_bias = layers.Embedding(num_drama, 1) # layer embedding resto bias
 
  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    drama_vector = self.drama_embedding(inputs[:, 1]) # memanggil layer embedding 3
    drama_bias = self.drama_bias(inputs[:, 1]) # memanggil layer embedding 4
 
    dot_user_drama = tf.tensordot(user_vector, drama_vector, 2) 
 
    x = dot_user_drama + user_bias + drama_bias
    
    return tf.nn.sigmoid(x) # activation sigmoid

model = KDramaRecommendNet(num_users, num_drama, 50) # inisialisasi model
 
# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

# Memulai training
 
history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('Model Metrics')
plt.ylabel('Root Mean-Squared Error')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper right')

plt.tight_layout()
plt.savefig('model_metrics.png')
plt.show()

"""**Lakukan Rekomendasi**"""

df2 = data2.copy()

# Mengambil sample user
user_id = df2['User ID'].sample(1).iloc[0]
drama_rated_by_user = df2[df2['User ID'] == user_id]
 
# Operator bitwise (~)
drama_not_rated = df2[~df2['Title'].isin(drama_rated_by_user.Title.values)]['Title'] 
drama_not_rated = list(
    set(drama_not_rated)
    .intersection(set(drama_to_drama_encoded.keys()))
)
 
drama_not_rated = [[drama_to_drama_encoded.get(x)] for x in drama_not_rated]
user_encoder = user_to_user_encoded.get(user_id)
user_drama_array = np.hstack(
    ([[user_encoder]] * len(drama_not_rated), drama_not_rated)
)

ratings = model.predict(user_drama_array).flatten()
 
top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_drama_ids = [
    drama_encoded_to_drama.get(drama_not_rated[x][0]) for x in top_ratings_indices
]
 
print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Drama with high ratings from user')
print('----' * 8)
 
top_drama_user = (
    drama_rated_by_user.sort_values(
        by = 'Rating',
        ascending=False
    )
    .head(5)
    .Title.values
)
 
drama_df_rows = df1[df1['Title'].isin(top_drama_user)]
for row in drama_df_rows.itertuples():
    print(row.Title, ':', row.Genre)
 
print('----' * 8)
print('Top drama recommendation')
print('----' * 8)
 
recommended_drama = df1[df1['Title'].isin(recommended_drama_ids)]
for row in recommended_drama.itertuples():
    print(row.Title, ':', row.Genre)

"""## Evaluation"""

# Menampilkan RMSE untuk Collaboratibe Filtering
val_rmse = history.history['val_root_mean_squared_error'][-1]
train_rmse = history.history['root_mean_squared_error'][-1]

rmse_dict = {'train' : train_rmse, 'validation': val_rmse}

metrics_df = pd.DataFrame(rmse_dict, index = ['Colaborative RMSE'])
metrics_df

count = 0

for i in kdrama_recommendations(title_idx)['Genre']:
  positive = 0
  for j in df1[df1.Title.eq(title_idx)].loc[idx, 'Genre'].split(','):
    # Cek apakah ada kecocokan genre, minimal 1 yang cocok
    if (i.find(j) >= 0):
      positive += 1
  
  # Jika ada yang cocok, tambahkan satu
  if (positive > 0):
    count +=1 

precision = 100*(count/5)
prec_dict = {'Positive' : count, 'Negative': 5-count, 'Precision': precision}

metrics_df2 = pd.DataFrame(prec_dict, index = ['Content Prec'])
metrics_df2

"""Untuk mengukur keberhasilan sistem rekomendasi yang dibuat, digunakan dua metrik:
1. *Root Mean Squared Error* (RMSE) untuk Collaborative Filtering
2. Presisi untuk Content-Based Filtering 

RMSE memberi informasi terkait seberapa besar kesalahan prediksi (*error*) dari model. Kesalahan prediksi diperoleh dengan menghitung selisih dari data prediksi terhadap data sebenarnya. RMSE dihitung dengan mengikuti persamaan di bawah:

$$ MSE = \frac{1}{N} \sum (y_{true} - y_{pred})^2 $$<br>
$$ RMSE = \sqrt{MSE} $$ <br>

Sementara itu, presisi mengukur seberapa tepat sistem rekomendasi dalam menentukan jenis konten yang direkomendasikan. Presisi pada proyek ini diukur dengan melihat genre dari konten yang direkomendasikan dan membandingkannya dengan genre konten yang dimasukkan ke sistem. Apabila ada satu kecocokan, meskipun hanya pada satu genre, prediksi tersebut akan dianggap sebagai *positif*. Sementara itu, apabila tidak ada kecocokan sama sekali, maka prediksi dianggap *negatif*. Presisi kemudian dihitung dengan membandingkan jumlah prediksi positif terhadap total prediksi:

$$ Presisi = \frac{Total Prediksi Positif}{Total Prediksi} \times 100 $$ <br>

Pada proyek ini, sistem rekomendasi dengan tipe Collaborative Filtering memiliki nilai RMSE latih dan validasi masing-masing sebesar 0.043 dan 0.292. Hal ini menunjukkan bahwa model belum memiliki kemampuan generalisasi yang baik dilihat dari RMSE validasi yang masih cukup besar. Hal ini membuka peluang peningkatan kinerja model. Meskipun demikian, model ini tetap mampu memberikan rekomendasi K-Drama meskipun dengan nilai kesalahan yang tidak kecil.

Sementara itu, untuk tipe Content-Based Filtering, sistem rekomendasi yang dibangun berhasil mencapai presisi sebesar 100 persen. Hal ini menunjukkan bahwa model ini memiliki kinerja yang sangat baik untuk memberikan rekomendasi konten K-Drama.

Dengan demikian, proyek ini dapat dikatakan telah mampu menghasilkan dua sistem rekomendasi yang fungsional meskipun dengan kinerja yang masih dapat ditingkatkan. Sistem rekomendasi ini dapat dimanfaatkan untuk berbagai layanan yang menyediakan konten hiburan berisi K-Drama.


"""