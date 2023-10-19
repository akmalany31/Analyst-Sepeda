import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from sklearn.cluster import KMeans

sns.set(style='dark')

# JUDUL
st.markdown(
    """
    <h1 style="text-align: center;">Dashboard Peminjaman Sepeda</h1>
    """,
    unsafe_allow_html=True
)

day = pd.read_csv("day.csv")
day.head()

st.write('<div style="text-align: center;">Analisis Peminjaman Sepeda.',
         unsafe_allow_html=True)

# Pilih Pertanyaan
option = st.selectbox('Pilih Pertanyaan:', ('',
                      ' Apakah jenis hari (holiday, weekday, workingday) mempengaruhi peminjaman sepeda?', 'Apakah cuaca(weathersit) mempengaruhi peminjaman sepeda?'))

if option == 'Apakah cuaca mempengaruhi peminjaman sepeda?':
    # Clustering
    X = day[['weathersit']]
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)
    day['cluster'] = kmeans.labels_

    # Visualisasi histogram peminjaman sepeda berdasarkan cuaca di setiap kluster
    plt.figure(figsize=(12, 6))

    # Loop melalui setiap kluster
    for cluster in day['cluster'].unique():
        plt.subplot(1, n_clusters, cluster + 1)
    plt.hist(day[day['cluster'] == cluster]['weathersit'],
             bins=4, range=(1, 4), rwidth=0.8)
    plt.xlabel('Cuaca (weathersit)')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.title(f'Kluster {cluster + 1}')
    plt.suptitle(
        'Histogram Peminjaman Sepeda Berdasarkan Cuaca di Setiap Kluster')
    plt.show()

    st.write('Berdasarkan visualisasi data, cuaca (weathersit) mempengaruhi peminjaman sepeda, dimana saat cuaca 1 sepeda paling banyak dipinjam, diikuti cuaca 2, dan cuaca 3 sedikit, cuaca 4 tidak ada peminjaman sepeda.')

elif option == 'Apakah jenis hari (hari libur, hari kerja, dan hari biasa) mempengaruhi peminjaman sepeda?':
    day['jenis_hari'] = day.apply(lambda row: 'Hari Libur' if row['holiday'] == 1 else (
        'Hari Kerja' if row['workingday'] == 1 else 'Hari Biasa'), axis=1)

    # Menampilkan distribusi jumlah peminjaman sepeda berdasarkan jenis hari
    plt.figure(figsize=(10, 6))
    sns.histplot(data=day, x='cnt', hue='jenis_hari', bins=20, kde=True)
    plt.xlabel('Jumlah Peminjaman Sepeda (cnt)')
    plt.title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Jenis Hari')
    plt.show()

    st.write('Berdasarkan visualisasi data, jenis hari mempengaruhi peminjaman sepeda. Dimana saat hari kerja peminjaman sepeda banyak dilakukan, diikuti dengan hari biasa dan hari libur.')

else:
    # KOSONG
    st.write('')
