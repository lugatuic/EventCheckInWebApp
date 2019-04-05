from flask import Flask

#name helps Flask to locate the templates and other files

app = Flask(__name__)

from app import routes

app.run(debug=True)


















