from flask import Flask

application = Flask(__name__)

app = application

@app.route('/')
def home():
    return "I'm changing my message"



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)