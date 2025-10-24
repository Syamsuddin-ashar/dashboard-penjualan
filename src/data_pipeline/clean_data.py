import pandas as pd
from datetime import datetime

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Membersihkan dan menyiapkan data penjualan"""
    # 1. Pastikan kolom tanggal dalam format datetime
    df['tanggal'] = pd.to_datetime(df['tanggal'], errors='coerce')

    # 2. Hilangkan baris dengan tanggal kosong
    df = df.dropna(subset=['tanggal'])

    # 3. Isi nilai kosong di kolom jumlah atau harga_total dengan 0
    df['jumlah'] = df['jumlah'].fillna(0)
    df['harga_total'] = df['harga_total'].fillna(0)

    # 4. Tambahkan kolom 'pendapatan'
    df['pendapatan'] = df['jumlah'] * df['harga_total']

    # 5. Urutkan data berdasarkan tanggal
    df = df.sort_values(by='tanggal')

    # 6. Reset index
    df = df.reset_index(drop=True)

    return df

if __name__ == "__main__":
    raw_path = "data/raw/penjualan.csv"
    save_path = "data/processed/penjualan_bersih.csv"

    df = pd.read_csv(raw_path)
    cleaned_df = clean_data(df)
    cleaned_df.to_csv(save_path, index=False)
    print(f"Data bersih disimpan di: {save_path}")
    print(cleaned_df.head())
