FROM python:3.11
WORKDIR /app
COPY . /app
RUN apt -qq update
RUN pip install -r requirements.txt
CMD ["python", "botai.py"]
