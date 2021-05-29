FROM python:3.8-slim-buster

# Install git
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# Copy the app
COPY src/ /app
COPY requirements.txt /app

WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]