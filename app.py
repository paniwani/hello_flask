from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, SAST' + str(np.random.rand(1)) + '!'
