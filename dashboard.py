import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(
    """
    <h1 style="text-align: center;">Dashboard Peminjaman Sepeda</h1>
    """,
    unsafe_allow_html=True
)

day = pd.read_csv("day.csv")

st.write('<div style="text-align: center;">Analisis Peminjaman Sepeda.',
         unsafe_allow_html=True)

# Pilih Pertanyaan
option = st.selectbox('Pilih Pertanyaan:', [
    'Pilih Pertanyaan:',
    'Apakah jenis hari (holiday, weekday, workingday) mempengaruhi peminjaman sepeda?',
    'Apakah cuaca (weathersit) mempengaruhi peminjaman sepeda?'
])

if option == 'Apakah cuaca (weathersit) mempengaruhi peminjaman sepeda?':
    # Clustering
    X = day[['weathersit']]
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)
    day['cluster'] = kmeans.labels_

    # Visualisasi histogram peminjaman sepeda berdasarkan cuaca di setiap kluster
    fig, axs = plt.subplots(1, n_clusters, figsize=(12, 6))

    # Loop melalui setiap kluster
    for cluster in day['cluster'].unique():
        axs[cluster].hist(day[day['cluster'] == cluster]['weathersit'],
                          bins=4, range=(1, 4), rwidth=0.8)
        axs[cluster].set_xlabel('Cuaca (weathersit)')
        axs[cluster].set_ylabel('Jumlah Peminjaman Sepeda')
        axs[cluster].set_title(f'Kluster {cluster + 1}')
    plt.suptitle(
        'Histogram Peminjaman Sepeda Berdasarkan Cuaca di Setiap Kluster')

    # Visualisasinya
    st.pyplot(fig)

    with st.expander("Lihat penjelasan:"):
        st.write('Berdasarkan visualisasi data di atas, cuaca (weathersit) mempengaruhi peminjaman sepeda, dimana saat cuaca 1(Clear, Few clouds, Partly cloudy, Partly cloudy) sepeda paling banyak dipinjam, diikuti cuaca 2(Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist), dan cuaca 3(Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds) sedikit peminjaman, cuaca 4(Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) tidak ada peminjaman sepeda.')

elif option == 'Apakah jenis hari (holiday, weekday, workingday) mempengaruhi peminjaman sepeda?':
    # Jenis harinya
    day['jenis_hari'] = day.apply(lambda row: 'Hari Libur' if row['holiday'] == 1 else (
        'Hari Kerja' if row['workingday'] == 1 else 'Hari Biasa'), axis=1)

    # Menampilkan distribusi jumlah peminjaman sepeda berdasarkan jenis hari
    plt.figure(figsize=(10, 6))
    sns.histplot(data=day, x='cnt', hue='jenis_hari', bins=20, kde=True)
    plt.xlabel('Jumlah Peminjaman Sepeda (cnt)')
    plt.title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Jenis Hari')

    # Visualisasinya
    st.pyplot()

    with st.expander("Lihat penjelasan:"):
        st.write('Berdasarkan visualisasi data, jenis hari mempengaruhi peminjaman sepeda. Dimana saat hari kerja peminjaman sepeda banyak dilakukan, diikuti dengan hari biasa dan hari libur.')

else:
    st.write('<div style="text-align: center;">Dataset Characteristics',
             unsafe_allow_html=True)
    st.write("""
- instant: record index
- weekday: day of the week
- workingday: if day is neither weekend nor holiday is 1, otherwise is 0.
- weathersit:
  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- cnt: count of total rental bikes including both casual and registered
""")
