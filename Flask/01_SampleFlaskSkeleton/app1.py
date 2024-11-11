from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Siddhesh'

@app.route('/members')
def hello_members():
    return 'Hello World from Siddhesh Badakh'

if __name__ == '__main__':
    app.run(debug=True)
