import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr, malden_arr, totten_arr

def plot_data(df): # plot data for one direction of traffic at an intersection
    ax1 = df['Thru'].plot(label="Through")
    ax2 = df['Right'].plot(label="Right")
    ax3 = df['Left'].plot(label="Left")
    ax4 = df['U-Turn'].plot(label="U-Turn")
    plt.legend(loc="upper right")
    plt.show()

### Setup
d_lights_n = dorchester_arr[0]
d_lights_n['Start Time'] = pd.to_datetime(d_lights_n['Start Time'])
d_lights_n.set_index(['Start Time'], inplace=True)

## Filter by day (monday = 0)
d_lights_n_monday = d_lights_n[d_lights_n.index.weekday == 0]

## Resample: split data at different intervals (ex. every day or every 30 min instead of 15min)
# dlnr = d_lights_n_monday.resample('D').mean()

## Group by day (view average data for one day)
# dlnr = d_lights_n.groupby(lambda x: x.hour+x.minute, axis=0).mean() # doesn't work
dlnr = d_lights_n.groupby([d_lights_n.index.hour, d_lights_n.index.minute]).mean()
print(dlnr)
plot_data(dlnr)
