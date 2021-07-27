FROM python:3.7
RUN mkdir /app
COPY app.py /app/app.py
WORKDIR /app
RUN pip install Flask
CMD ["python", "app.py"]
