import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_charts(df):
    if df.empty:
        st.info("Belum ada data untuk ditampilkan di grafik.")
        return

    # Grafik penjualan per hari
    st.subheader("📈 Tren Penjualan Harian")
    daily_sales = df.groupby("tanggal")["total_penjualan"].sum().reset_index()

    fig, ax = plt.subplots()
    ax.plot(daily_sales["tanggal"], daily_sales["total_penjualan"], marker="o")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Total Penjualan (Rp)")
    ax.grid(True)
    st.pyplot(fig)

    # Grafik penjualan per kategori
    if "kategori" in df.columns:
        st.subheader("📊 Penjualan Berdasarkan Kategori")
        category_sales = df.groupby("kategori")["total_penjualan"].sum().sort_values(ascending=False)

        fig2, ax2 = plt.subplots()
        ax2.bar(category_sales.index, category_sales.values)
        ax2.set_xlabel("Kategori Produk")
        ax2.set_ylabel("Total Penjualan (Rp)")
        ax2.set_xticklabels(category_sales.index, rotation=45, ha="right")
        st.pyplot(fig2)
