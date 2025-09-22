from flask import Flask
#Hello
app = Flask(__name__)

@app.route('/')
def hello_world():

    test_str = " File changes to check PR"
    return 'Hello from Flask Dockerized!-->' + " "+ test_str

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
