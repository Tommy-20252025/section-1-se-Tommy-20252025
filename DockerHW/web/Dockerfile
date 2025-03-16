# 步驟 1: 從官方 Python 映像開始
FROM python:3.11-slim

# 步驟 2: 設定工作目錄（這是容器內的目錄，程式會在這裡運行）
WORKDIR /web

# 步驟 3: 複製當前目錄的所有檔案到容器的 /app 目錄中
COPY . /web

# 步驟 4: 安裝 Python 的需求庫（如果有 requirements.txt）
# 如果你的應用程式有依賴其他 Python 函式庫，請確保有一個 requirements.txt 文件
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# 步驟 5: 執行 main.py 程式
CMD ["python", "main.py"]
