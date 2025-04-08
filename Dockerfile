FROM python:3.9-slim

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    ffmpeg \
    libsndfile1 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 複製專案檔案
COPY . .

# 安裝套件相依
RUN pip install --no-cache-dir -r requirements.txt

# 開發模式安裝套件本身
RUN pip install -e .

# 設定環境變數
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# 建立資料目錄
RUN mkdir -p /app/data/input /app/data/output /app/data/reports

# 預設命令
CMD ["python", "-m", "audio_stft_processor.cli"]