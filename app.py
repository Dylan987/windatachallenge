from flask import Flask
from flask import render_template
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



@app.route('/home.html')
@app.route('/home')
def hello_world():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(debug=True)
