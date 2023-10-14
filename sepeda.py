import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# JUDUL
st.markdown(
    """
    <h1 style="text-align: center;">Dashboard Peminjaman Sepeda</h1>
    """,
    unsafe_allow_html=True
)

hour = pd.read_csv("day.csv")
hour.head()

day = pd.read_csv("hour.csv")
day.head()

st.write('<div style="text-align: center;">Analisis Peminjaman Sepeda.',
         unsafe_allow_html=True)

# Pilih Pertanyaan
option = st.selectbox('Pilih Pertanyaan:', ('',
                      'Apakah jenis hari (hari libur, hari kerja, dan hari biasa) mempengaruhi peminjaman sepeda?', 'Apakah cuaca mempengaruhi peminjaman sepeda?'))

if option == 'Apakah cuaca mempengaruhi peminjaman sepeda?':
    # Analisis untuk DAY
    plt.figure(figsize=(10, 6))
    sns.histplot(data=day, x='cnt', hue='weathersit', bins=20, kde=True)
    plt.xlabel('Jumlah Peminjaman Sepeda (cnt)')
    plt.title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Cuaca (DAY)')
    st.pyplot(plt.gcf())
    st.write('Berdasarkan hasil visualisasi dataset DAY diatas, cuaca (weathersit) mempengaruhi peminjaman sepeda, dimana sepeda paling banyak dipinjam saat cuaca 1, diikuti cuaca 2, dan cuaca 3 sedikit, cuaca 4 sangat sedikit')

  # Analisis untuk HOUR
    plt.figure(figsize=(10, 6))
    sns.histplot(data=hour, x='cnt', hue='weathersit', bins=20, kde=True)
    plt.xlabel('Jumlah Peminjaman Sepeda (cnt)')
    plt.title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Cuaca (HOUR)')
    st.pyplot(plt.gcf())
    st.write('Berdasarkan hasil visualisasi dataset HOUR diatas, cuaca (weathersit) mempengaruhi peminjaman sepeda, dimana sepeda paling banyak dipinjam saat cuaca 1, diikuti cuaca 2, dan cuaca 3 sedikit')

elif option == 'Apakah jenis hari (hari libur, hari kerja, dan hari biasa) mempengaruhi peminjaman sepeda?':
    day['jenis_hari'] = day.apply(lambda row: 'Hari Libur' if row['holiday'] == 1 else (
        'Hari Kerja' if row['workingday'] == 1 else 'Hari Biasa'), axis=1)

    # Analisis untuk DAY
    st.write("DAY")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=day, x='cnt', hue='jenis_hari', bins=20, kde=True)
    plt.xlabel('Jumlah Peminjaman Sepeda (cnt)')
    plt.title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Jenis Hari (DAY)')
    st.pyplot(plt.gcf())

    hour['jenis_hari'] = hour.apply(lambda row: 'Hari Libur' if row['holiday'] == 1 else (
        'Hari Kerja' if row['workingday'] == 1 else 'Hari Biasa'), axis=1)

    # Analisis untuk HOUR
    st.write("HOUR")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=hour, x='cnt', hue='jenis_hari', bins=20, kde=True)
    plt.xlabel('Jumlah Peminjaman Sepeda (cnt)')
    plt.title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Jenis Hari (HOUR)')
    st.pyplot(plt.gcf())

    st.write('Berdasarkan hasil visualisasi data, jenis hari mempengaruhi peminjaman sepeda. Dimana saat hari kerja peminjaman sepeda banyak dilakukan, diikuti dengan hari biasa dan hari libur.')

else:
    # KOSONG
    st.write('')
