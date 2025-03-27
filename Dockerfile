# Base image
FROM python:3.13-bookworm

# Set environment variables for python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt .

# Install Python dependecies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code into the container
COPY . .

# Expose the port that Gunicorn will use
EXPOSE 8000

# Use the entrypoint script as the CMD
CMD ["/app/entrypoint.sh"]