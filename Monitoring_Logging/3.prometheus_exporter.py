from prometheus_client import start_http_server, Gauge
from flask import Flask, request

# Inisialisasi Flask untuk menerima data dari Streamlit
app = Flask(__name__)

# Metrik untuk memantau nilai prediksi terakhir
LAST_PREDICTION = Gauge('bike_predictions_total', 'Value of the last rental prediction')

@app.route('/update')
def update_metrics():
    # Mengambil nilai dari parameter 'value' di URL
    value = request.args.get('value', default=0, type=int)
    LAST_PREDICTION.set(value)
    return f"Metrik diperbarui ke: {value}"

if __name__ == '__main__':
    # Jalankan server prometheus di port 8000
    start_http_server(8000)
    # Jalankan server Flask untuk menerima update data
    app.run(port=8001)