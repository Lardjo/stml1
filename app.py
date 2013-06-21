# all the imports
from flask import Flask, render_template

# configuration
DEBUG = True
SECRET_KEY = 'development key'

# create application
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()