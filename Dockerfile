# 
FROM python:3.9

# 
WORKDIR /TestApiApp

# 
COPY ./requirements.txt /TestApiApp/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /TestApiApp/requirements.txt

# 
COPY ./app /TestApiApp/app

# 
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1000"]