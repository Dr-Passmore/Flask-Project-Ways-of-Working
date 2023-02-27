from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import mimetypes
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


mimetypes.add_type("application/javascript", ".js", True)

if __name__ == '__main__':
   app.run()
   