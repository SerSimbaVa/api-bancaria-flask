# Etapa 1: Instalar dependencias
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

# Etapa 2: Imagen final minimalista
FROM python:3.11-slim

WORKDIR /app

# Agregar binarios de dependencias de builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["python", "run.py"]


