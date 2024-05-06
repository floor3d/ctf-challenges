# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and additional files
COPY filesystem/pwnme.py /app/
COPY filesystem/file.txt /app/
COPY filesystem/bruh.txt /app/
COPY filesystem/hello.txt /app/
COPY filesystem/slime.txt /app/

# Install socat
RUN apt-get update && apt-get install -y socat

# Expose the port on which socat will listen
EXPOSE 1337

# Run pwnme.py with socat
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:python pwnme.py"]
