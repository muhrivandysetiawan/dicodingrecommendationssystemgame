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



## Analisis Multivariat


 
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

