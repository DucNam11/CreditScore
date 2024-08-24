FROM python:3.12.3-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["dashboard.py"]