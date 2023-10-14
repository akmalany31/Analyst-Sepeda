# Panduan Menjalankan Dashboard Peminjaman Sepeda

Ini adalah panduan sederhana untuk menjalankan dashboard Peminjaman Sepeda yang telah Anda buat.

## Persyaratan Prasyarat

Sebelum Anda dapat menjalankan dashboard, pastikan Anda memiliki persyaratan prasyarat berikut:

1. **Python**: Pastikan Anda telah menginstal Python di komputer Anda. Anda dapat mengunduh Python dari [python.org](https://www.python.org/).

2. **Paket Python**: Pastikan Anda telah menginstal semua paket Python yang dibutuhkan. Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal:

   ```bash
   conda create --name main-ds python=3.9
   conda activate main-ds
   pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
   ```

## Run Streamlit

```bash
streamlit run dashboard.py
```
