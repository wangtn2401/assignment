# Sử dụng một hình ảnh Python làm cơ sở
FROM python:3.10

# Tạo thư mục làm việc và thiết lập làm thư mục mặc định
WORKDIR /app

# Sao chép toàn bộ mã nguồn vào thư mục làm việc
COPY . .

# Khởi chạy ứng dụng Python Proxy
CMD ["python", "proxy.py"]
