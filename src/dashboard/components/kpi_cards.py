import streamlit as st

def show_kpi_cards(df):
    if df.empty:
        st.info("Tidak ada data untuk ditampilkan berdasarkan filter saat ini.")
        return

    total_penjualan = df["total_penjualan"].sum() if "total_penjualan" in df.columns else 0
    total_transaksi = len(df)
    rata2_transaksi = df["total_penjualan"].mean() if "total_penjualan" in df.columns else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Penjualan", f"Rp {total_penjualan:,.0f}")
    col2.metric("Jumlah Transaksi", f"{total_transaksi:,}")
    col3.metric("Rata-rata per Transaksi", f"Rp {rata2_transaksi:,.0f}")
