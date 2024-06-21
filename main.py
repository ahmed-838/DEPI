from flask import Flask, render_template
import logging as logs
app = Flask(__name__, static_folder='./static')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
