FROM python:3.10-slim
WORKDIR /app

# Salin requirements dari folder utama
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# SALIN file modelling.py DARI folder Membangun_model KE folder kerja /app
COPY Membangun_model/modelling.py .

# Salin folder data agar bisa dibaca oleh script
COPY data_preprocessing/ ./data_preprocessing/

CMD ["python", "modelling.py"]