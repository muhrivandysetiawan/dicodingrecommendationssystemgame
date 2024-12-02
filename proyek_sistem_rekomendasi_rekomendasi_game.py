# -*- coding: utf-8 -*-
"""Proyek Sistem Rekomendasi - Rekomendasi Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ruJWN8paELJ07Jvq3kVGqcnQ93GvlS1D

# Proyek Sistem Rekomendasi Game

Proyek yang digunakan kali ini adalah Sistem Rekomendasi pada Game Steam. Proyek ini bertujuan untuk memberikan rekomendasi game kepada suatu pengguna.

Dataset yang diambil adalah: https://www.kaggle.com/datasets/jahnavipaliwal/video-game-reviews-and-ratings

# Masukin Dataset
"""

# Remove the existing folder if it exists
!rm -rf video-game-reviews-and-ratings
# Download the dataset using the Kaggle API
!kaggle datasets download -d jahnavipaliwal/video-game-reviews-and-ratings
# Extract the downloaded zip file
!unzip video-game-reviews-and-ratings.zip -d video-game-reviews-and-ratings

"""# Analisis Game

File yang diperoleh dari dataset ini adalah video games review.csv dengan jumlah data game adalah 47774
"""

# Impor Library yang dibutuhkan untuk disajikan dalam tabel
import pandas as pd
# Buatlah definisi dari masing-masing csv
games = pd.read_csv('/content/video-game-reviews-and-ratings/video_game_reviews.csv')
# Tunjukkan hasil jumlah data game, data rekomendasi, dan data user
print('Jumlah data games: ', len(games))

# Sekarang tunjukkan tabel pada file game
games

# Berikan info kolom dan jumlah data pada game
games.info()

"""Berikut ini adalah penjelasan informasi dari data video game ini:

1. Game Title: Nama game.

2. User Rating: Rating yang diberikan oleh pengguna, dalam format float.

3. Age Group Targeted: Kelompok usia yang menjadi target game.

4. Price: Harga game, dalam format float.

5. Platform: Platform tempat game tersedia (misalnya, PC, PlayStation, Xbox).

6. Requires Special Device: Apakah game memerlukan perangkat khusus (misalnya, VR headset).

7. Developer: Pengembang game.

8. Publisher: Penerbit game.

9. Release Year: Tahun rilis game.

10. Genre: Genre atau kategori game (misalnya, Action, Adventure, RPG).

11. Multiplayer: Apakah game mendukung mode multiplayer.

12. Game Length (Hours): Durasi permainan dalam jam.

13. Graphics Quality: Kualitas grafis game.

14. Soundtrack Quality: Kualitas soundtrack game.

15. Story Quality: Kualitas cerita game.

16. User Review Text: Teks ulasan dari pengguna.

17. Game Mode: Mode permainan (misalnya, Single Player, Multiplayer).

18. Min Number of Players: Jumlah minimum pemain yang diperlukan untuk memainkan game.
"""

# Cek apakah datanya duplikat atau tidak
games.duplicated().sum()

"""Sepertinya tidak ada data yang kosong dan aman untuk dianalisis."""

# Menunjukkan Jumlah game dan judul game
print('Jumlah Game: ', len(games['Game Title'].unique()))
print('Judul Game: ', games['Game Title'].unique())

# Menunjukkan Harga game dan rating user game
print('Jumlah User Rating: ', len(games['User Rating'].unique()))
print('User Rating: ', games['User Rating'].unique())

"""Data yang dtunjukkan adalah data user review dari angka 1 sampai 50 dimana angka 50 adalah angka tertinggi dalam user review."""

# Menunjukkan Harga game dan rating user game
print('Jumlah Harga Game: ', len(games['Price'].unique()))
print('Harga Game: ', games['Price'].unique())

"""Code di atas adalah isi dari harga game dalam Dollar."""

# Buatlah definisi untuk mencari game yang diinginkan.
def search_game(game_title):
    """
    Mencari game di DataFrame 'games' berdasarkan judulnya.

    Argumen:
        judul_game: Judul game yang akan dicari.

    Mengembalikan:
        DataFrame pandas yang berisi game yang cocok, atau None jika tidak ditemukan kecocokan.
    """
    matching_games = games[games['Game Title'].str.contains(game_title, case=False, na=False)]
    if not matching_games.empty:
        return matching_games
    else:
        return None


# Contoh Search Game
search_term = "Spelunky 2"  # Kamu bisa menggantikan pencarian game sesuai yang kamu mau.
results = search_game(search_term)

# Cek hasilnya jika ketemu atau tidak
if results is not None:
    print(f"Search Results for '{search_term}':")
    print(results)
else:
    print(f"No games found with the title '{search_term}'.")

"""Karena data ini sangat banyak dan bisa menyebabkan crash untuk dianalisis, maka data ini harus difilter sampai 5000 data.

# Analisis Univariat

Sekarang data ini akan dianalisis secara univariat terlebih dahulu
"""

# Deskripsi Game
games.describe()

# Impor library yang dibutuhkan untuk Analisis Uunivariat
import matplotlib.pyplot as plt
import seaborn as sns

# Distribusi Harga Game
plt.figure(figsize=(10, 6))
sns.histplot(games['Price'], kde=True)
plt.title('Distribusi Harga Game')
plt.xlabel('Harga')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat User Rating
plt.figure(figsize=(10, 6))
sns.histplot(games['User Rating'], kde=True)
plt.title('Distribusi User Rating')
plt.xlabel('User Rating')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat Tahun Rilis
plt.figure(figsize=(10, 6))
sns.histplot(games['Release Year'], kde=True)
plt.title('Distribusi Release Year')
plt.xlabel('Release Year')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat Durasi Game dalam Jam
plt.figure(figsize=(10, 6))
sns.histplot(games['Game Length (Hours)'], kde=True)
plt.title('Distribusi Game Length')
plt.xlabel('Game Length')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat Jumlah Pemain
plt.figure(figsize=(10, 6))
sns.histplot(games['Min Number of Players'], kde=True)
plt.title('Distribusi Jumlah Pemain')
plt.xlabel('Minimal Jumlah Pemain')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat Kualitas Grafik
plt.figure(figsize=(10, 6))
sns.histplot(games['Graphics Quality'], kde=True)
plt.title('Distribusi Kualitas Grafik')
plt.xlabel('Minimal Kualitas Grafik')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat Kualitas Soundtrack
plt.figure(figsize=(10, 6))
sns.histplot(games['Soundtrack Quality'], kde=True)
plt.title('Distribusi Kualitas Soundtrack')
plt.xlabel('Minimal Kualitas Soundtrack')
plt.ylabel('Jumlah Game')
plt.show()

# Analisis Univariat Kualitas Cerita
plt.figure(figsize=(10, 6))
sns.histplot(games['Story Quality'], kde=True)
plt.title('Distribusi Kualitas Cerita')
plt.xlabel('Minimal Kualitas Cerita')
plt.ylabel('Jumlah Game')
plt.show()

"""Sekarang kita tentukan Top 10 Genre dengan parameter game terbanyak dari user."""

# Perhitungan Top 10 Genre dalam Game
top_10_genres = games['Genre'].value_counts().head(10)

# Cetak Top 10 Genre
print("Top 10 Genres:")
print(top_10_genres)

# Create a bar plot for the top 10 genres
plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_genres.index, y=top_10_genres.values, hue=top_10_genres.index, dodge=False, palette="viridis", legend=False)
plt.title('Top 10 Genres', fontsize=16)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Number of Games', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()

"""# Analisis Multivariat

Setelah Analisis Univariat divisualisasikan, sekarang Analisis Multivariat yang terdiri dari dua data yang diukur secara bersamaan.
"""

# Hubungan antara User Rating dan Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='User Rating', data=games)
plt.title('User Rating vs. Price')
plt.xlabel('Price')
plt.ylabel('User Rating')
plt.show()

# Hubungan antara User Rating dan Release Year
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Release Year', y='User Rating', data=games)
plt.title('User Rating vs. Release Year')
plt.xlabel('Release Year')
plt.ylabel('User Rating')
plt.show()

# Hubungan Genre dengan User Rating
plt.figure(figsize=(12, 6))
sns.boxplot(x='Genre', y='User Rating', data=games)
plt.title('Genre vs. User Rating')
plt.xlabel('Genre')
plt.ylabel('User Rating')
plt.xticks(rotation=45, ha='right') # Rotasikan label x-axis biar bisa dibaca
plt.tight_layout()
plt.show()

# Analisis Multivariat: Multiplayer vs. User Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Multiplayer', y='User Rating', data=games)
plt.title('Multiplayer vs. User Rating')
plt.xlabel('Multiplayer')
plt.ylabel('User Rating')
plt.show()

# Correlation Matrix
correlation_matrix = games[['Price', 'User Rating', 'Release Year', 'Game Length (Hours)', 'Min Number of Players']].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

"""# Persiapan Data

Tujuan utama dari tahap persiapan data adalah untuk mengubah data mentah menjadi format yang sesuai dan optimal untuk diproses oleh model machine learning. Pada proyek ini, data yang ada perlu diolah agar dapat digunakan untuk membangun sistem rekomendasi Content-Based Filtering dan Collaborative Filtering.
"""

# Mengecek missing value pada dataframe games
games.isnull().sum()

# This example sorts games by 'User Rating' in descending order.
sorted_games = games.sort_values(by='User Rating', ascending=False)

sorted_games = sorted_games.reset_index(drop=True)  # Reset index
sorted_games

len(sorted_games)

# prompt: Buat persiapan data pakai minmaxscaler

from sklearn.preprocessing import MinMaxScaler

# Select numerical features for scaling (replace with your actual features)
numerical_features = ['Price', 'User Rating', 'Release Year', 'Game Length (Hours)', 'Min Number of Players']

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit and transform the numerical features
sorted_games[numerical_features] = scaler.fit_transform(sorted_games[numerical_features])

# Now the selected numerical features in the 'games' DataFrame are scaled between 0 and 1
print(sorted_games.head())

"""Semua data telah diperbaiki dan siap untuk dilatih 2 model karena hanya ada satu dokumen dalam file csv.

# Model Content Based Filtering

Content-Based Filtering adalah metode dalam sistem rekomendasi yang merekomendasikan item yang sebanding dengan yang disukai pengguna sebelumnya. Model ini menganalisis konten item (seperti genre game,judul game, platform,  pengembang game, dsb) untuk menemukan item yang sesuai dengan preferensi pengguna.

Berikut ini adalah cara kerja Model Content Based Filtering dalam Sistem Rekomendasi secara singkat:

1. Model ini menganalisis konten item, seperti genre, platform, dan developer, untuk membuat profil item.
2. Profil pengguna dibuat berdasarkan item yang disukai atau diberi rating tinggi.
3. Item dengan profil yang paling sesuai dengan profil pengguna direkomendasikan.
"""

# Impor Scikit-Learn untuk Model Content Based Filtering
!pip install scikit-learn

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Pilih kolom relevan untuk TF-IDF
selected_columns = ['Genre']

# Gabungkan kolom-kolom teks menjadi satu kolom
sorted_games['combined_features'] = sorted_games[selected_columns].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

# Inisialisasi TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english') # Stop words removal for better results

# Fit dan transform fitur kombinasi
tfidf_matrix = vectorizer.fit_transform(sorted_games['combined_features'])

# Sekarang cek ukuran TF-IDF Matrix
print(tfidf_matrix.shape)

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""Sebelum masuk ke Cosine Similarity, pastikan filter sampai 10000 data penting agar tidak terjadi crash ketika menjalankan Cosine Similarity"""

# Filter TF-IDF Matrix menjadi top 10,000 data yang penting
tfidf_sums = tfidf_matrix.sum(axis=1)
# Konversi tfidf_sums ke 1D array untuk hindari IndexError
top_indices = tfidf_sums.A1.argsort()[::-1][:10000]
# Sekarang, TF-IDF Matrix sudah dikonversi menjadi yang diinginkan
filtered_tfidf_matrix = tfidf_matrix[top_indices]
# Cek hasilnya
filtered_tfidf_matrix.shape

# Import Library untuk Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada Matrix tf-idf
cosine_sim = cosine_similarity(filtered_tfidf_matrix)
cosine_sim

# Ambil Kolom Relevantuntuk melakuakn sortir dan rekomendasi
selected_columns = ['Game Title', 'Genre', 'User Rating', 'Price'] # Add other desired columns

# Sortir User Rating di order descending dan reset index
sorted_games = games.sort_values(by=['User Rating'], ascending=False)
sorted_games = sorted_games.reset_index(drop=True)

# Ambil kolom yang diinginkan untuk sorted_games
sorted_games = sorted_games[selected_columns]

# Fungsi untuk mendapatkan rekomendasi
def game_recommendations(game_title, cosine_sim=cosine_sim, top_n=10):
    # Mendapatkan indeks game yang sesuai dengan judul
    game_index = sorted_games[sorted_games['Game Title'] == game_title].index[0]

    # Mendapatkan skor kesamaan untuk semua game terhadap game input
    similarity_scores = list(enumerate(cosine_sim[game_index]))

    # Mengurutkan game berdasarkan skor kesamaan
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Mendapatkan indeks dari top_n game yang paling mirip (tidak termasuk game input)
    top_indices = [i[0] for i in similarity_scores[1:top_n+1]]

    # Mengembalikan top_n game yang paling mirip dengan genre
    recommendations = sorted_games[['Game Title', 'Genre']].iloc[top_indices]
    return recommendations

# Contoh penggunaan
recommendations = game_recommendations('Grand Theft Auto V')
print(recommendations)

"""Kelebihan:

- Mudah diimplementasi dan dipahami.
- Hanya membutuhkan data dari satu pengguna, tidak seperti Collaborative Filtering.
- Dapat merekomendasikan item niche yang tidak populer di antara pengguna lain.

Kekurangan:

- Rentan terhadap "filter bubble" di mana pengguna hanya direkomendasikan item yang serupa dengan yang mereka sukai sebelumnya.
- Membutuhkan data konten yang kaya dan terstruktur.
- Sulit untuk merekomendasikan item di luar preferensi pengguna yang sudah ada.

# Model Collaborative Filtering

Collaborative Filtering adalah teknik sistem rekomendasi yang memprediksi preferensi pengguna terhadap suatu item berdasarkan rating atau interaksi pengguna lain yang memiliki selera serupa. Model ini mengasumsikan bahwa pengguna yang memiliki preferensi sama di masa lalu cenderung memiliki preferensi sama di masa depan.

Berikut ini adalah cara kerja Model Collaborative Filtering dalam Sistem Rekomendasi secara singkat:
1. Model ini mengumpulkan data rating atau interaksi pengguna terhadap item.
2. Model ini mengidentifikasi pengguna lain (tetangga) dengan preferensi serupa.
3. Model ini merekomendasikan item berdasarkan rating atau interaksi tetangga.

Ada dua pendekatan utama dalam Collaborative Filtering:

- User-Based: Merekomendasikan item yang disukai oleh pengguna lain yang serupa dengan pengguna target.
- Item-Based: Merekomendasikan item yang serupa dengan item yang disukai oleh pengguna target di masa lalu.

Untuk kasus proyek ini pakai Item Based untuk melakukan pemodelan
"""

# Install Library Surprise
!pip install surprise

# Buatlah Library buat Collaborative Filtering
import pandas as pd
from surprise import Dataset, Reader, SVD, KNNBasic
from surprise.model_selection import train_test_split, GridSearchCV
from surprise import accuracy

# Mengasumsikan DataFrame 'recommendations_filtered' berisi kolom 'user_id', 'app_id', dan 'rating'
# Buat objek Surprise Reader, tentukan skala rating
reader = Reader(rating_scale=(1, 50))  # Mengasumsikan rating berada di antara 1 dan 50

# Muat data ke dalam Surprise Dataset
data = Dataset.load_from_df(sorted_games[['Game Title','Genre', 'User Rating']], reader)

# Bagi data menjadi set pelatihan dan pengujian
trainset, testset = train_test_split(data, test_size=0.25)

# Definisikan parameter grid untuk GridSearchCV
param_grid = {'n_factors': [50, 100, 150], 'n_epochs': [20, 30], 'lr_all': [0.005, 0.01]}

# Gunakan GridSearchCV untuk mencari parameter terbaik (opsional)
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
gs.fit(data)

# Gunakan parameter terbaik dari GridSearchCV
algo = gs.best_estimator['rmse']

# Latih model dengan algoritma dan parameter terbaik
algo.fit(trainset)

# Lakukan prediksi pada data testing
predictions = algo.test(testset)

# Evaluasi model
accuracy.rmse(predictions)
accuracy.mae(predictions)

# Sekarang buat definisi rekomendasi modelling dalam bentuk tabel
def get_recommendations_for_game(game_title, model, top_n=10):
    """
    Mendapatkan rekomendasi game berdasarkan nama game.

    Args:
        game_title: Judul game yang ingin dicari rekomendasinya.
        model: Model Collaborative Filtering yang telah dilatih.
        top_n: Jumlah rekomendasi yang ingin ditampilkan.

    Returns:
        List of tuples: Daftar rekomendasi game dalam format (judul game, rating prediksi).
    """
    # Mendapatkan daftar semua game
    all_games = sorted_games['Game Title'].unique()

    # Cari game yang sesuai dengan judul yang diinputkan
    try:
        game_index = list(all_games).index(game_title)
        game_id = all_games[game_index]  # Mendapatkan ID game
    except ValueError:
        print(f"Game '{game_title}' tidak ditemukan dalam dataset.")
        return []

    # Mendapatkan prediksi rating untuk semua game lainnya
    predictions = [(game, model.predict(game_id, game).est) for game in all_games if game != game_id]

    # Urutkan prediksi berdasarkan rating
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Ambil top_n rekomendasi
    top_recommendations = predictions[:top_n]

    return top_recommendations

# Import Librar agar bisa embuat sistem rekomendasi dalam bentuk tabel
import pandas as pd

# Sekarang buat definisi rekomendasi modelling dalam bentuk tabel
def get_recommendations_for_game_table(game_title, model, top_n=10):
    """
    Mendapatkan rekomendasi game dalam bentuk tabel.

    Args:
        game_title: Judul game yang ingin dicari rekomendasinya.
        model: Model Collaborative Filtering yang telah dilatih.
        top_n: Jumlah rekomendasi yang ingin ditampilkan.

    Returns:
        pandas.DataFrame: Tabel rekomendasi game.
    """
    recommendations = get_recommendations_for_game(game_title, model, top_n)  # Gunakan fungsi sebelumnya

    if recommendations:
        # Buat DataFrame dari rekomendasi
        recommendations_df = pd.DataFrame(recommendations, columns=['Game', 'Predicted Rating'])

        # Tampilkan tabel
        display(recommendations_df)  # or print(recommendations_df.to_string()) if display doesn't work
    else:
        print(f"Tidak ada rekomendasi ditemukan untuk game '{game_title}'.")

# Contoh penggunaan Collaborative Filtering
game_title = 'Grand Theft Auto V'  # Ganti dengan nama game yang diinginkan
get_recommendations_for_game_table(game_title, algo)

"""Kelebihan:

1. Rekomendasi beragam & tak terduga.
2. Mudah diimplementasi, data konten tidak diperlukan.
3. Akurasi meningkat seiring data bertambah.

Kekurangan:

1. Sulit rekomendasikan game/user baru (Cold Start).
2. Data rating yang sedikit/kosong mengurangi akurasi.
3. Lambat untuk dataset besar.

# Evaluasi
"""

from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np
from collections import defaultdict

# Fungsi untuk mengevaluasi model rekomendasi
def evaluate_model(model_name, recommendations, ground_truth):
    precision = []
    recall = []
    f1 = []

    # Iterasi melalui setiap game dalam ground truth
    for game in ground_truth:
        try:
            # Jika game ada dalam rekomendasi yang dihasilkan model
            if game in recommendations:
                # Ubah set menjadi list untuk menjaga urutan perbandingan
                actual = list(ground_truth[game])
                predicted = list(recommendations[game])

                # Ubah list menjadi array NumPy untuk metrik sklearn
                actual_array = np.array(actual)
                predicted_array = np.array(predicted)

                # Pastikan elemen yang sama untuk perbandingan
                common_elements = list(set(actual_array) & set(predicted_array))

                # Sesuaikan array aktual dan prediksi untuk hanya menyertakan elemen yang sama
                actual_array_filtered = np.isin(actual_array, common_elements).astype(int)
                predicted_array_filtered = np.isin(predicted_array, common_elements).astype(int)

                # Hitung dan tambahkan skor
                precision.append(precision_score(actual_array_filtered, predicted_array_filtered, average='micro'))
                recall.append(recall_score(actual_array_filtered, predicted_array_filtered, average='micro'))
                f1.append(f1_score(actual_array_filtered, predicted_array_filtered, average='micro'))
            else:
                # Jika tidak ada rekomendasi untuk game ini, tambahkan skor 0
                precision.append(0)
                recall.append(0)
                f1.append(0)
        except Exception as e:
            print(f"Error evaluating game {game}: {e}")

    # Cetak hasil evaluasi
    print(f"{model_name} Evaluasi")
    print(f"Presisi: {sum(precision)/len(precision)}")
    print(f"Recall: {sum(recall)/len(recall)}")
    print(f"Skor F1: {sum(f1)/len(f1)}")

# Contoh ground truth (ganti dengan data aktual Anda)
ground_truth = defaultdict(list, {'Grand Theft Auto V': ['Red Dead Redemption 2']})

# Contoh rekomendasi content-based filtering (ganti dengan output model aktual Anda)
content_recommendations = defaultdict(list, {'Grand Theft Auto V': ['Hades']})

# Evaluasi model Content-Based Filtering
evaluate_model("Content-Based Filtering", content_recommendations, ground_truth)

# Contoh rekomendasi collaborative filtering (ganti dengan output model aktual Anda)
collaborative_recommendations = defaultdict(list, {'Grand Theft Auto V': ['Portal 2']})

# Evaluasi model Collaborative Filtering
evaluate_model("Collaborative Filtering", collaborative_recommendations, ground_truth)

"""Presisi (Precision): Nilai presisi 1.0 berarti bahwa semua rekomendasi yang diberikan oleh model adalah benar. Dengan kata lain, setiap game yang direkomendasikan oleh model memang sesuai dengan preferensi pengguna.

Recall: Nilai recall 1.0 menunjukkan bahwa model berhasil menemukan semua game yang relevan untuk pengguna. Artinya, tidak ada game yang relevan yang terlewatkan oleh model.

Skor F1 (F1 Score): Skor F1 adalah rata-rata harmonis dari presisi dan recall. Dengan nilai 1.0, ini berarti bahwa model memiliki keseimbangan yang sempurna antara presisi dan recall.
"""