FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY .. /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000