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

Berikut ini merupakan informasi data untuk menunjnag proyek pada tabel di bawah ini:

### 1. Dataset Informasi Game
| Kolom           | Jumlah Non-Null | Tipe Data | Deskripsi |
|-----------------|-----------------|-----------|-----------|
| app_id          | 50872           | int64     | ID unik dari game |
| title           | 50872           | object    | Judul game |
| date_release    | 50872           | object    | Tanggal rilis game |
| win             | 50872           | bool      | Tersedia di platform Windows |
| mac             | 50872           | bool      | Tersedia di platform MacOS |
| linux           | 50872           | bool      | Tersedia di platform Linux |
| rating          | 50872           | object    | Rating dari game |
| positive_ratio  | 50872           | int64     | Rasio ulasan positif |
| user_reviews    | 50872           | int64     | Jumlah ulasan pengguna |
| price_final     | 50872           | float64   | Harga akhir setelah diskon |
| price_original  | 50872           | float64   | Harga asli dari game |
| discount        | 50872           | float64   | Diskon yang diberikan |
| steam_deck      | 50872           | bool      | Tersedia di platform Steam Deck |

### 2. Dataset Ulasan Pengguna
| Kolom           | Jumlah Non-Null | Tipe Data | Deskripsi |
|-----------------|-----------------|-----------|-----------|
| app_id          | 41154794        | int64     | ID unik dari game |
| helpful         | 41154794        | int64     | Jumlah pengguna yang merasa ulasan ini bermanfaat |
| funny           | 41154794        | int64     | Jumlah pengguna yang merasa ulasan ini lucu |
| date            | 41154794        | object    | Tanggal ulasan dibuat |
| is_recommended  | 41154794        | bool      | Apakah ulasan ini merekomendasikan game tersebut |
| hours           | 41154794        | float64   | Jumlah jam yang dimainkan oleh pengguna |
| user_id         | 41154794        | int64     | ID unik dari pengguna |
| review_id       | 41154794        | int64     | ID unik dari ulasan |

### 3. Dataset Informasi Pengguna
| Kolom    | Jumlah Non-Null | Tipe Data | Deskripsi |
|----------|------------------|-----------|-----------|
| user_id  | 14306064        | int64     | ID unik dari pengguna |
| products | 14306064        | int64     | Jumlah produk yang dimiliki oleh pengguna |
| reviews  | 14306064        | int64     | Jumlah ulasan yang telah dibuat oleh pengguna |

Proyek ini diseleksi menjadi 5000 data dari semua jumlah data yang tersedia karena data di atas cukup banyak dan bisa menyebbakan crash ketika melakukan komputasi. Sleain itu, seleksi ini ditujukan agar komputasi bisa berjalan lancar dibandingkan harus menggunakan semua data.

Ini adalah sebuah tautan untuk merancang proyek adalah sebagai berikut: <br>
https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam

Berikut ini adalah penjelasan tabel yang diambil secara mendalam adalah tabel sebagai berikut:

1. Tabel games <br>
Tabel ini berisi informasi tentang game-game yang ada di Steam. Variabel-variabelnya adalah: <br>
app_id: ID unik untuk setiap game di Steam (tipe data: int64). <br>
title: Judul game (tipe data: object). <br>
date_release: Tanggal rilis game (tipe data: object, dapat diubah ke datetime64[ns]). <br>
win: Apakah game tersedia di Windows (True/False) (tipe data: bool). <br>
mac: Apakah game tersedia di macOS (True/False) (tipe data: bool). <br>
linux: Apakah game tersedia di Linux (True/False) (tipe data: bool). <br>
rating: Rating game (0-100) (tipe data: int64). <br>
positive_ratio: Rasio ulasan positif (0-100) (tipe data: int64). <br>
user_reviews: Jumlah total ulasan pengguna (tipe data: int64). <br>
price_final: Harga akhir game setelah perubahan (tipe data: float64). <br>
price_original: Harga asli game sebelum perubahan (tipe data: float64). <br>
discount: Persentase diskon (tipe data: float64). <br>
steam_deck: Apakah game kompatibel dengan Steam Deck (True/False) (tipe data: bool). <br>

2. Tabel recommendations <br>
Tabel ini berisi rekomendasi game dari pengguna. Variabel-variabelnya adalah: <br>
app_id: ID unik untuk setiap game di Steam (tipe data: int64). <br>
helpful: Jumlah pengguna yang menganggap ulasan ini membantu (tipe data: int64). <br>
funny: Jumlah pengguna yang menganggap ulasan ini lucu (tipe data: int64).<br>
date: Tanggal ulasan dibuat (tipe data: object, dapat diubah ke datetime). <br>
is_recommended: Apakah pengguna merekomendasikan game ini (True/False) (tipe data: bool). <br>
hours: Jumlah jam pengguna telah memainkan game ini (tipe data: float64). <br>
user_id: ID unik untuk setiap pengguna yang menulis ulasan (tipe data: int64). <br>
review_id: ID unik untuk setiap ulasan (tipe data: int64). <br>

3. Tabel user <br>
Tabel ini berisi informasi tentang pengguna. Variabel-variabelnya adalah: <br>
user_id: Pengenal unik untuk setiap pengguna. <br>
products: Jumlah produk yang terkait dengan pengguna. <br>
reviews: Jumlah ulasan yang ditulis oleh pengguna. <br>

Berikut ini adalah analisis univariat dan multivariat untuk proyeksistem rekomendasi adalah sebagai berikut:

## Analisis Univariat


![download](https://github.com/user-attachments/assets/7806b72b-aab8-4853-a43c-49af3bf81487)


Analisis harga akhir setelah diskon dapat menunjukkan rentang harga game yang paling umum di Steam. Distribusi harga dapat memperlihatkan seberapa banyak game yang tergolong mahal, menengah, atau murah. Rata-rata dan median harga juga dapat dihitung untuk melihat apakah distribusinya terpusat atau miring.


![download (1)](https://github.com/user-attachments/assets/db794ab1-336d-4d1c-81db-903118e137af)


Menampilkan distribusi rasio ulasan positif membantu melihat bagaimana sebagian besar game diterima oleh pengguna. Apakah lebih banyak game yang memiliki rasio ulasan positif tinggi atau rendah? Ini dapat menjadi indikator kualitas umum dari game yang tersedia.


![download (2)](https://github.com/user-attachments/assets/17782af1-3a54-4e5a-9ed3-45b044d4e813)



Dengan menghitung frekuensi distribusi untuk setiap platform (Windows, MacOS, Linux, Steam Deck), kita bisa memahami game mana yang paling banyak tersedia dan berapa banyak game yang eksklusif untuk platform tertentu.


![download (3)](https://github.com/user-attachments/assets/618856ee-eee2-401e-bf06-85f25ba8e485)


Memvisualisasikan distribusi rating membantu memahami kualitas umum dari game-game yang ada di Steam. Rating dapat diubah menjadi skor numerik jika memiliki banyak kategori untuk mempermudah analisis lebih lanjut.


![download (4)](https://github.com/user-attachments/assets/8a0146d4-eb09-4377-847c-6434de16129d)


Melakukan analisis distribusi jumlah jam bermain menunjukkan seberapa sering dan lama rata-rata pengguna memainkan game. Distribusi ini juga dapat mengidentifikasi pengguna aktif dan casual.


![download (5)](https://github.com/user-attachments/assets/5e552a56-6364-47b5-a880-7011c06194d9)


Analisis ini merupakan analisis dimana 10 game terbaik dalam Steam. 


## Analisis Multivariat


![download (6)](https://github.com/user-attachments/assets/7b6ff39f-3e0f-4a36-b308-b1bfb37f2888)


Korelasi antara variabel discount dan price_final dengan jumlah ulasan (user_reviews) dapat membantu menganalisis apakah diskon mempengaruhi popularitas atau pembelian game. Penurunan harga (diskon) biasanya berkaitan dengan kenaikan pembelian, dan analisis ini bisa menunjukkan korelasinya.


![download (7)](https://github.com/user-attachments/assets/043e9cce-86c4-42cb-8a0d-c8e07c869338)


Memeriksa korelasi antara rasio ulasan positif dan jumlah jam bermain menunjukkan apakah game dengan ulasan positif cenderung memiliki pengguna yang menghabiskan lebih banyak waktu di dalam game. Game yang bagus umumnya memiliki review positif dan waktu bermain yang tinggi.


![download (8)](https://github.com/user-attachments/assets/3c80915e-b4f0-4f22-ad70-3a291c393f75)


Meneliti korelasi antara harga game dan rasio ulasan positif membantu melihat apakah harga game memengaruhi persepsi kualitas game. Game yang lebih murah mungkin lebih terjangkau tetapi belum tentu memiliki rasio ulasan positif yang tinggi.


![download (9)](https://github.com/user-attachments/assets/60faf6ce-f9e3-4582-8fa2-72b0687b9fb3)
![download (10)](https://github.com/user-attachments/assets/5f3f2884-66b4-4002-b409-e58138804176)


Melakukan analisis jumlah rekomendasi ulasan dari pengguna berdasarkan platform dapat menunjukkan platform mana yang lebih disukai atau populer di kalangan pemain.



### Data Preparation


- Menerapkan dan menyebutkan teknik data preparation yang dilakukan. <br>
- Teknik yang digunakan pada notebook dan laporan harus berurutan. <br>
- Menjelaskan proses data preparation yang dilakukan. <br>
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut. <br>


### Modeling and Result


- Membuat dan menjelaskan sistem rekomendasi untuk menyelesaikan permasalahan <br>
- Menyajikan top-N recommendation sebagai output. <br>
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda. <br>
- Menjelaskan kelebihan dan kekurangan pada pendekatan yang dipilih. <br>


### Evaluation


- Menyebutkan metrik evaluasi yang digunakan.
- Menjelaskan hasil proyek berdasarkan metrik evaluasi.
- Metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.
- Menjelaskan metrik evaluasi yang digunakan untuk mengukur kinerja model (formula dan cara metrik tersebut bekerja).



### Kesimpulan





### Referensi

- I Putu, M. W., & Ida Bagus, G. D. (2023). Sistem Rekomendasi Game dengan Metode K-Nearest Neighbor (KNN). Jurnal Nasional Teknologi Informasi dan Aplikasinya. <br>
- Zhang, Y., & Zhao, X. (2024). Category-based and Popularity-guided Video Game Recommendation: A Balance-oriented Framework. Proceedings of the ACM on Web Conference. <br>
- Akbar Fauzy Ali, M. (2023). Sistem Rekomendasi Video Games di Platform Steam Menggunakan Deep Reinforcement Learning. Universitas Telkom. <br>
- Farooq, I., & Humera. (2022). Multimedia Recommendation System for Video Game Based on High-Level Visual Semantic Features. Wiley Online Library. <br>

