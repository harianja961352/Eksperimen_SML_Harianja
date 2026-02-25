<<<<<<< HEAD
import pandas as pd
import os

def load_data(file_path):
    """Fungsi untuk memuat data mentah Bike Sharing."""
    print(f"Loading data from {file_path}...")
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Fungsi utama untuk melakukan pembersihan dan transformasi data.
    Langkah ini harus sama dengan apa yang dilakukan di file .ipynb
    """
    print("Mulai proses preprocessing data...")
    df_clean = df.copy()
    
    # 1. Menghapus kolom yang tidak relevan sebagai fitur
    # 'instant' adalah index, 'dteday' sudah diwakili kolom 'yr', 'mnth', 'weekday'
    cols_to_drop = ['instant', 'dteday']
    df_clean = df_clean.drop(columns=cols_to_drop, errors='ignore')
    
    # 2. Mencegah Data Leakage (Kebocoran Data)
    # Target kita adalah 'cnt' (total sewa). Kolom 'casual' + 'registered' = 'cnt'
    # Jika fitur ini dimasukkan, model akan curang. Jadi harus dihapus.
    leakage_cols = ['casual', 'registered']
    df_clean = df_clean.drop(columns=leakage_cols, errors='ignore')
    
    # 3. Menangani Missing Values (Meskipun data ini biasanya bersih, ini best practice)
    df_clean = df_clean.dropna()
    
    print("Preprocessing selesai. Kolom yang tersisa:")
    print(df_clean.columns.tolist())
    
    return df_clean

def save_data(df, output_path):
    """Fungsi untuk menyimpan data yang sudah diproses."""
    # Pastikan folder output ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data bersih berhasil disimpan di {output_path}")

if __name__ == "__main__":
    # Tentukan path file input dan output sesuai struktur folder GitHub kamu
    INPUT_PATH = "data_raw/hour.csv"
    OUTPUT_PATH = "data_preprocessing/hour_cleaned.csv"
    
    # Jalankan pipeline
    try:
        raw_data = load_data(INPUT_PATH)
        cleaned_data = preprocess_data(raw_data)
        save_data(cleaned_data, OUTPUT_PATH)
        print("🎉 Pipeline otomatisasi berhasil dieksekusi!")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
=======
import pandas as pd
import os

def load_data(file_path):
    """Fungsi untuk memuat data mentah Bike Sharing."""
    print(f"Loading data from {file_path}...")
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Fungsi utama untuk melakukan pembersihan dan transformasi data.
    Langkah ini harus sama dengan apa yang dilakukan di file .ipynb
    """
    print("Mulai proses preprocessing data...")
    df_clean = df.copy()
    
    # 1. Menghapus kolom yang tidak relevan sebagai fitur
    # 'instant' adalah index, 'dteday' sudah diwakili kolom 'yr', 'mnth', 'weekday'
    cols_to_drop = ['instant', 'dteday']
    df_clean = df_clean.drop(columns=cols_to_drop, errors='ignore')
    
    # 2. Mencegah Data Leakage (Kebocoran Data)
    # Target kita adalah 'cnt' (total sewa). Kolom 'casual' + 'registered' = 'cnt'
    # Jika fitur ini dimasukkan, model akan curang. Jadi harus dihapus.
    leakage_cols = ['casual', 'registered']
    df_clean = df_clean.drop(columns=leakage_cols, errors='ignore')
    
    # 3. Menangani Missing Values (Meskipun data ini biasanya bersih, ini best practice)
    df_clean = df_clean.dropna()
    
    print("Preprocessing selesai. Kolom yang tersisa:")
    print(df_clean.columns.tolist())
    
    return df_clean

def save_data(df, output_path):
    """Fungsi untuk menyimpan data yang sudah diproses."""
    # Pastikan folder output ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data bersih berhasil disimpan di {output_path}")

if __name__ == "__main__":
    # Tentukan path file input dan output sesuai struktur folder GitHub kamu
    INPUT_PATH = "data_raw/hour.csv"
    OUTPUT_PATH = "data_preprocessing/hour_cleaned.csv"
    
    # Jalankan pipeline
    try:
        raw_data = load_data(INPUT_PATH)
        cleaned_data = preprocess_data(raw_data)
        save_data(cleaned_data, OUTPUT_PATH)
        print("🎉 Pipeline otomatisasi berhasil dieksekusi!")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
>>>>>>> f363770c053cc00794ac2ed4ca49f7ebc0087512
