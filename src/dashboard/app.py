import streamlit as st
import pandas as pd
from components.filters import show_filters
from components.charts import show_charts
from components.kpi_cards import show_kpi_cards

st.set_page_config(page_title="Dashboard Penjualan", page_icon="📈", layout="wide")

# ====== HEADER ======
st.image("../../assets/logo.png", width=120)
st.title("📊 Dashboard Penjualan Interaktif")
st.markdown("""
Selamat datang di dashboard analisis penjualan.  
Gunakan filter di sebelah kiri untuk eksplorasi performa penjualan berdasarkan tanggal & kategori.
""")

# ====== LOAD DATA ======
df = pd.read_csv("../../data/processed/penjualan_bersih.csv")
df['tanggal'] = pd.to_datetime(df['tanggal'])

# ====== FILTER ======
selected_range, selected_category = show_filters(df)

mask = (df['tanggal'] >= pd.to_datetime(selected_range[0])) & (df['tanggal'] <= pd.to_datetime(selected_range[1]))
if selected_category != "Semua":
    mask &= (df['kategori'] == selected_category)
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
