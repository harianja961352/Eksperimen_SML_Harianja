import pandas as pd
import mlflow
import mlflow.sklearn
import dagshub
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. SETUP DAGSHUB & MLFLOW
# GANTI link di bawah dengan link .mlflow yang kamu salin dari DagsHub
MLFLOW_TRACKING_URI = "https://dagshub.com/harianja961352/Eksperimen_SML_Harianja.mlflow"
dagshub.init(repo_owner='harianja961352', repo_name='Eksperimen_SML_Harianja', mlflow=True)
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("Eksperimen_Bike_Sharing_Harianja")

# 2. LOAD DATA
df = pd.read_csv('hour_cleaned.csv')
X = df.drop(columns=['cnt'])
y = df['cnt']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. TRAINING MODEL DENGAN MLFLOW
with mlflow.start_run():
    # Parameter model
    n_estimators = 100
    max_depth = 10
    
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    
    # Prediksi & Evaluasi
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)
    
    # Log Parameter & Metric ke DagsHub
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)
    
    # Simpan Model
    mlflow.sklearn.log_model(model, "random_forest_model")
    
    print(f"Model berhasil dilatih! RMSE: {rmse:.2f}, R2: {r2:.2f}")