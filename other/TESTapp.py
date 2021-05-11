'''from flask import Flask
app = Flask(__name__)
@app.route('/')

@app.route('/home')
def home():
    return('hello and welcome to the home page')

@app.route('/about')
def about():
    return 'This is the about page where we will tell you about our web application :)'
@app.route('/about/<word>')
def about1(word):
    return str(word)

if __name__ == "__main__":
    app.run(debug=True)'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)