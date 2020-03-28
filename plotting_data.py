import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr, malden_arr, totten_arr

# Plots right, left &
d_lights_n = dorchester_arr[0].iloc[:, :6]
plt.ylabel('Amount of Traffic')
plt.xlabel('Date/Time')
d_lights_n.set_index('Start Time', inplace=True)
ax1 = d_lights_n['Thru'].plot(label="Through")
ax2 = d_lights_n['Right'].plot(label="Right")
ax3 = d_lights_n['Left'].plot(label="Left")
ax4 = d_lights_n['U-Turn'].plot(label="U-Turn")
plt.legend(loc="upper right")
plt.show()