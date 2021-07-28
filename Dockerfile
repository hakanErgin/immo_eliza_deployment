FROM python:3.7
RUN mkdir /app
RUN mkdir /app/code
COPY code/app.py /app/code/app.py
WORKDIR /app
RUN pip install Flask
CMD ["python", "code/app.py"]
