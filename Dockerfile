# Gunakan image Python dasar
FROM python:3.10-slim

# Set folder kerja di dalam kontainer
WORKDIR /app

# Salin file requirements dan instal library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode proyek ke dalam kontainer
COPY . .

# Perintah untuk menjalankan aplikasi (sesuaikan jika perlu)
CMD ["python", "modelling.py"]