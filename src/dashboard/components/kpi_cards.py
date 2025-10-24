import streamlit as st
import pandas as pd

def show_kpi_cards(df: pd.DataFrame):
    total_penjualan = df['pendapatan'].sum()
    total_transaksi = df.shape[0]
    produk_terlaris = df.groupby('produk')['pendapatan'].sum().idxmax()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pendapatan", f"Rp {total_penjualan:,.0f}")
    col2.metric("Total Transaksi", total_transaksi)
    col3.metric("Produk Terlaris", produk_terlaris)