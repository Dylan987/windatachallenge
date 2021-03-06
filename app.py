from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import graphs_test
from day_aggregate import plot_any

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("site.html")

@app.route('/update_graph')
def update():
    data = request.args
    plot_any(data['intersection'], data['direction'], data['traffic'])
    return "it worked"

@app.route('/analysis.html')
def analysis():
    return render_template("analysis.html")


@app.route('/dashboard.html')
def hello_world():
    return render_template("site.html")


if __name__ == '__main__':
    app.run(debug=True)
