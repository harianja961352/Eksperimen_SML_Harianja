import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Judul Aplikasi
st.title("🚲 Prediksi Penyewaan Sepeda (Bike Sharing)")
st.write("Aplikasi ini memprediksi jumlah penyewaan sepeda berdasarkan kondisi cuaca.")

# 2. Muat Model
model = joblib.load('bike_model.joblib')

# 3. Sidebar untuk Input Data
st.sidebar.header("Input Kondisi Cuaca")

def user_input_features():
    season = st.sidebar.selectbox("Musim", (1, 2, 3, 4), format_func=lambda x: {1:"Springer", 2:"Summer", 3:"Fall", 4:"Winter"}[x])
    yr = st.sidebar.selectbox("Tahun", (0, 1), format_func=lambda x: "2011" if x==0 else "2012")
    mnth = st.sidebar.slider("Bulan", 1, 12, 1)
    hr = st.sidebar.slider("Jam", 0, 23, 12)
    holiday = st.sidebar.selectbox("Hari Libur?", (0, 1), format_func=lambda x: "Tidak" if x==0 else "Ya")
    weekday = st.sidebar.slider("Hari (0=Minggu, 6=Sabtu)", 0, 6, 3)
    workingday = st.sidebar.selectbox("Hari Kerja?", (0, 1), format_func=lambda x: "Tidak" if x==0 else "Ya")
    weathersit = st.sidebar.selectbox("Kondisi Cuaca", (1, 2, 3, 4))
    temp = st.sidebar.slider("Temperatur (Normalized)", 0.0, 1.0, 0.5)
    atemp = st.sidebar.slider("Feeling Temperatur (Normalized)", 0.0, 1.0, 0.5)
    hum = st.sidebar.slider("Kelembaban (Normalized)", 0.0, 1.0, 0.5)
    windspeed = st.sidebar.slider("Kecepatan Angin (Normalized)", 0.0, 1.0, 0.1)

    data = {
        'season': season, 'yr': yr, 'mnth': mnth, 'hr': hr, 'holiday': holiday,
        'weekday': weekday, 'workingday': workingday, 'weathersit': weathersit,
        'temp': temp, 'atemp': atemp, 'hum': hum, 'windspeed': windspeed
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# 4. Tampilkan Prediksi
st.subheader("Hasil Prediksi")
prediction = model.predict(input_df)
st.metric(label="Estimasi Jumlah Penyewa", value=int(prediction[0]))

# 5. Visualisasi Sederhana (Opsional tapi bagus untuk nilai tambahan)
st.subheader("Analisis Input")
fig, ax = plt.subplots()
sns.barplot(x=input_df.columns, y=input_df.iloc[0], ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)