import pandas as pd
import os 

def load_data(filepath: str):
    """Membaca data CSV penjualan dari folder raw"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} tidak ditemukan.")
    data = pd.read_csv(filepath)
    print(f"Data berhasil dimuat: {data.shape[0]} baris, {data.shape[1]} kolom")
    return data

if __name__ == "__main__":
    df = load_data("data/raw/penjualan.csv")
    print(df.head())