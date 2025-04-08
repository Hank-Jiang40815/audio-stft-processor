# 音訊 STFT 處理工具

這個套件提供了音訊信號的短時傅立葉轉換(STFT)和逆轉換(iSTFT)處理功能。可用於音訊頻譜分析、修改和信號處理。

## 功能特點

- 支援音訊檔案的 STFT 分析
- 支援 iSTFT 將頻域資料轉回音訊
- 多種視窗函數選擇
- 可調整的參數設定
- 視覺化頻譜圖
- 自動生成分析報告

## 安裝方式

### 使用 pip 安裝

```bash
pip install audio-stft-processor
```

### 從原始碼安裝

```bash
git clone https://github.com/Hank-Jiang40815/audio-stft-processor.git
cd audio-stft-processor
pip install -e .
```

### 使用 Docker

```bash
docker build -t audio-stft-processor .
docker run -v $(pwd)/data:/app/data audio-stft-processor
```

## 使用方式

### 基本使用

```python
from audio_stft_processor import STFTProcessor

# 初始化處理器
processor = STFTProcessor(window_size=2048, hop_length=512)

# 處理音訊檔案
stft_data = processor.process_file('input.wav')

# 產生頻譜圖
processor.plot_spectrogram(stft_data, 'spectrogram.png')

# 還原音訊
processor.reconstruct_audio(stft_data, 'output.wav')
```

### 命令列使用

```bash
audiostft --input input.wav --output output.wav --window hann --size 2048 --hop 512
```

## 版權和授權

此專案採用 MIT 授權條款 - 詳情請參閱 LICENSE 檔案。