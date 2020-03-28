from flask import Flask
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import graphs_test

app = Flask(__name__)
@app.route('/')
def hello_world():
    return graphs_test.get_data()

