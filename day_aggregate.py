import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr, malden_arr, totten_arr

plt.close('all')

def plot_data(df): # plot data for one direction of traffic at an intersection
    df.plot()
    plt.legend(loc="upper right")

# arr = array of dfs
# d = direction (N = 0, E = 1, S = 2, W = 3)
# i = index of arr with the df you want to graph
def plot_any(arr, d, i):
    d_dict = {0: 'Southbound', 1: 'Westbound', 2: 'Northbound', 3: 'Eastbound'}
    i_dict = {0: 'General Traffic', 1: 'Single-Unit Trucks', 2: 'Articulated Trucks', 3: 'Buses',
              4: 'Work Vans', 5: 'Bicycles', 6: 'Pedestrians'}
    graph_title= d_dict[d] + " " + i_dict[i]
    if (d==0):
        df = arr[i].iloc[:, :6]
    else:
        df = arr[i].iloc[:, np.r_[0, d*6+1:d*6+6]]
    df_grouped = df.groupby([df.index.hour, df.index.minute]).mean()
    ax = df_grouped.plot(title=graph_title)
    ax.set_xlabel("Time of day (hour, minute)")
    ax.set_ylabel("# of vehicles")
    plt.legend(loc="upper right")

plot_any(dorchester_arr,3, 5)
plt.show()

##### MOST OF BELOW CAN NOW BE COMPLETED WITH PLOT_ANY #####
### Setup
# d_lights_n = dorchester_arr[0].iloc[:, :6]
# d_lights_n['Start Time'] = pd.to_datetime(d_lights_n['Start Time'])
# d_lights_n.set_index(['Start Time'], inplace=True)

# d_sut_n = dorchester_arr[1].iloc[:,0:6]
# print(d_sut_n)
# d_lights_e = dorchester_arr[0].iloc[:, np.r_[0, 7:12]]
# d_sut_n['Start Time'] = pd.to_datetime(d_sut_n['Start Time'])
# d_sut_n.set_index(['Start Time'], inplace=True)

## Filter by day (monday = 0)
# d_lights_n_monday = d_lights_n[d_lights_n.index.weekday == 0]

## Resample: split data at different intervals (ex. every day or every 30 min instead of 15min)
# dlnr = d_lights_n_monday.resample('D').mean()

## Group by day (view average data for one day)
# dlnr = d_lights_n.groupby(lambda x: x.hour+x.minute, axis=0).mean() # doesn't work
# dlnr = d_sut_n.groupby([d_sut_n.index.hour, d_sut_n.index.minute]).mean()
#
# print(dlnr)
# plot_data(dlnr)
# plt.show()

# dler = d_lights_e.groupby([d_lights_e.index.hour, d_lights_e.index.minute]).mean()
# print(dler.info)
# plot_data(dler)
# plt.show()