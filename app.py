from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, LOOK AT THIS v2: ' + str(np.random.rand(1)) + '!'