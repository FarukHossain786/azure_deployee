from flask import Flask
from Deployee import Database
application = Flask(__name__)

app = application

@app.route('/')
def home():
    obj =Database.Database()
    return obj.fun()



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)