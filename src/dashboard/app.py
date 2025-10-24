import streamlit as st
import pandas as pd
from pathlib import Path
from components.filters import show_filters
from components.charts import show_charts
from components.kpi_cards import show_kpi_cards
import os

# ====== KONFIGURASI DASHBOARD ======
st.set_page_config(page_title="Dashboard Penjualan", page_icon="📈", layout="wide")

# ====== HEADER ======
# Dapatkan path absolut ke file logo (jika tidak ada, skip)
logo_path = Path(__file__).resolve().parents[2] / "assets" / "profile.jpg"
if logo_path.exists():
    st.image(str(logo_path), width=120)
else:
    st.write("🧩 (Logo belum tersedia)")

st.title("📊 Dashboard Penjualan Interaktif")
st.markdown("""
Selamat datang di dashboard analisis penjualan.  
Gunakan filter di sebelah kiri untuk eksplorasi performa penjualan berdasarkan tanggal & kategori.
""")

# ====== LOAD DATA ======
# Path absolut ke file CSV
data_path = Path(__file__).resolve().parents[2] / "data" / "processed" / "penjualan_bersih.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    st.success("✅ Data penjualan berhasil dimuat otomatis.")
else:
    st.warning("⚠️ File `penjualan_bersih.csv` belum ditemukan. Silakan upload manual di bawah ini.")
    uploaded_file = st.file_uploader("📂 Upload data penjualan (.csv)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Data berhasil di-upload!")
    else:
        st.stop()

# Pastikan kolom tanggal dalam format datetime
if "tanggal" in df.columns:
    df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")

# ====== FILTER ======
selected_range, selected_category = show_filters(df)

mask = (df["tanggal"] >= pd.to_datetime(selected_range[0])) & (df["tanggal"] <= pd.to_datetime(selected_range[1]))
if selected_category != "Semua":
    mask &= (df["kategori"] == selected_category)
filtered_df = df.loc[mask]

# ====== DASHBOARD CONTENT ======
with st.container():
    show_kpi_cards(filtered_df)

st.markdown("---")

with st.container():
    show_charts(filtered_df)

# ====== FOOTER ======
st.markdown("---")
st.caption("🚀 Dibuat oleh **Ashar Talatee** — Proyek Streamlit Level 1")
