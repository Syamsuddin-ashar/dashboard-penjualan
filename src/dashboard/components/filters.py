import streamlit as st

def show_filters(df):
    st.sidebar.header("🔍 Filter Data")

    # Pastikan kolom tanggal dan kategori ada
    if "tanggal" not in df.columns or "kategori" not in df.columns:
        st.sidebar.warning("Kolom 'tanggal' atau 'kategori' tidak ditemukan di dataset.")
        return (None, None)

    # Filter tanggal
    min_date = df["tanggal"].min()
    max_date = df["tanggal"].max()

    selected_range = st.sidebar.date_input(
        "Pilih Rentang Tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # Filter kategori
    kategori_options = ["Semua"] + sorted(df["kategori"].dropna().unique().tolist())
    selected_category = st.sidebar.selectbox("Pilih Kategori Produk", kategori_options)

    return selected_range, selected_category
