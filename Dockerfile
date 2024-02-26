FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install pygame
CMD ["python", "tateti.py"]
