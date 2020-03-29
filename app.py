from flask import Flask
from flask import render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graphs_test

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)
