from flask import Flask
from flask import render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import graphs_test

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html", data=graphs_test.get_data())

