FROM python:3.9

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    xvfb \
    chromium-driver \
    chromium

RUN pip install selenium pandas openpyxl

WORKDIR /app

COPY . /app

VOLUME [ "/app/data" ]

ENTRYPOINT ["python"]

CMD ["acoes.py"]