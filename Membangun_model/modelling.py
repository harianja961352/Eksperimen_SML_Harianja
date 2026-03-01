import pandas as pd
import mlflow
import mlflow.sklearn
import dagshub
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 1. SETUP DAGSHUB & MLFLOW
# GANTI link di bawah dengan link .mlflow yang kamu salin dari DagsHub
MLFLOW_TRACKING_URI = "https://dagshub.com/harianja961352/Eksperimen_SML_Harianja.mlflow"
dagshub.init(repo_owner='harianja961352', repo_name='Eksperimen_SML_Harianja', mlflow=True)
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("Eksperimen_Bike_Sharing_Harianja")

# 2. LOAD DATA
df = pd.read_csv('data_preprocessing/hour_cleaned.csv')
X = df.drop(columns=['cnt'])
y = df['cnt']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- KRITERIA 2: MENGAKTIFKAN AUTOLOG (WAJIB) ---
# Mengaktifkan autolog sebelum proses training dimulai
mlflow.sklearn.autolog()
# ------------------------------------------------

# 3. TRAINING MODEL DENGAN MLFLOW
with mlflow.start_run():
    # Parameter model
    n_estimators = 100
    max_depth = 10
    
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    # Begitu .fit() dipanggil, MLflow Autolog akan mencatat semuanya secara otomatis
    model.fit(X_train, y_train)
    
    # Prediksi & Evaluasi
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)
    

    
    print(f"Model berhasil dilatih! RMSE: {rmse:.2f}, R2: {r2:.2f}")

# Menyimpan model ke folder Dashboard agar bisa dipakai Streamlit
joblib.dump(model, '../Dashboard/bike_model.joblib')
print("Model berhasil disimpan ke folder Dashboard!")