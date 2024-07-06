# Python App 

## Development 
```bash 
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
``` 
## Create Virtual Environment <venv>
```bash
python -m venv venv
``` 
## Open the venv in the terminal 
```bash 
source venv/bin/activate 
```
## Create requirements txt file
```bash
pip freeze > requirements.txt 
```
## servers in python 
### production server
``` gunicorn server that running with wsgi file ```<br>
```to install it use the following command : ```
```bash 
pip install gunicorn 
```
```to run a production server after creating a wsgi file  use the following command : ```
```bash 
gunicorn wsgi
```
### the content of the wsgi.py file should be like : 
```bash
from main import app as application

if __name__ == "__main__" : 
    application.run()
``` 
`what is ((jinja)) ?? => jinja is a templateing engine syntax  that allow us to excute code like variables or functions inside html code or any simeler things `

### to install the used modules from the requirements.txt file use the following command : 
```bash 
 pip install -r requirements.txt   
```
## Logging and Linting 
### at first import the logging library 
```python 
import logging
```
### there is 5 levels of logging
=> every method of them take string parameter to display 

```python 
import logging

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
```
## Dockerization 
### Create docker file : 
1. create file named " Dockerfile "
in the Dockerfile 
at first we spacify the python version 
```docker
FROM python:3 
```
then follow the comming steps 
```bash
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

```

## this line means that 
### CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi"] 

### What Happens When the Container Starts
When you start a Docker container using an image that includes this CMD, Docker will execute the command specified (gunicorn -b 0.0.0.0:8000 wsgi).
gunicorn will start as the main process inside the container.

It will bind to port 8000 on all interfaces (0.0.0.0), allowing external access to your application.

gunicorn will look for the wsgi module or application inside the container and run it. This assumes that you have configured your Docker image to include the necessary files and dependencies, such as your Python application code and any required libraries specified in requirements.txt.
