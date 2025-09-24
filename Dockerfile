FROM python:3.13-slim

WORKDIR /Vacado

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DEBUG=False
ENV PORT=8000

CMD ["uvicorn", "main:vacado", "--host", "0.0.0.0", "--port", "8000"]