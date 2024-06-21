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
### producrtion server
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