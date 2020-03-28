import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr

testing = pd.read_csv("Miovision Data/Dorchester Road and Huron Church Road_tmc_data_test.csv")[["dt_bin", "Direction",
                                                                                                 "Movement Type",
                                                                                                 "Vehicle Classification",
                                                                                                 "Number of Vehicles"]]
placeholder = ["Right", "Thru", "Left", "U-Turn"]
for i in range(1, 4):
    for j in range(0, 4):
        placeholder.append(placeholder[j] + "." + str(i))

dfs = [pd.DataFrame({placeholder[i]: dorchester_arr[j][placeholder[i]] for i in range(len(placeholder))}) for j in range(len(dorchester_arr))]
sum_arr = [0 for i in range(len(dorchester_arr))]
shift = 5764

for j in range(len(dfs)):
    for header in placeholder:
        for i in range(0 + shift * j, len(dfs[j]["Right"]) + shift * j):
            sum_arr[j] += dfs[j][header][i]

print(sum_arr)

vehicles_aggregate = testing[["Vehicle Classification", "Number of Vehicles"]]

vehicles = testing["Vehicle Classification"]
unique_vehicles = []
for vehicle in vehicles:
    if vehicle not in unique_vehicles:
        unique_vehicles.append(vehicle)

#print(vehicles_aggregate)

totals = {unique_vehicles[i]: 0 for i in range(0, len(unique_vehicles))}

for i in range(0, len(vehicles_aggregate)):
    totals[vehicles_aggregate["Vehicle Classification"][i]] += vehicles_aggregate["Number of Vehicles"][i]


print(totals)