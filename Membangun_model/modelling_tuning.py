import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 1. Load data hasil preprocessing
# Pastikan path file csv sesuai dengan struktur folder kamu
train_df = pd.read_csv('data_preprocessing/hour_cleaned.csv') 
X_train = train_df.drop('cnt', axis=1) # Sesuaikan nama kolom target
y_train = train_df['cnt']

# 2. Setup MLflow Tracking (Ganti dengan URL DagsHub kamu)
mlflow.set_tracking_uri("https://dagshub.com/harianja961352/Eksperimen_SML_Harianja.mlflow")
#mlflow.set_experiment("/") # Menggunakan default experiment agar pasti terdeteksi
#mlflow.set_experiment("0")
# Ganti baris set_experiment yang lama dengan ini:
experiment_name = "Bike_Sharing_Tuning_New"
try:
    mlflow.set_experiment(experiment_name)
except:
    mlflow.create_experiment(experiment_name)
    mlflow.set_experiment(experiment_name)
    
with mlflow.start_run(run_name="RandomForest_Tuning"):
    # 3. Definisikan Model dan Parameter yang akan diuji
    rf = RandomForestRegressor(random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }

    # 4. Pencarian Parameter Terbaik (Hyperparameter Tuning)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, 
                               cv=3, scoring='neg_mean_squared_error', verbose=2)
    grid_search.fit(X_train, y_train)

    # 5. Catat Parameter Terbaik dan Metrik ke MLflow
    best_params = grid_search.best_params_
    mlflow.log_params(best_params)
    
    best_model = grid_search.best_estimator_
    predictions = best_model.predict(X_train)
    mse = mean_squared_error(y_train, predictions)
    
    mlflow.log_metric("mse", mse)
    
    # 6. Simpan Model Terbaik sebagai Artifak
    mlflow.sklearn.log_model(best_model, "best_rf_model")

    print(f"Tuning selesai! Parameter terbaik: {best_params}")