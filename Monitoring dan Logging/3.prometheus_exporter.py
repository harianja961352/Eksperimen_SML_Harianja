from prometheus_client import start_http_server, Gauge, Counter, Summary
from flask import Flask, request
import time

# Inisialisasi Flask
app = Flask(__name__)

# --- KRITERIA 4: TIGA METRIK UTAMA ---

# 1. Metrik Nilai Prediksi (Gauge)
# Menampilkan nilai hasil prediksi terakhir
LAST_PREDICTION = Gauge('bike_predictions_value', 'Value of the last rental prediction')

# 2. Metrik Jumlah Request (Counter)
# Menghitung total berapa kali prediksi dilakukan
PREDICTION_REQUESTS = Counter('bike_predictions_requests_total', 'Total number of prediction requests')

# 3. Metrik Latensi/Waktu Inferensi (Summary)
# Mengukur berapa lama proses update metrik berlangsung
PREDICTION_LATENCY = Summary('bike_predictions_latency_seconds', 'Time spent processing prediction update')

@app.route('/update')
def update_metrics():
    # Mulai hitung waktu untuk latensi
    start_time = time.time()
    
    # Tambahkan hitungan pada jumlah request
    PREDICTION_REQUESTS.inc()
    
    # Mengambil nilai dari parameter 'value' di URL
    value = request.args.get('value', default=0, type=int)
    
    # Update nilai prediksi terakhir
    LAST_PREDICTION.set(value)
    
    # Hitung durasi proses dan catat ke latensi
    duration = time.time() - start_time
    PREDICTION_LATENCY.observe(duration)
    
    return f"Metrik diperbarui! Prediksi: {value}, Total Request: {PREDICTION_REQUESTS}, Latensi: {duration:.4f}s"

if __name__ == '__main__':
    # 1. Jalankan server Prometheus di port 8000
    # Nantinya di Prometheus/Grafana cari: bike_predictions_value, bike_predictions_requests_total, dll.
    start_http_server(8000)
    print("Prometheus Exporter berjalan di port 8000...")
    
    # 2. Jalankan server Flask di port 8001 untuk menerima data dari Streamlit
    app.run(port=8001)