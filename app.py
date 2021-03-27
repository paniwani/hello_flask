from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, JPO here is a random number: ' + str(np.random.rand(1)) + '!'