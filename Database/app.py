from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@86.21.126.234:3306/flask_gcp"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)