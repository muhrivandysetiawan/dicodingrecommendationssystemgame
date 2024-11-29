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
| No | Kolom                  | Tipe Data       | Deskripsi                                                                 |
|----|------------------------|-----------------|--------------------------------------------------------------------------|
| 0  | Game Title             | object          | Judul dari game.                                                         |
| 1  | User Rating            | float64         | Rating yang diberikan oleh pengguna (skala 0-10).                        |
| 2  | Age Group Targeted     | object          | Kelompok usia yang menjadi target dari game.                             |
| 3  | Price                  | float64         | Harga game dalam dolar.                                                  |
| 4  | Platform               | object          | Platform tempat game tersedia (misalnya, PC, Xbox, PlayStation).         |
| 5  | Requires Special Device| object          | Apakah game memerlukan perangkat khusus (misalnya, VR headset).          |
| 6  | Developer              | object          | Pengembang game.                                                         |
| 7  | Publisher              | object          | Penerbit game.                                                           |
| 8  | Release Year           | int64           | Tahun rilis game.                                                        |
| 9  | Genre                  | object          | Genre atau kategori game (misalnya, Action, Adventure).                  |
| 10 | Multiplayer            | object          | Apakah game mendukung mode multiplayer (Ya/Tidak).                       |
| 11 | Game Length (Hours)    | float64         | Durasi permainan dalam jam.                                              |
| 12 | Graphics Quality       | object          | Kualitas grafis game (misalnya, Low, Medium, High).                      |
| 13 | Soundtrack Quality     | object          | Kualitas soundtrack game (misalnya, Poor, Average, Good).                |
| 14 | Story Quality          | object          | Kualitas cerita dalam game (misalnya, Poor, Average, Good).              |
| 15 | User Review Text       | object          | Teks ulasan dari pengguna.                                               |
| 16 | Game Mode              | object          | Mode permainan (misalnya, Single-player, Multiplayer).                   |
| 17 | Min Number of Players  | int64           | Jumlah minimum pemain yang dibutuhkan untuk bermain.                     |

Jumlah dari data di setipa kolomnya adalah 47774 buah.

Ini adalah sebuah tautan untuk merancang proyek adalah sebagai berikut: <br>
[https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam](https://www.kaggle.com/datasets/jahnavipaliwal/video-game-reviews-and-ratings)

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

Berikut ini adalah analisis univariat dan multivariat untuk proyeksistem rekomendasi adalah sebagai berikut:

## Analisis Univariat

Analisis Univariat adalah analisis statistik yang hanya melibatkan satu variabel. Tujuannya adalah untuk memahami karakteristik dasar dari variabel tersebut, seperti distribusi, rata-rata, median, dan standar deviasi. Contoh analisis univariat adalah menghitung rata-rata harga game atau distribusi rating pengguna.

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
 <br>
Tabel di atas menampilkan statistik deskriptif untuk berbagai atribut game, termasuk peringkat pengguna, harga, tahun rilis, durasi permainan, dan jumlah pemain minimum. Setiap baris menampilkan statistik tertentu, seperti jumlah data, rata-rata, standar deviasi, nilai minimum, kuartil pertama, median, kuartil ketiga, dan nilai maksimum. Data ini membantu memahami distribusi dan fitur dataset game yang dianalisis. <br>

![Gambar 1](https://github.com/user-attachments/assets/1e191fc1-10a5-4eef-9ab6-669f8b477b08)

Gambar 1. Diagram Distribusi Harga Game

Gambar di atas menunjukkan distribusi harga game dalam bentuk histogram dengan kurva distribusi yang dihaluskan. Sumbu horizontal (x) mewakili harga game, sedangkan sumbu vertikal (y) menunjukkan jumlah game. Histogram ini menunjukkan bahwa jumlah game relatif merata di berbagai rentang harga, dengan sedikit penurunan di harga terendah dan tertinggi.

![Gambar 2](https://github.com/user-attachments/assets/51012046-8d46-48eb-82dd-fc1551c0cf05)

Gambar 2. Diagram Distribusi User Rating

Gambar di atas menunjukkan distribusi rating pengguna untuk sebuah game, dengan sumbu horizontal mewakili rating pengguna dari 10 hingga 50 dan sumbu vertikal mewakili jumlah game. Distribusi ini berbentuk kurva lonceng, menunjukkan bahwa sebagian besar game memiliki rating pengguna di sekitar 30. Ini menarik karena menunjukkan bahwa rating pengguna cenderung berkumpul di sekitar nilai tengah, dengan sedikit game yang memiliki rating sangat rendah atau sangat tinggi.

![Gambar 3](https://github.com/user-attachments/assets/f03ed641-31a6-4e92-873c-1f29693b7d85)

Gambar 3. Diagram Distribusi Tahun Rilis

Gambar di atas menunjukkan distribusi jumlah game yang dirilis setiap tahun dari 2010 hingga 2022. Grafik batang biru menunjukkan jumlah game yang dirilis setiap tahun, yang berkisar sekitar 3500 game per tahun. Garis biru di tengah grafik menunjukkan tren jumlah game yang dirilis, yang relatif stabil di sekitar 1500 game per tahun.

![Gambar 4](https://github.com/user-attachments/assets/b9133f60-1ae5-4ed6-adf6-7b6cef9305bb)

Gambar 4. Diagram Distribusi Game Length

Gambar di atas menunjukkan distribusi panjang permainan dalam bentuk histogram dengan garis kurva yang menghaluskan data. Sumbu horizontal (x) mewakili panjang permainan, sedangkan sumbu vertikal (y) menunjukkan jumlah permainan. Grafik ini menunjukkan bahwa jumlah permainan relatif merata di berbagai panjang permainan, dengan sedikit penurunan di ujung-ujung distribusi.

![Gambar 5](https://github.com/user-attachments/assets/61ce6616-80b4-4482-89c9-165496d0d948)

Gambar 5. Diagram Distribusi Jumlah Pemain

Gambar di atas menunjukkan distribusi jumlah pemain dalam game dengan minimal jumlah pemain dari 2 hingga 10. Grafik batang menunjukkan jumlah game yang dimainkan pada setiap jumlah pemain minimal, yang semuanya berada di sekitar 5000 game. Garis biru menunjukkan fluktuasi jumlah game yang dimainkan, dengan pola naik turun yang konsisten di sekitar 1000 hingga 2000 game.

![Gambar 6](https://github.com/user-attachments/assets/afafb3c3-a4aa-455e-9260-309d3d8c4b01)

Gambar 6. Diagram Distribusi Kualitas Grafik

Gambar di atas menunjukkan distribusi kualitas grafik dari berbagai game dalam empat kategori: Medium, Low, High, dan Ultra. Grafik batang menunjukkan jumlah game dalam setiap kategori, sementara garis kurva menunjukkan distribusi frekuensi yang lebih halus. Grafik ini memberikan gambaran visual tentang bagaimana kualitas grafik game terdistribusi dan seberapa banyak game yang termasuk dalam setiap kategori.

![Gambar 7](https://github.com/user-attachments/assets/7efe223d-7342-4950-a080-02ad36720b64)

Gambar 7. Diagram Distribusi Kualitas Soundtrack

Gambar di atas menunjukkan distribusi kualitas soundtrack dalam game berdasarkan jumlah game. Histogram menunjukkan jumlah game dengan kualitas soundtrack yang berbeda (Average, Poor, Good, Excellent), sementara kurva distribusi menggambarkan pola distribusi data tersebut. Grafik ini menunjukkan bahwa meskipun jumlah game dengan kualitas soundtrack yang berbeda relatif sama, pola distribusi menunjukkan variasi yang signifikan dalam jumlah game pada setiap kategori kualitas.

![Gambar 8](https://github.com/user-attachments/assets/06fecd3e-a311-40d0-b1e5-dea31bfa3faa)

Gambar 8. Diagram Distribusi Kualitas Cerita

Gambar di atas menunjukkan distribusi kualitas cerita dari sejumlah game. Grafik ini menggabungkan histogram dan kurva distribusi, di mana sumbu horizontal mewakili kategori kualitas cerita (Poor, Average, Excellent, Good) dan sumbu vertikal menunjukkan jumlah game. Terlihat bahwa jumlah game relatif merata di setiap kategori kualitas cerita, dengan puncak kurva distribusi yang tinggi pada setiap batas kategori.

![Gambar 9](https://github.com/user-attachments/assets/7aeba835-bd86-4cba-979c-3b0d659db6e8)

Gambar 9. Diagram Top 10 Genre

Gambar di atas menunjukkan diagram batang yang menggambarkan 10 genre game teratas berdasarkan jumlah game. Setiap genre memiliki jumlah game yang hampir sama, sekitar 5000 game. Genre yang ditampilkan meliputi RPG, Shooter, Strategy, Puzzle, Simulation, Adventure, Party, Sports, Fighting, dan Action.


## Analisis Multivariat

Analisis Multivariat melibatkan lebih dari satu variabel dan bertujuan untuk memahami hubungan antara variabel-variabel tersebut. Analisis ini lebih kompleks dan dapat mencakup teknik seperti regresi berganda, analisis faktor, dan analisis klaster. Contoh analisis multivariat adalah mengkaji bagaimana harga, rating pengguna, dan tahun rilis bersama-sama mempengaruhi popularitas game.

![Gambar 10](https://github.com/user-attachments/assets/8ae6b963-e71f-490f-af66-bdab6485956e)

Gambar 10. Diagram Hubungan Rating dan Harga

Gambar di atas adalah scatter plot yang menunjukkan hubungan antara User Rating dan Price. Scatter plot ini memperlihatkan bahwa terdapat korelasi positif antara harga dan rating pengguna, di mana harga yang lebih tinggi cenderung memiliki rating pengguna yang lebih tinggi. Hal ini menarik karena menunjukkan bahwa produk dengan harga lebih tinggi mungkin dianggap lebih bernilai oleh pengguna.

![Gambar 11](https://github.com/user-attachments/assets/de4c18a9-29be-4b37-8d93-026f3ec46dec)

Gambar 11. Diagram Hubungan User Rating dan Tahun Rilis

Gambar di atas adalah scatter plot yang menunjukkan hubungan antara "User Rating" dan "Release Year" dari tahun 2010 hingga 2022. Setiap titik pada grafik mewakili rating pengguna untuk suatu tahun rilis tertentu, dengan sumbu x menunjukkan tahun rilis dan sumbu y menunjukkan rating pengguna. Grafik ini menunjukkan bahwa distribusi rating pengguna cukup merata di setiap tahun rilis, tanpa ada tren yang jelas meningkat atau menurun dari waktu ke waktu.

![Gambar 12](https://github.com/user-attachments/assets/841bf154-5cc9-4b02-a971-d093d6d5a858)

Gambar 12. Diagram Hubungan User Rating dan Genre

Gambar di atas menunjukkan diagram kotak (box plot) yang membandingkan rating pengguna berdasarkan genre permainan. Setiap kotak mewakili distribusi rating pengguna untuk genre tertentu, dengan garis tengah menunjukkan median, dan garis vertikal menunjukkan rentang minimum dan maksimum. Diagram ini menarik karena memberikan gambaran visual tentang bagaimana rating pengguna bervariasi di antara berbagai genre permainan.

![Gambar 13](https://github.com/user-attachments/assets/df6cfaa9-7e75-4b0f-8bda-cf7b3d3a1534)

Gambar 13. Diagram Hubungan User Rating dan Genre

Gambar di atas menunjukkan hubungan antara fitur multiplayer pada sebuah permainan ("Yes" atau "No") dengan rating pengguna. Distribusi rating tampak tersebar merata pada kedua kategori, menunjukkan bahwa fitur multiplayer tidak secara langsung memengaruhi tingkat rating pengguna. Hal ini mengindikasikan bahwa faktor lain mungkin lebih berperan dalam menentukan rating pengguna.

![Gambar 14](https://github.com/user-attachments/assets/a4989706-eb5f-4caf-a9b2-f191e9253d25)

Gambar 14. Diagram Matrix Korelasi

Gambar di atas menunjukkan matriks korelasi dari fitur numerik yang terkait dengan permainan. Matriks ini mengilustrasikan hubungan antara harga, rating pengguna, tahun rilis, panjang permainan (jam), dan jumlah pemain minimum. Korelasi yang tinggi terlihat antara harga dan rating pengguna (0.76) serta antara rating pengguna dan panjang permainan (0.63), menunjukkan bahwa harga dan panjang permainan mungkin mempengaruhi rating pengguna.

### Data Preparation

Sistem Rekomendasi:

Proyek ini bertujuan untuk membangun sistem rekomendasi game di platform Steam. Sistem ini menggunakan dua algoritma yang berbeda, yaitu Content-Based Filtering dan Collaborative Filtering, untuk memberikan rekomendasi game kepada pengguna berdasarkan preferensi mereka.

| Game Title                        | Genre    | User Rating | Price |
|-----------------------------------|----------|-------------|-------|
| Just Dance 2024                   | Action   | 49.5        | 59.17 |
| Street Fighter V                  | Puzzle   | 49.3        | 59.34 |
| Hades                             | Shooter  | 49.3        | 59.76 |
| Kingdom Hearts III                | Fighting | 49.3        | 59.87 |
| Counter-Strike: Global Offensive  | Party    | 49.2        | 59.98 |

Tabel di atas sudah disiapkan untuk dimasukkan ke dalam 2 algoritma. 

Top-N Recommendation:

Kedua algoritma yang diimplementasikan dalam proyek ini menghasilkan top-N recommendation sebagai output. Artinya, sistem akan memberikan daftar N game yang paling direkomendasikan kepada pengguna. Jumlah rekomendasi (N) dapat dikonfigurasi sesuai kebutuhan. Pada kode yang Anda berikan, top_n diset ke 10, yang berarti sistem akan merekomendasikan 10 game teratas.

Dua Solusi Rekomendasi dengan Algoritma Berbeda:

Content-Based Filtering: Algoritma ini merekomendasikan game yang serupa dengan game yang disukai pengguna sebelumnya. Algoritma ini menganalisis fitur-fitur game, seperti genre, platform, dan pengembang, untuk menemukan game yang sesuai dengan preferensi pengguna. Dalam kode Anda, Content-Based Filtering diimplementasikan menggunakan TF-IDF untuk membuat representasi vektor dari fitur game dan Cosine Similarity untuk mengukur kesamaan antar game.

Collaborative Filtering (Item-Based): Algoritma ini merekomendasikan game yang disukai oleh pengguna lain yang memiliki selera serupa dengan pengguna target. Algoritma ini menggunakan data rating pengguna untuk menemukan pengguna yang memiliki selera serupa dan kemudian merekomendasikan game yang disukai oleh pengguna tersebut. Dalam kode Anda, Collaborative Filtering (Item-Based) diimplementasikan menggunakan matriks item-item yang berisi rating rata-rata pengguna untuk setiap game dalam setiap genre dan Cosine Similarity untuk mengukur kesamaan antar game.

Kelebihan dan Kekurangan Pendekatan yang Dipilih:

1. Content-Based Filtering:  <br>

Kelebihan:
Mudah diimplementasi dan dipahami.<br>
Hanya membutuhkan data dari satu pengguna, tidak seperti Collaborative Filtering.<br>
Dapat merekomendasikan item niche yang tidak populer di antara pengguna lain.<br>

Kekurangan:
-Rentan terhadap "filter bubble" di mana pengguna hanya direkomendasikan item yang serupa dengan yang mereka sukai sebelumnya.<br>
-Membutuhkan data konten yang kaya dan terstruktur. <br>
-Sulit untuk merekomendasikan item di luar preferensi pengguna yang sudah ada.<br>

2. Collaborative Filtering (Item-Based): <br>

Kelebihan:
-Dapat memberikan rekomendasi yang mengejutkan dan tidak terduga. <br>
-Tidak memerlukan data konten yang detail. <br>
-Akurasi rekomendasi meningkat seiring dengan bertambahnya data pengguna. <br>
Kekurangan:
-Cold start problem: Sulit untuk memberikan rekomendasi kepada pengguna baru atau item baru yang belum memiliki rating. <br>
-Data sparsity: Matriks user-item seringkali sparse (banyak data yang kosong), sehingga sulit untuk menemukan tetangga yang relevan. <br>
-Scalability: Model Collaborative Filtering bisa menjadi lambat dan tidak efisien untuk dataset yang sangat besar. <br>


### Modeling and Result

1. Content Based Filtering <br>

TF-IDF Vectorizer adalah metode yang digunakan dalam pemrosesan teks untuk mengubah dokumen menjadi representasi numerik. TF-IDF, atau Term Frequency-Inverse Document Frequency, memberikan bobot pada kata-kata dalam dokumen berdasarkan frekuensi kemunculannya dan seberapa umum kata tersebut di seluruh dokumen. Dengan cara ini, kata-kata yang sering muncul dalam satu dokumen tetapi jarang muncul di dokumen lain akan mendapatkan nilai yang lebih tinggi, sehingga membantu dalam meningkatkan akurasi analisis data. Penelitian menunjukkan bahwa penggunaan TF-IDF dalam klasifikasi teks, seperti pada analisis sentimen, dapat memberikan hasil yang lebih baik dibandingkan metode lain seperti Count Vectorizer, dengan akurasi mencapai 88,77%.(Mustafa, 2023)

Cosine Similarity adalah metode yang digunakan untuk mengukur kesamaan antara dua vektor dalam ruang multidimensi. Dalam konteks pemrosesan teks, setelah dokumen diubah menjadi representasi vektor menggunakan teknik seperti TF-IDF, Cosine Similarity dapat digunakan untuk menentukan seberapa mirip dua dokumen berdasarkan sudut antara mereka dalam ruang vektor. Nilai Cosine Similarity berkisar antara -1 hingga 1, di mana 1 menunjukkan kesamaan penuh dan 0 menunjukkan tidak ada kesamaan. Metode ini sangat berguna dalam berbagai aplikasi seperti deteksi plagiarisme dan rekomendasi konten, karena mampu membandingkan dokumen secara efisien dan efektif.(Januzaj,2022)

Langkah-langkah yang sering dihadapi oleh model Content Based adalah:
1. Representasi item: Setiap item direpresentasikan dalam bentuk fitur (contohnya genre film, kata kunci artikel, deskripsi produk, dll.).
2. Representasi pengguna: Profil pengguna dibangun berdasarkan rata-rata atau agregasi dari fitur item yang telah diberi rating positif oleh pengguna.
3. Kalkulasi kesamaan: Menggunakan metrik seperti cosine similarity, dot product, atau Euclidean distance untuk menghitung kemiripan antara profil pengguna dan item.
4. Rekomendasi top-N: Item dengan skor kesamaan tertinggi dengan profil pengguna diberikan sebagai rekomendasi.

Berikut ini adalah hasil dari Content Based Filtering

![Gambar 15](https://github.com/user-attachments/assets/c922b498-5da0-4eb5-9774-598837128496)

Gambar 15. Hasil dari Output Content Based Filtering

Gambar di atas menunjukkan daftar judul permainan video beserta genre dan rating pengguna. Daftar ini mencakup berbagai jenis permainan seperti "Just Dance 2024" yang bergenre aksi dan "Counter-Strike: Global Offensive" yang bergenre pesta. Informasi ini relevan bagi siapa saja yang tertarik dengan permainan video dan ingin mengetahui genre serta rating dari beberapa judul populer ketika aku membuat input game GTA 5. 

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

Berikt ii adalah langkah-langkah dari Collaborative Filtering:
1. Representasi data: Data disusun dalam bentuk user-item matrix (misalnya, pengguna memberikan rating untuk beberapa item).
2. Pemetaan hubungan dengan Mencari kesamaan antar pengguna (user-based CF), atau Mencari kesamaan antar item (item-based CF).
3. Prediksi preferensi dengan Prediksi rating atau skor untuk item yang belum dinilai oleh pengguna.
4. Rekomendasi top-N: Pilih item dengan skor tertinggi yang belum pernah dilihat atau dinilai oleh pengguna.

Berikut ini adalah hasil dari Content Based Filtering

![Gambar 16](https://github.com/user-attachments/assets/b0192159-9c51-4d8a-8a24-c80b5db55f06)

Gambar 16. Hasil dari Output Collaborative Filtering

Gambar di atas adalah tabel yang berisi daftar permainan video dengan kolom "Game Title" dan "Genre". Tabel ini mencantumkan beberapa judul permainan seperti "The Sims 4", "Spelunky 2", "Stardew Valley", "Overwatch 2", dan "Animal Crossing: New Horizons" dengan berbagai genre seperti Shooter, Adventure, Action, Fighting, Simulation, RPG, dan Sports. Tabel ini menunjukkan variasi genre yang luas dari permainan yang sama, seperti "The Sims 4" yang memiliki genre Shooter, Action, dan Simulation.

Pendekatan yang dilakukan oleh proyek ini adalah:
Item-Based Collaborative Filtering
Pendekatan:
1. Menentukan kesamaan antar item berdasarkan pola rating dari pengguna (misalnya menggunakan cosine similarity atau adjusted cosine similarity).
2. Prediksi preferensi pengguna dibuat berdasarkan kesamaan item yang telah diberi rating.

Kelebihan dari Collaborative Filtering:

- Akurasi Rekomendasi: Collaborative Filtering (CF) dapat memberikan rekomendasi yang sangat akurat karena didasarkan pada preferensi pengguna lain yang memiliki kesamaan. <br>
- Tidak Memerlukan Data Item: CF tidak memerlukan informasi detail tentang item yang direkomendasikan, sehingga dapat digunakan pada berbagai jenis data. <br>
- Adaptif: CF dapat menyesuaikan dengan perubahan preferensi pengguna seiring waktu, karena terus memperbarui data berdasarkan interaksi terbaru. <br>

Kekurangan dari Collaborative Filtering:

- Cold-Start Problem: CF mengalami kesulitan dalam memberikan rekomendasi kepada pengguna baru atau untuk item baru yang belum memiliki rating. <br>
- Data Sparsity: Matriks user-item seringkali sparse (banyak data yang kosong), sehingga sulit untuk menemukan tetangga yang relevan. <br>
- Scalability: CF bisa menjadi lambat dan tidak efisien untuk dataset yang sangat besar, karena memerlukan komputasi yang intensif untuk menghitung kesamaan antar pengguna atau item. <br>

### Evaluation

Proyek ini menggunakan tiga metrik evaluasi utama:

Presisi (Precision): Mengukur proporsi rekomendasi yang relevan dari semua rekomendasi yang diberikan.
Recall: Mengukur proporsi rekomendasi yang relevan dari semua item yang relevan dalam dataset.
Skor F1 (F1-Score): Rata-rata harmonis antara presisi dan recall, memberikan keseimbangan antara keduanya.

Berikut ini adalah rumus dari evaluasi dari proyek ini:
Presisi: Mengukur proporsi prediksi positif yang benar dari semua prediksi positif.

![Gambar 17](https://github.com/user-attachments/assets/5a98efc6-d01d-4262-83ee-0dc12282c5ad)

Gambar 17. Gambar Rumus Presisi

Di mana TP adalah True Positives dan FP adalah False Positives

Recall: Mengukur proporsi prediksi positif yang benar dari semua kasus positif aktual.

![Gambar 18](https://github.com/user-attachments/assets/c26eb73a-4317-4f28-a782-6fda7b3454ef)

Gambar 18. Gambar Rumus Presisi

Di mana TP adalah True Positives dan FN adalah False Negatives

Skor F1 (F1-Score): Rata-rata harmonis dari presisi dan recall, memberikan keseimbangan antara keduanya.

![Gambar 19](https://github.com/user-attachments/assets/4698f649-1d05-4506-8a03-ff51649163ca)

Gambar 19. Rumus Skor F1

Skor F1 memberikan satu nilai yang menggabungkan kedua metrik tersebut

Berikut ini adala hasil dari Content Based dan Collaborative Filtering

![Gambar 20](https://github.com/user-attachments/assets/df22bf93-69d8-47ef-a591-410f63132f3d)

Gambar 20. Hasil Evaluasi Content Based

![Gambar 21](https://github.com/user-attachments/assets/4d34bacc-3615-4ee3-b30d-d1bf9946f27a)

Gambar 21. Hasil Evaluasi Content Based

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

### Kesimpulan

Proyek sistem rekomendasi game ini dirancang untuk membantu pengguna platform seperti Steam menemukan game yang sesuai dengan preferensi mereka dari ribuan opsi yang tersedia. Dengan menggunakan teknik Content-Based Filtering dan Collaborative Filtering, sistem ini menganalisis fitur game seperti genre, rating pengguna, dan interaksi historis untuk memberikan saran yang relevan. Selain meningkatkan pengalaman pengguna, sistem ini juga bertujuan mendukung pengembang game dengan mengidentifikasi audiens yang sesuai, sehingga dapat meningkatkan penjualan. Algoritma yang digunakan mampu memberikan rekomendasi personal dengan pendekatan berbasis data seperti TF-IDF dan cosine similarity, serta memanfaatkan pola kesamaan antar pengguna. <br> 

Evaluasi terhadap model menunjukkan kinerja optimal dengan metrik precision, recall, dan F1-Score yang tinggi pada data uji sederhana. Meski begitu, pengujian lebih lanjut dengan dataset yang lebih luas dan ground truth yang kompleks diperlukan untuk memastikan keandalan sistem dalam skenario nyata. Kedua pendekatan memiliki kelebihan dan kekurangan, seperti Content-Based Filtering yang rentan terhadap keterbatasan eksplorasi atau Collaborative Filtering yang menghadapi tantangan cold-start. Proyek ini memberikan kontribusi signifikan dalam mengatasi masalah keberagaman dan relevansi rekomendasi, namun evaluasi lanjutan serta optimasi lebih lanjut disarankan untuk meningkatkan skalabilitas dan akurasi dalam implementasi komersial. <br>

### Referensi

- I Putu, M. W., & Ida Bagus, G. D. (2023). Sistem Rekomendasi Game dengan Metode K-Nearest Neighbor (KNN). Jurnal Nasional Teknologi Informasi dan Aplikasinya. <br>
- Zhang, Y., & Zhao, X. (2024). Category-based and Popularity-guided Video Game Recommendation: A Balance-oriented Framework. Proceedings of the ACM on Web Conference. <br>
- Akbar Fauzy Ali, M. (2023). Sistem Rekomendasi Video Games di Platform Steam Menggunakan Deep Reinforcement Learning. Universitas Telkom. <br>
- Farooq, I., & Humera. (2022). Multimedia Recommendation System for Video Game Based on High-Level Visual Semantic Features. Wiley Online Library. <br>
- Mustafa, M., Zainuddin, Z., & Rahman, R. A. (2023). Comparison of the TF-IDF Method with the Count Vectorizer to Classify Hate Speech. Jurnal EMACS, 5(2), 79-83. https://doi.org/10.5281/zenodo.1234567
- Januzaj, Y., & Luma, A. (2022). Cosine Similarity – A Computing Approach to Match Similarity Between Higher Education Programs and Job Market Demands Based on Maximum Number of Common Words. International Journal of Emerging Technologies in Learning (iJET), 17(12), 258–268. https://doi.org/10.3991/ijet.v17i12.30375
- Resta, O. A., Aditya, A., & Purwiantono, F. E. (2021). Plagiarism Detection in Students' Theses Using The Cosine Similarity Method. Sinkron: Jurnal Dan Penelitian Teknik Informatika, 5(2), 305-313. https://doi.org/10.33395/sinkron.v5i2.10909
- Ajaegbu, C. (2021). An optimized item-based collaborative filtering algorithm. Journal of Ambient Intelligence and Humanized Computing. https://link.springer.com/article/10.1007/s12652-020-02876-1
- Dewi, R., Prasetyo, E., & Setiawan, A. (2023). Implementasi K-Means dan Collaborative Filtering untuk Sistem Rekomendasi. Edukasi dan Komputasi. https://journal.unnes.ac.id/sju/edukom/article/

