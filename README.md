# 📊 Dashboard Penjualan Interaktif

Proyek ini dibuat oleh **Ashar Talatee** sebagai latihan profesional membangun
dashboard analisis penjualan yang otomatis dan interaktif.

## 🎯 Fitur yang Akan Dibangun
- Load & clean data penjualan otomatis
- Visualisasi interaktif (produk terlaris, pendapatan, tren)
- Update data otomatis
- Kirim laporan via Telegram

## 🧩 Struktur Folder

## 🧩 Hari 2 – Data Pipeline
- Dataset contoh: `data/raw/penjualan.csv`
- Script: `src/data_pipeline/load_data.py`, `clean_data.py`
- Output: `data/processed/penjualan_bersih.csv`

Progres:

✅ Data dummy dibuat  
✅ Script load & clean otomatis  
✅ Siap dipakai untuk eksplorasi (Hari 3)

## 📊 Hari 3 – Eksplorasi & Validasi Data

### Tujuan
Menemukan insight dasar dari data penjualan untuk membangun dashboard.

### Output
- `data/processed/agregat_harian.csv` – total pendapatan per tanggal
- `data/processed/produk_terlaris.csv` – produk dengan pendapatan tertinggi
- `data/processed/pendapatan_kategori.csv` – pendapatan berdasarkan kategori
- `notebooks/data_exploration.ipynb` – analisis dan visualisasi awal

## 🎨 Hari 4 – Dashboard Dasar (UI/UX)

### Tujuan
Membangun tampilan dasar dashboard interaktif menggunakan Streamlit.

### Fitur
- Sidebar filter (tanggal & kategori)
- Metrik utama: pendapatan, transaksi, produk terlaris
- Tabel data dinamis
- Grafik tren penjualan (Plotly)

### File Baru
- `src/dashboard/components.py`
- `src/dashboard/charts.py`
- `assets/style.css`

### Cara Menjalankan
```bash
streamlit run src/dashboard/app.py


## 📅 Hari 5 – Dashboard Interaktif

### Fitur Baru
- Filter tanggal dan kategori
- KPI cards (Total pendapatan, transaksi, produk terlaris)
- Grafik interaktif (line, bar, pie)
- Layout profesional menggunakan Streamlit + Plotly

### Struktur Folder Baru
- `src/dashboard/components/` berisi modul modular (filter, chart, KPI)
- `src/dashboard/app.py` sebagai main entry point dashboard

