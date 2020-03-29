import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr, malden_arr, totten_arr
import pandas_bokeh
import sys


plt.close('all')

pd.set_option('plotting.backend', 'pandas_bokeh')

i = sys.argv[1]
j = sys.argv[2]
k = sys.argv[3]

pandas_bokeh.output_file("/static/views/graph" + i + j + k + ".html")

def plot_one(og, d, title):
    plt.close('all')
    graph_title = title
    if (d==0):
        df = og.iloc[:, :6]
    else:
        df = og.iloc[:, np.r_[0, d*6+1:d*6+6]]
    df_grouped = df.groupby([df.index.hour, df.index.minute]).mean()
    df_grouped.plot(title=graph_title)
    ax = plt.axes()
    ax.set_xlabel("Time of day (hour, minute)")
    ax.set_ylabel("# of vehicles")

    plt.show()

# arr = array of dfs representing an intersection
# d = direction (N = 0, E = 1, S = 2, W = 3)
# i = index of arr with the df you want to graph
def plot_intersection(arr, d, i, graph_title):
    plt.close('all')

    if (d==0):
        df = arr[i].iloc[:, :6]
    else:
        df = arr[i].iloc[:, np.r_[0, d*6+1:d*6+4]]
    df_grouped = df.groupby([df.index.hour, df.index.minute]).mean()
    df_grouped.plot(title=graph_title, xlabel='Time of day (hour, minute)', ylabel='Number of Vehicles')
    plt.show()

# plot_intersection(dorchester_arr,3, 5)

intersections = [dorchester_arr, malden_arr, totten_arr]

# intersection: 0 = dorch, 1 = malden, 2 = totten
def plot_any(intersection, d, i):
    intersection_dict = {0: 'Huron Church & Dorchester', 1: 'Huron Church & Malden', 2: 'Huron Church & Totten'}
    d_dict = {0: 'Southbound', 1: 'Westbound', 2: 'Northbound', 3: 'Eastbound'}
    i_dict = {0: 'General Traffic', 1: 'Single-Unit Trucks', 2: 'Articulated Trucks', 3: 'Buses',
              4: 'Work Vans', 5: 'Bicycles', 6: 'Pedestrians'}
    graph_title = d_dict[d] + " " + i_dict[i] + " on " + intersection_dict[intersection]
    plot_intersection(intersections[intersection], d, i, graph_title)

plot_any(i, j, k)


##### MOST OF BELOW CAN NOW BE COMPLETED WITH PLOT_ANY #####
### Setup
# d_lights_n = dorchester_arr[0].iloc[:, :6]
# dlnr = d_lights_n.groupby([d_lights_n.index.hour, d_lights_n.index.minute]).mean()
# plt.figure()
# dlnr.plot()
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



