FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt requirements.txt

# Update pip to the latest version
RUN python -m pip install --upgrade pip

# Install the dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD ["python", "app.py"]