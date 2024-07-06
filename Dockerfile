# Use the official Python image from the Docker Hub
FROM python:3

# Set the working directory in the container
WORKDIR /DirApp

# Copy the requirements.txt file into the container
COPY . . 

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app runs on
EXPOSE 8000

# Define the command to run the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi"]
