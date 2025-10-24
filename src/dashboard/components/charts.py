import plotly.express as px
import streamlit as st
import pandas as pd

def show_charts(df: pd.DataFrame):
    st.subheader("📈 Tren Penjualan Harian")
    daily_sales = df.groupby('tanggal')['pendapatan'].sum().reset_index()
    fig = px.line(daily_sales, x='tanggal', y='pendapatan', markers=True, title="Total Penjualan per Hari")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🏆 Top Produk")
    top_products = df.groupby('produk')['pendapatan'].sum().reset_index().sort_values(by='pendapatan', ascending=False).head(10)
    fig2 = px.bar(top_products, x='pendapatan', y='produk', orientation='h', title="10 Produk Terlaris", text='pendapatan')
    fig2.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🍰 Pendapatan per Kategori")
    category_income = df.groupby('kategori')['pendapatan'].sum().reset_index()
    fig3 = px.pie(category_income, values='pendapatan', names='kategori', title="Distribusi Pendapatan per Kategori")
    st.plotly_chart(fig3, use_container_width=True)
