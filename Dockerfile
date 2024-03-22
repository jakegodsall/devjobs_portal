FROM python:3.11-alpine


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "fm_joblistings/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]