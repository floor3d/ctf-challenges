# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script
COPY ech-no.py /app/
COPY flag.txt /app/

# Install socat
RUN apt-get update && apt-get install -y socat

# Expose the port on which socat will listen
EXPOSE 1337

# Run pwnme.py with socat
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:python ech-no.py"]
