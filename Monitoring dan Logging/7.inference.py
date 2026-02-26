import joblib
import pandas as pd

def run_inference(data):
    model = joblib.load('Dashboard/bike_model.joblib')
    prediction = model.predict(data)
    return prediction

# Contoh data dummy untuk tes
if __name__ == "__main__":
    test_data = pd.DataFrame([{
        'season': 1, 'yr': 0, 'mnth': 1, 'hr': 12, 'holiday': 0,
        'weekday': 3, 'workingday': 1, 'weathersit': 1,
        'temp': 0.5, 'atemp': 0.5, 'hum': 0.5, 'windspeed': 0.1
    }])
    print(f"Hasil Prediksi: {run_inference(test_data)}")