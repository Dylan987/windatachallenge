import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr, malden_arr, totten_arr, dorchester_data
from day_aggregate import plot_any, plot_one

merge_df = pd.concat(dorchester_arr)
# print(merge_df.index)
# print(merge_df)
agg_df = merge_df.resample('15min').sum()
# print(agg_df)
# print(agg_df.describe())
# print(dorchester_arr[0].describe())
# plot_one(agg_df, 0, "Aggregate Northbound Traffic")
# plot_any(dorchester_arr, 0, 0)
print(list(agg_df))
agg_df['n_sum'] = agg_df[['Right', 'Thru', 'Left', 'U-Turn', 'Peds CW', 'Peds CCW']].sum(axis=1)
agg_df['e_sum'] = agg_df[['Right.1', 'Thru.1', 'Left.1', 'U-Turn.1', 'Peds CW.1', 'Peds CCW.1']].sum(axis=1)
agg_df['s_sum'] = agg_df[['Right.2', 'Thru.2', 'Left.2', 'U-Turn.2', 'Peds CW.2', 'Peds CCW.2']].sum(axis=1)
agg_df['w_sum'] = agg_df[['Right.3', 'Thru.3', 'Left.3', 'U-Turn.3', 'Peds CW.3', 'Peds CCW.3']].sum(axis=1)
agg_df['ns_max'] = agg_df[['n_sum', 's_sum']].max(axis=1)
agg_df['ew_max'] = agg_df[['e_sum', 'w_sum']].max(axis=1)
print(agg_df)

plt.ylabel('Amount of Traffic')
plt.xlabel('Date/Time')
ax1 = agg_df['ns_max'].plot(label="N-S Traffic")
ax2 = agg_df['ew_max'].plot(label="E-W Traffic")
plt.legend(loc="upper right")
plt.show()

# merge all in arr together
# resample ('15min')