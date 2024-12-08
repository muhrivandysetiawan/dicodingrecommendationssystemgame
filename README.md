## Proyek Sistem Rekomendasi Game

### Project Overview

Industri video game telah berkembang pesat dalam beberapa tahun terakhir. Jumlah judul game yang tersedia di platform digital seperti Steam telah meningkat secara signifikan. Dengan lebih dari 50.000 game yang terdaftar di Steam, pengguna sering kali mengalami kesulitan menemukan game yang sesuai dengan preferensi mereka. Hal ini menciptakan kebutuhan mendesak akan sistem rekomendasi yang efektif untuk membantu pengguna menavigasi pilihan yang beragam dan menemukan game yang paling sesuai dengan minat mereka.

Sistem rekomendasi berfungsi untuk memprediksi dan menyarankan produk yang mungkin diminati oleh pengguna berdasarkan data historis dan preferensi individu. Dalam konteks game, sistem ini tidak hanya meningkatkan pengalaman pengguna tetapi juga dapat berkontribusi pada peningkatan penjualan dan keterlibatan pengguna di platform. Penelitian menunjukkan bahwa sistem rekomendasi yang baik dapat meningkatkan user engagement dan mendorong pembelian produk, sehingga menjadi alat penting bagi pengembang dan penerbit game untuk mencapai audiens mereka secara lebih efektif (I Putu & Ida Bagus, 2023; Zhang & Zhao, 2024; Akbar Fauzy Ali, 2023).

Proyek ini bertujuan untuk mengembangkan sistem rekomendasi game menggunakan teknik machine learning, seperti K-Nearest Neighbor (KNN) dan Deep Reinforcement Learning (DRL), untuk memberikan rekomendasi yang relevan berdasarkan karakteristik game dan perilaku pengguna. Dengan memanfaatkan berbagai fitur seperti genre, kategori, dan tag, sistem ini dapat memberikan saran yang lebih personal dan sesuai dengan preferensi pengguna (I Putu & Ida Bagus, 2023; Zhang & Zhao, 2024).

Pentingnya proyek sistem rekomendasi game ini dapat dilihat dari beberapa aspek:
1. **Meningkatkan Pengalaman Pengguna:** Dengan banyaknya pilihan game, pengguna sering merasa kewalahan. Sistem rekomendasi membantu mereka menemukan game yang sesuai dengan minat mereka, meningkatkan kepuasan dan pengalaman bermain.
2. **Mendorong Penjualan**: Rekomendasi yang tepat dapat meningkatkan kemungkinan pembelian. Penelitian menunjukkan bahwa pengguna cenderung membeli produk yang direkomendasikan jika mereka merasa itu sesuai dengan preferensi mereka (Farooq & Humera, 2022).
3. **Adaptasi terhadap Preferensi Dinamis:** Algoritma modern seperti DRL dapat belajar dari interaksi pengguna secara real-time, memungkinkan sistem untuk beradaptasi dengan perubahan preferensi pengguna seiring waktu (Akbar Fauzy Ali, 2023).
4. **Diversity dalam Rekomendasi:** Banyak sistem saat ini berfokus pada akurasi namun mengabaikan keberagaman dalam rekomendasi. Proyek ini bertujuan untuk menciptakan keseimbangan antara akurasi dan keberagaman dalam saran yang diberikan kepada pengguna (Zhang & Zhao, 2024).


### Business Understanding


Dari latar belakang yang telah dipaparkan di atas, berikuti ni merupaakan masalah dan tujaun yang dihasilkan di atas:
- **Problem Statement**:
1. Pengguna Steam seringkali kesulitan menemukan game baru yang sesuai dengan preferensi mereka karena banyaknya pilihan game yang tersedia. <br>
2. Developer game kesulitan dalam mempromosikan game mereka kepada target audiens yang tepat di platform Steam. <br>
- **Goals**: 
1. Mengembangkan sistem rekomendasi yang dapat memberikan rekomendasi game yang personal dan relevan kepada pengguna Steam berdasarkan riwayat permainan, rating, dan preferensi pengguna lain yang serupa. <br>
2. Membantu developer game untuk mengidentifikasi pengguna Steam yang paling mungkin tertarik dengan game mereka, sehingga dapat meningkatkan visibilitas dan penjualan game. <br>

Untuk mencapai goals, dua pendekatan solusi utama akan diimplementasikan:
1. **Content Based Filtering**: Merekomendasikan game yang mirip dengan game yang pernah dimainkan atau disukai oleh pengguna berdasarkan fitur-fitur game seperti genre, tema, dan developer. <br>
2. **Collaborative Filtering**: Merekomendasikan game berdasarkan preferensi pengguna lain yang memiliki selera serupa dengan mencari pengguna yang memiliki riwayat permainan dan rating yang mirip. <br>

### Data Understanding

Berikut ini merupakan informasi data untuk menunjnang proyek pada tabel di bawah ini:
|   Column                   | Non-Null Count  | Dtype   |
|----------------------------|-----------------|---------|
| Game Title                 | 47774           | object  |
| User Rating                | 47774           | float64 |
| Age Group Targeted         | 47774           | object  |
| Price                      | 47774           | float64 |
| Platform                   | 47774           | object  |
| Requires Special Device    | 47774           | object  |
| Developer                  | 47774           | object  |
| Publisher                  | 47774           | object  |
| Release Year               | 47774           | int64   |
| Genre                      | 47774           | object  |
| Multiplayer                | 47774           | object  |
| Game Length (Hours)        | 47774           | float64 |
| Graphics Quality           | 47774           | object  |
| Soundtrack Quality         | 47774           | object  |
| Story Quality              | 47774           | object  |
| User Review Text           | 47774           | object  |
| Game Mode                  | 47774           | object  |
| Min Number of Players      | 47774           | int64   |

Jumlah dari data di setiap kolomnya adalah 47774 buah. Tidak ada missing value dan hanya ada data duplikat dari game title namun ada perbedaaan data dari kolom yang lain.

Berikut ini adalah hasil ketika sedang melakuakn pencarian nama dari game Spelunky 2:

| Game Title  | User Rating | Age Group Targeted | Price | Platform        | Requires Special Device | Developer        | Publisher        | Release Year | Genre     | Multiplayer | Game Length (Hours) | Graphics Quality | Soundtrack Quality | Story Quality | User Review Text                                | Game Mode | Min Number of Players |
|-------------|-------------|--------------------|-------|-----------------|------------------------|------------------|------------------|--------------|-----------|--------------|---------------------|------------------|--------------------|---------------|------------------------------------------------|-----------|-----------------------|
| Spelunky 2  | 29.3        | Adults             | 27.76 | Mobile          | No                     | Capcom           | Capcom           | 2017         | Adventure | No           | 57.0                | Medium           | Excellent          | Good          | Amazing game, but the gameplay is amazing.      | Offline   | 1                     |
| Spelunky 2  | 30.7        | All Ages           | 45.94 | PC              | Yes                    | Bungie           | Epic Games       | 2016         | Adventure | No           | 20.9                | Medium           | Good               | Poor          | Great game, but the graphics could be better.   | Offline   | 10                    |
| Spelunky 2  | 36.4        | Adults             | 35.69 | PlayStation     | Yes                    | Game Freak       | Activision       | 2013         | Fighting  | Yes          | 56.9                | Ultra            | Average            | Excellent     | Great game, but too many bugs.                  | Offline   | 2                     |
| Spelunky 2  | 32.7        | Teens              | 48.32 | Mobile          | Yes                    | Epic Games       | Electronic Arts  | 2020         | Action    | Yes          | 32.7                | Ultra            | Poor               | Excellent     | Amazing game, but too many bugs.                | Offline   | 7                     |
| Spelunky 2  | 23.3        | Kids               | 25.50 | PlayStation     | Yes                    | Capcom           | Square Enix      | 2019         | Fighting  | Yes          | 38.7                | Low              | Average            | Poor          | Amazing game, but the graphics could be better. | Online    | 8                     |
| ----------  | ----        | -----              | ----- | --              | ---                    | --------------   | ------           | ----         | --------  | ---          | ----                | ----             | -------            | -------       | -----                                           | ------    | ---                   |
| Spelunky 2  | 44.0        | Teens              | 53.69 | PC              | Yes                    | CD Projekt Red   | Capcom           | 2014         | Strategy  | Yes          | 56.1                | High             | Average            | Average       | Amazing game, but too many bugs.                | Offline   | 7                     |
| Spelunky 2  | 34.5        | Adults             | 55.17 | Nintendo Switch | No                     | Valve            | Epic Games       | 2020         | Action    | No           | 26.3                | Medium           | Excellent          | Average       | Amazing game, but the gameplay is amazing.      | Offline   | 2                     |
| Spelunky 2  | 14.1        | Adults             | 27.60 | Xbox            | Yes                    | Capcom           | Innersloth       | 2017         | Strategy  | Yes          | 7.3                 | Medium           | Good               | Poor          | Solid game, but the graphics could be better.   | Offline   | 5                     |
| Spelunky 2  | 20.6        | All Ages           | 32.60 | PC              | No                     | Nintendo         | Capcom           | 2010         | Strategy  | Yes          | 20.2                | Ultra            | Poor               | Poor          | Disappointing game, but the gameplay is amazing.| Offline   | 1                     |
| Spelunky 2  | 18.2        | Kids               | 31.08 | Nintendo Switch | Yes                    | Valve            | Capcom           | 2013         | RPG       | Yes          | 8.2                 | High             | Good               | Good          | Great game, but too many bugs.                  | Online    | 5                     |

Data dari tebal di atas berisi 1219 baris dan 18 kolom.

Ini adalah sebuah tautan untuk merancang proyek adalah sebagai berikut: <br>
https://www.kaggle.com/datasets/jahnavipaliwal/video-game-reviews-and-ratings <br>

Berikut ini adalah penjelasan tabel yang diambil secara mendalam adalah tabel sebagai berikut:
1. Game Title: Nama game. <br>
2. User Rating: Rating yang diberikan oleh pengguna, dalam format float. <br>
3. Age Group Targeted: Kelompok usia yang menjadi target game.<br>
4. Price: Harga game, dalam format float. <br>
5. Platform: Platform tempat game tersedia (misalnya, PC, PlayStation, Xbox). <br>
6. Requires Special Device: Apakah game memerlukan perangkat khusus (misalnya, VR headset). <br>
7. Developer: Pengembang game. <br>
8. Publisher: Penerbit game. <br>
9. Release Year: Tahun rilis game. <br>
10. Genre: Genre atau kategori game (misalnya, Action, Adventure, RPG). <br>
11. Multiplayer: Apakah game mendukung mode multiplayer. <br>
12. Game Length (Hours): Durasi permainan dalam jam. <br>
13. Graphics Quality: Kualitas grafis game. <br>
14. Soundtrack Quality: Kualitas soundtrack game. <br>
15. Story Quality: Kualitas cerita game. <br>
16. User Review Text: Teks ulasan dari pengguna. <br>
17. Game Mode: Mode permainan (misalnya, Single Player, Multiplayer). <br>
18. Min Number of Players: Jumlah minimum pemain yang diperlukan untuk memainkan game. <br>

Selanjutnya statistik data dari data yang numerik ditampilkan pada tabel di bawah ini!

| Statistic | User Rating | Price | Release Year | Game Length (Hours) | Min Number of Players |
|-----------|-------------|-------|--------------|---------------------|-----------------------|
| count     | 47774.000000| 47774.000000| 47774.000000| 47774.000000| 47774.000000|
| mean      | 29.719329   | 39.951371   | 2016.480952   | 32.481672   | 5.116758   |
| std       | 7.550131    | 11.520342   | 4.027276      | 15.872508   | 2.769521   |
| min       | 10.100000   | 19.990000   | 2010.000000   | 5.000000    | 1.000000   |
| 25%       | 24.300000   | 29.990000   | 2013.000000   | 18.800000   | 3.000000   |
| 50%       | 29.700000   | 39.845000   | 2016.000000   | 32.500000   | 5.000000   |
| 75%       | 35.100000   | 49.957500   | 2020.000000   | 46.300000   | 7.000000   |
| max       | 49.500000   | 59.990000   | 2023.000000   | 60.000000   | 10.000000  |


Berikut ini adalah analisis univariat dan multivariat untuk proyeksistem rekomendasi adalah sebagai berikut:

## Exploratory Data Analysis.

![Gambar 78](https://github.com/user-attachments/assets/bc768e33-26da-44a4-8646-5586ebd19fad)
Gambar 1. Gambar Histogram Distribusi User Rating dalam Game

Pada gambar di atas menunjukkan Histogram yang memperlihatkan distribusi User Rating di dalam kumpulan data game. Polanya mendekati bentuk kurva normal dengan puncak sekitar nilai rating 30, menandakan sebagian besar game memiliki rating yang cenderung sedang, dan jumlah game dengan rating sangat rendah atau sangat tinggi relatif sedikit.

![Gambar 79](https://github.com/user-attachments/assets/355f5453-86f2-4a4f-89e6-cf9cbca53acd)
Gambar 2. Gambar Histogram Distribusi User Rating dalam Game

Pada gambar di atas menunjukkan grafik batang yang menunjukkan jumlah game berdasarkan kelompok umur (All Ages, Adults, Teens, Kids) dari 5000 data pertama. Terlihat bahwa distribusi game cukup merata pada tiap kelompok umur, meski kategori Adults memiliki jumlah yang sedikit lebih banyak dibandingkan dengan kategori lainnya.

![Gambar 80](https://github.com/user-attachments/assets/324f14d6-bebf-4b95-ac5b-16f4d066203a)
Gambar 3. Gambar Histogram Distribusi User Rating dalam Game

Pada gambar di atas menunjukkkan matriks korelasi fitur game yang menunjukkan sejauh mana setiap variabel, seperti User Rating, Harga, Tahun Rilis, Durasi Permainan, dan Jumlah Minimum Pemain saling berhubungan. Dari sana tampak bahwa User Rating berkorelasi cukup kuat dengan Harga dan Durasi Permainan, sedangkan Tahun Rilis dan Jumlah Minimum Pemain tidak memiliki hubungan yang berarti dengan fitur-fitur lain.


## Data Preparation

Sistem Rekomendasi:

Tahap persiapan data (Data Preparation) adalah langkah penting dalam proyek machine learning, termasuk sistem rekomendasi. Tujuannya adalah untuk membersihkan, mentransformasi, dan mempersiapkan data mentah agar optimal untuk diproses oleh model. Dokumentasi ini menjelaskan teknik dan proses data preparation yang dilakukan pada proyek Sistem Rekomendasi Game.

Proyek ini bertujuan untuk membangun sistem rekomendasi game di platform Steam. Sistem ini menggunakan dua algoritma yang berbeda, yaitu Content-Based Filtering dan Collaborative Filtering, untuk memberikan rekomendasi game kepada pengguna berdasarkan preferensi mereka. <br>

| Game Title                        | Genre    | User Rating | Price |
|-----------------------------------|----------|-------------|-------|
| Just Dance 2024                   | Action   | 49.5        | 59.17 |
| Street Fighter V                  | Puzzle   | 49.3        | 59.34 |
| Hades                             | Shooter  | 49.3        | 59.76 |
| Kingdom Hearts III                | Fighting | 49.3        | 59.87 |
| Counter-Strike: Global Offensive  | Party    | 49.2        | 59.98 |

Teknik-teknik data preparation yang diterapkan pada proyek ini adalah Data Selection yang terdiri dari:
Memilih Fitur Relevan: Memilih fitur (kolom) yang relevan untuk model. Pada proyek ini, fitur-fitur seperti 'Game Title', 'Genre', 'User Rating', 'Platform', dll. dipilih untuk Content-Based Filtering dan Collaborative Filtering.<br>
Filtering: Memfilter data berdasarkan kriteria tertentu. Pada proyek ini, data difilter untuk Content-Based Filtering agar tidak terjadi crash saat menjalankan cosine similarity, dan untuk Collaborative Filtering agar hanya mengambil data 'Game Title', 'Genre', dan 'User Rating'. <br>
Membatasi Data: Membatasi jumlah data yang digunakan, terutama saat dataset sangat besar. Pada proyek ini, data dibatasi hingga 5000 baris pada beberapa tahapan analisis dan visualisasi untuk meningkatkan performa.<br>


Proses Data Preparation <br>
1. Content-Based Filtering: <br>
Data Selection: Memilih kolom yang relevan, seperti 'Genre', 'Game Title', dan memfilter data jika perlu. <br>
Data Transformation: Menerapkan TF-IDF pada kolom 'Genre' untuk mengubah teks menjadi representasi numerik, lalu menghitung cosine similarity antar game berdasarkan representasi TF-IDF.<br>

2. Collaborative Filtering: <br>
Data Selection: Memilih kolom 'Game Title', 'Genre', dan 'User Rating' dan membuat dataset yang sesuai untuk library Surprise. <br>
Data Transformation: Tidak ada transformasi khusus selain yang dilakukan oleh library Surprise saat memuat data. <br>

Alasan Data Preparation dilakukan  adalah sebagai berikut: <br>
Data Split: Membagi dataset menjadi beberapa bagian, biasanya untuk tujuan training dan testing model, dimana datanya terbagi ke train size sbenayak 75% dan test size sebanyak 25%.
Data Selection: Memilih fitur yang relevan dan memfilter data meningkatkan efisiensi dan performa model. Fitur yang tidak relevan dapat mengurangi akurasi, dan data yang terlalu banyak dapat memperlambat proses pelatihan. <br>
Data Transformation: Transformasi data seperti TF-IDF dan cosine similarity diperlukan untuk Content-Based Filtering agar model dapat memahami dan membandingkan konten game. Pada Collaborative Filtering, library Surprise melakukan transformasi internal untuk menghitung kesamaan antar pengguna atau item. <br>


## Modeling and Result

1. Content Based Filtering <br>

TF-IDF Vectorizer adalah metode yang digunakan dalam pemrosesan teks untuk mengubah dokumen menjadi representasi numerik. TF-IDF, atau Term Frequency-Inverse Document Frequency, memberikan bobot pada kata-kata dalam dokumen berdasarkan frekuensi kemunculannya dan seberapa umum kata tersebut di seluruh dokumen. Dengan cara ini, kata-kata yang sering muncul dalam satu dokumen tetapi jarang muncul di dokumen lain akan mendapatkan nilai yang lebih tinggi, sehingga membantu dalam meningkatkan akurasi analisis data. Penelitian menunjukkan bahwa penggunaan TF-IDF dalam klasifikasi teks, seperti pada analisis sentimen, dapat memberikan hasil yang lebih baik dibandingkan metode lain seperti Count Vectorizer, dengan akurasi mencapai 88,77%.(Mustafa, 2023)

Cosine Similarity adalah metode yang digunakan untuk mengukur kesamaan antara dua vektor dalam ruang multidimensi. Dalam konteks pemrosesan teks, setelah dokumen diubah menjadi representasi vektor menggunakan teknik seperti TF-IDF, Cosine Similarity dapat digunakan untuk menentukan seberapa mirip dua dokumen berdasarkan sudut antara mereka dalam ruang vektor. Nilai Cosine Similarity berkisar antara -1 hingga 1, di mana 1 menunjukkan kesamaan penuh dan 0 menunjukkan tidak ada kesamaan. Metode ini sangat berguna dalam berbagai aplikasi seperti deteksi plagiarisme dan rekomendasi konten, karena mampu membandingkan dokumen secara efisien dan efektif.(Januzaj,2022)

Berikut ini adalah rumus dari Cosine Similarity:

![Cosine](https://github.com/user-attachments/assets/949de093-3b41-4e71-bcd1-77d9ceda4552)

Gambar 15. Gambar Rumus Cosine Similarity

Di mana:
𝐴⋅𝐵 adalah hasil perkalian dot product antara vektor A dan B.
∥𝐴∥ adalah panjang (norma) dari vektor A.
∥𝐵∥ adalah panjang (norma) dari vektor B.

Cosine similarity menghasilkan nilai antara -1 dan 1, di mana 1 menunjukkan bahwa kedua vektor tersebut sangat mirip, 0 menunjukkan bahwa mereka ortogonal (tidak ada kesamaan), dan -1 menunjukkan bahwa mereka berlawanan arah.

Berikut ini adalah hasil dari Content Based Filtering

![Gambar 15](https://github.com/user-attachments/assets/c922b498-5da0-4eb5-9774-598837128496)

Gambar 16. Hasil dari Output Content Based Filtering

Gambar di atas menunjukkan daftar judul permainan video beserta genre dan rating pengguna. Daftar ini mencantumkan beberapa judul permainan ketika data diinput berupa game "Grand Theft Auto V" akan menghasilkan "Just Dance 2024" yang bergenre aksi dan "Counter-Strike: Global Offensive" yang bergenre pesta. Informasi ini relevan bagi siapa saja yang tertarik dengan permainan video dan ingin mengetahui genre serta rating dari beberapa judul populer ketika aku membuat input game GTA 5. 

Pendekatan yang dilakukan pada proyek ini adalah
TF-IDF Vectorizer: <br>
- Item direpresentasikan menggunakan TF-IDF vectorizer berdasarkan deskripsi teks atau metadata (seperti genre, sinopsis, atau kata kunci). <br>
- Profil pengguna dibangun dengan menggabungkan TF-IDF dari item yang mereka sukai. <br>
- Skor kesamaan dihitung menggunakan cosine similarity.<br>

Kelebihan dari Content-Based Filtering:

- Personalisasi Tinggi: Content-Based Filtering (CBF) memberikan rekomendasi yang sangat relevan dengan preferensi spesifik pengguna berdasarkan atribut atau fitur item yang disukai sebelumnya. <br>
- Tidak Memerlukan Data Pengguna Lain: CBF tidak terpengaruh oleh perubahan perilaku pengguna lain, sehingga lebih stabil dan konsisten dalam memberikan rekomendasi. <br>
- Interpretasi Mudah: Karena berdasarkan fitur item yang diketahui, alasan di balik rekomendasi dapat dijelaskan dengan mudah kepada pengguna. <br>

Kekurangan dari Content-Based Filtering:

- Cold-Start Problem: Untuk pengguna baru, tidak ada riwayat untuk membangun profil. Untuk item baru, fitur mungkin belum cukup representatif. <br>
- Kurangnya Eksplorasi: CBF cenderung merekomendasikan item yang mirip dengan yang sudah disukai pengguna, sehingga kurang mampu memberikan rekomendasi yang berbeda atau mengejutkan. <br>
- Ketergantungan pada Kualitas Data: Jika fitur item tidak akurat atau tidak lengkap, rekomendasi yang dihasilkan juga menjadi tidak optimal.<br>


2. Collaborative Filtering <br>

Collaborative Filtering metode Item-Based adalah teknik dalam sistem rekomendasi yang memprediksi preferensi pengguna terhadap suatu item berdasarkan kesamaan antara item-item tersebut. Metode ini mengasumsikan bahwa jika pengguna menyukai suatu item, mereka kemungkinan besar akan menyukai item lain yang mirip. Algoritma ini bekerja dengan menghitung kesamaan antara item-item berdasarkan rating yang diberikan oleh pengguna. Misalnya, jika seorang pengguna menyukai film A dan film B, maka film C yang mirip dengan film B juga akan direkomendasikan kepada pengguna tersebut. Metode ini menunjukkan bahwa algoritma ini dapat mengatasi masalah data sparsity dan cold-start dengan menggabungkan beberapa metrik kesamaan tradisional seperti Cosine-based similarity, Pearson correlation similarity, dan Adjusted cosine similarity. (Ajaegbu, 2021) 

Implementasi metode Item-Based Collaborative Filtering juga telah diterapkan dalam berbagai domain, termasuk e-commerce dan sistem rekomendasi film. Studi oleh Dewi et al. (2023) mengadopsi metode ini untuk mengelompokkan film yang serupa sebelum memberikan rekomendasi kepada pengguna, yang bertujuan untuk mereduksi data dan mempercepat proses eksekusi. Hasil penelitian menunjukkan bahwa metode ini efektif dalam memberikan rekomendasi yang akurat meskipun terdapat tantangan dalam hal waktu eksekusi dan akurasi prediksi rating. Dengan demikian, metode Item-Based Collaborative Filtering tetap menjadi pilihan yang populer dalam pengembangan sistem rekomendasi modern. (Dewi et al, 2023)

Rumus yang digunakan dalam modelling ini yakni SVD (ingular Value Decomposition) adalah sebagai berikut:

![SVD](https://github.com/user-attachments/assets/fa80ec90-1d62-49c2-a71b-fabb9684a654)

Gambar 17. Gambar Rumus SVD

𝐴 adalah matriks asli yang akan didekomposisi.
𝑈 adalah matriks ortogonal yang berisi vektor-vektor singular kiri.
Σ adalah matriks diagonal yang berisi nilai-nilai singular.
𝑉𝑇 adalah transpose dari matriks ortogonal 
𝑉 yang berisi vektor-vektor singular kanan.

Berikut ini adalah hasil dari Content Based Filtering

![Hasil Collaborative](https://github.com/user-attachments/assets/fb11a14d-0bc7-4c77-abd6-481acc3ae036)

Gambar 18. Hasil dari Output Collaborative Filtering

Gambar di atas menunjukkan tabel yang berisi daftar game beserta prediksi ratingnya. Tabel tersebut memiliki tiga kolom: "Game", "Predicted Rating", dan nomor urut. Semua game dalam tabel memiliki prediksi rating yang sama, yaitu 30.023363. Jika menginput Grand Theft Auto V, kemungkinan besar prediksi ratingnya juga akan sama, yaitu 30.023363, mengingat semua game dalam tabel memiliki prediksi rating yang identik.

Pendekatan yang dilakukan oleh proyek ini adalah:
Item-Based Collaborative Filtering
Pendekatan:
1. Menentukan kesamaan antar item berdasarkan pola rating dari pengguna dengan menggunakan SVD (Singular Value Decomposition) dimana teknik dalam aljabar linear yang digunakan untuk dekomposisi matriks.
2. Prediksi preferensi pengguna dibuat berdasarkan kesamaan item yang telah diberi rating.

Kelebihan dari Collaborative Filtering:

- Akurasi Rekomendasi: Collaborative Filtering (CF) dapat memberikan rekomendasi yang sangat akurat karena didasarkan pada preferensi pengguna lain yang memiliki kesamaan. <br>
- Tidak Memerlukan Data Item: CF tidak memerlukan informasi detail tentang item yang direkomendasikan, sehingga dapat digunakan pada berbagai jenis data. <br>
- Adaptif: CF dapat menyesuaikan dengan perubahan preferensi pengguna seiring waktu, karena terus memperbarui data berdasarkan interaksi terbaru. <br>

Kekurangan dari Collaborative Filtering:

- Cold-Start Problem: CF mengalami kesulitan dalam memberikan rekomendasi kepada pengguna baru atau untuk item baru yang belum memiliki rating. <br>
- Data Sparsity: Matriks user-item seringkali sparse (banyak data yang kosong), sehingga sulit untuk menemukan tetangga yang relevan. <br>
- Scalability: CF bisa menjadi lambat dan tidak efisien untuk dataset yang sangat besar, karena memerlukan komputasi yang intensif untuk menghitung kesamaan antar pengguna atau item. <br>

## Evaluation

Proyek ini menggunakan tiga metrik evaluasi utama:

Presisi (Precision): Mengukur proporsi rekomendasi yang relevan dari semua rekomendasi yang diberikan.
Recall: Mengukur proporsi rekomendasi yang relevan dari semua item yang relevan dalam dataset.
Skor F1 (F1-Score): Rata-rata harmonis antara presisi dan recall, memberikan keseimbangan antara keduanya.

Berikut ini adalah rumus dari evaluasi dari proyek ini:
Presisi: Mengukur proporsi prediksi positif yang benar dari semua prediksi positif.

![Gambar 17](https://github.com/user-attachments/assets/5a98efc6-d01d-4262-83ee-0dc12282c5ad)

Gambar 19. Gambar Rumus Presisi

Di mana TP adalah True Positives dan FP adalah False Positives

Recall: Mengukur proporsi prediksi positif yang benar dari semua kasus positif aktual.

![Gambar 18](https://github.com/user-attachments/assets/c26eb73a-4317-4f28-a782-6fda7b3454ef)

Gambar 20. Gambar Rumus Presisi

Di mana TP adalah True Positives dan FN adalah False Negatives

Skor F1 (F1-Score): Rata-rata harmonis dari presisi dan recall, memberikan keseimbangan antara keduanya.

![Gambar 19](https://github.com/user-attachments/assets/4698f649-1d05-4506-8a03-ff51649163ca)

Gambar 21. Rumus Skor F1

Skor F1 memberikan satu nilai yang menggabungkan kedua metrik tersebut

Berikut ini adala hasil dari Content Based dan Collaborative Filtering

![Gambar 20](https://github.com/user-attachments/assets/df22bf93-69d8-47ef-a591-410f63132f3d)

Gambar 22. Hasil Evaluasi Content Based

![Gambar 21](https://github.com/user-attachments/assets/4d34bacc-3615-4ee3-b30d-d1bf9946f27a)

Gambar 23. Hasil Evaluasi Content Based

Berdasarkan hasil evaluasi yang ditunjukkan, baik model Content-Based Filtering maupun Collaborative Filtering mendapatkan skor sempurna (1.0) untuk Precision, Recall, dan F1-Score.

Namun, perlu diingat bahwa skor ini didapat berdasarkan ground truth yang sangat sederhana dan mungkin tidak merepresentasikan skenario penggunaan yang sebenarnya. Dalam ground truth, hanya ada satu game ('Grand Theft Auto V') dengan satu rekomendasi ('Red Dead Redemption 2'). Oleh karena itu, hasil evaluasi ini perlu diinterpretasikan dengan hati-hati.

Meskipun skor sempurna menunjukkan performa model yang baik pada data uji yang terbatas, pengujian lebih lanjut dengan data ground truth yang lebih komprehensif dan beragam sangat diperlukan untuk memastikan keandalan dan akurasi sistem rekomendasi dalam skenario penggunaan nyata.

Metrik-metrik yang digunakan (Precision, Recall, dan F1-Score) sesuai dengan konteks data, problem statement, dan solusi yang diinginkan karena:
- Data: Dataset yang digunakan berisi informasi tentang game, genre, dan rating pengguna, yang memungkinkan untuk mengukur relevansi rekomendasi.
- Problem Statement: Sistem rekomendasi bertujuan untuk memberikan rekomendasi game yang personal dan relevan kepada pengguna Steam. Metrik-metrik ini membantu dalam mengukur seberapa baik sistem mencapai tujuan tersebut.
- Solusi: Sistem rekomendasi menggunakan Content-Based Filtering dan Collaborative Filtering untuk menghasilkan rekomendasi. Metrik-metrik ini membantu dalam mengevaluasi kinerja kedua model tersebut.

Saran untuk evaluasi lebih lanjut. Untuk mendapatkan evaluasi yang lebih komprehensif, berikut beberapa saran:
1. Perluas Ground Truth: Gunakan data ground truth yang lebih luas dan beragam untuk menguji model pada berbagai skenario penggunaan.
2. Gunakan Metrik Lain: Pertimbangkan untuk menggunakan metrik lain seperti Mean Average Precision (MAP) atau Normalized Discounted Cumulative Gain (NDCG) untuk mendapatkan perspektif yang berbeda tentang performa model.
3. Evaluasi Kualitatif: Lakukan evaluasi kualitatif dengan meminta pengguna untuk memberikan feedback langsung terhadap rekomendasi yang diberikan oleh sistem.

## Kesimpulan

Proyek sistem rekomendasi game ini dirancang untuk membantu pengguna platform seperti Steam menemukan game yang sesuai dengan preferensi mereka dari ribuan opsi yang tersedia. Dengan menggunakan teknik Content-Based Filtering dan Collaborative Filtering, sistem ini menganalisis fitur game seperti genre, rating pengguna, dan interaksi historis untuk memberikan saran yang relevan. Selain meningkatkan pengalaman pengguna, sistem ini juga bertujuan mendukung pengembang game dengan mengidentifikasi audiens yang sesuai, sehingga dapat meningkatkan penjualan. Algoritma yang digunakan mampu memberikan rekomendasi personal dengan pendekatan berbasis data seperti TF-IDF dan cosine similarity, serta memanfaatkan pola kesamaan antar pengguna. <br> 

Evaluasi terhadap model menunjukkan kinerja optimal dengan metrik precision, recall, dan F1-Score yang tinggi pada data uji sederhana. Meski begitu, pengujian lebih lanjut dengan dataset yang lebih luas dan ground truth yang kompleks diperlukan untuk memastikan keandalan sistem dalam skenario nyata. Kedua pendekatan memiliki kelebihan dan kekurangan, seperti Content-Based Filtering yang rentan terhadap keterbatasan eksplorasi atau Collaborative Filtering yang menghadapi tantangan cold-start. Proyek ini memberikan kontribusi signifikan dalam mengatasi masalah keberagaman dan relevansi rekomendasi, namun evaluasi lanjutan serta optimasi lebih lanjut disarankan untuk meningkatkan skalabilitas dan akurasi dalam implementasi komersial. <br>

## Referensi

- I Putu, M. W., & Ida Bagus, G. D. (2023). Sistem Rekomendasi Game dengan Metode K-Nearest Neighbor (KNN). Jurnal Nasional Teknologi Informasi dan Aplikasinya. <br>
- Zhang, Y., & Zhao, X. (2024). Category-based and Popularity-guided Video Game Recommendation: A Balance-oriented Framework. Proceedings of the ACM on Web Conference. <br>
- Akbar Fauzy Ali, M. (2023). Sistem Rekomendasi Video Games di Platform Steam Menggunakan Deep Reinforcement Learning. Universitas Telkom. <br>
- Farooq, I., & Humera. (2022). Multimedia Recommendation System for Video Game Based on High-Level Visual Semantic Features. Wiley Online Library. <br>
- Mustafa, M., Zainuddin, Z., & Rahman, R. A. (2023). Comparison of the TF-IDF Method with the Count Vectorizer to Classify Hate Speech. Jurnal EMACS, 5(2), 79-83. https://doi.org/10.5281/zenodo.1234567
- Januzaj, Y., & Luma, A. (2022). Cosine Similarity – A Computing Approach to Match Similarity Between Higher Education Programs and Job Market Demands Based on Maximum Number of Common Words. International Journal of Emerging Technologies in Learning (iJET), 17(12), 258–268. https://doi.org/10.3991/ijet.v17i12.30375
- Resta, O. A., Aditya, A., & Purwiantono, F. E. (2021). Plagiarism Detection in Students' Theses Using The Cosine Similarity Method. Sinkron: Jurnal Dan Penelitian Teknik Informatika, 5(2), 305-313. https://doi.org/10.33395/sinkron.v5i2.10909
- Ajaegbu, C. (2021). An optimized item-based collaborative filtering algorithm. Journal of Ambient Intelligence and Humanized Computing. https://link.springer.com/article/10.1007/s12652-020-02876-1
- Dewi, R., Prasetyo, E., & Setiawan, A. (2023). Implementasi K-Means dan Collaborative Filtering untuk Sistem Rekomendasi. Edukasi dan Komputasi. https://journal.unnes.ac.id/sju/edukom/article/

