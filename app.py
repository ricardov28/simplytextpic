from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body style="background-color:black;"><p style="color:white;">This is the latest picture</p></body></html>'

if __name__ == '__main__':
    app.run()
