# Bike Sharing Data Dashboard ✨

Ini adalah proyek akhir Data Analytics yang menampilkan dashboard interaktif menggunakan Streamlit untuk menganalisis data penyewaan sepeda (Bike Sharing Dataset).

## 1. Setup Environment
Untuk menjalankan proyek ini, pastikan kamu sudah menginstal Python. Kamu bisa memilih salah satu dari dua cara di bawah ini untuk melakukan *setup environment*:

### Pilihan A: Menggunakan Anaconda
Buka **Anaconda Prompt** dan jalankan perintah berikut secara berurutan:
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

### Pilihan B: Menggunakan Terminal/Shell (Pipenv)
Buka **terminal/command prompt**,lalu jalankan perintah berikut:
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## 2. Menjalankan Dashboard Secara Local
Setelah environment berhasil diaktifkan dan seluruh library di dalam file requirements.txt selesai diinstal, jalankan perintah berikut di terminal untuk membuka dashboard secara lokal:
```bash
streamlit run dashboard.py

## 💡 Catatan Penting Sebelum Submit Ulang:
1. **Pastikan file `requirements.txt` benar-benar ada** di dalam repositori GitHub kamu. Jika file itu tidak ada, *reviewer* tidak akan bisa melakukan `pip install -r requirements.txt`. Isi file tersebut biasanya berupa daftar library: `pandas`, `matplotlib`, `seaborn`, `streamlit`, dll.
2. **Cek nama file dashboard kamu.** Di panduan tertulis `streamlit run dashboard.py`. Jika nama file Python kamu untuk dashboard bukan `dashboard.py` (misalnya `app.py` atau `main.py`), pastikan kamu mengubah teks di README tersebut menyesuaikan nama file aslimu ya! 

Silakan salin kode di atas ke dalam file `README.md` kamu di GitHub, lalu *commit* perubahan tersebut. Semangat, tinggal selangkah lagi!