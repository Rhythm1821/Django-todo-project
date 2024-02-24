FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/

# Run the Django application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]