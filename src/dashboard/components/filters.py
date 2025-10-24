import streamlit as st
import pandas as pd

def show_filters(df: pd.DataFrame):
    st.sidebar.header("Filter Data")

    #Filter tanggl
    min_date = df['tanggal'].min()
    max_date = df['tanggal'].max()
    selected_range = st.sidebar.date_input(
        "Pilih rentang tanggal",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    #Filter kategori
    categories = ["Semua"] + sorted(df['kategori'].unique().tolist())
    selected_category = st.sidebar.selectbox("Pilih Kategori Produk", categories)

    return selected_range, selected_category