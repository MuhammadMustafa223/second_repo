FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install numpy pandas matplotlib seaborn pytest

COPY . /app

CMD ["python"]
