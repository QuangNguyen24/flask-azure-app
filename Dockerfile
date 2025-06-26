FROM python:3.9-slim

# Tạo thư mục làm việc
WORKDIR /app

# Cài đặt thư viện Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy toàn bộ mã nguồn
COPY . .

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
