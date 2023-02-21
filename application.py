from flask import Flask

application = Flask(__name__)

app = application

@app.route('/')
def home():
    return "You are in home"



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)