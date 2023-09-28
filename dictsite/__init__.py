import os
from flask import Flask

app = Flask(__name__)

#https://stackoverflow.com/questions/47687307/how-do-you-solve-the-error-keyerror-a-secret-key-is-required-to-use-csrf-whe
app.config['SECRET_KEY'] = os.urandom(32) 
