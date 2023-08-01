# Use the official Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Expose the port on which the Flask app is listening
EXPOSE 5005

# Command to run the Flask app using Waitress
CMD ["waitress-serve", "--listen=0.0.0.0:5005", "app:app"]
