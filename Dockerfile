# 使用轻量级 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录所有文件到容器
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir fastapi uvicorn transformers torch

# 暴露端口
EXPOSE 80

# 启动命令
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
