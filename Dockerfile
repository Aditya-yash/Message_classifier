FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK resources during build
RUN python -m nltk.downloader punkt stopwords

COPY . .

ENV STREAMLIT_PORT=8501
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

 