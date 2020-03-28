import pandas as pd
import matplotlib.pyplot as plt
from basic_tests import dorchester_arr

testing = pd.read_csv("Miovision Data/Dorchester Road and Huron Church Road_tmc_data_test.csv")[["dt_bin", "Direction", "Movement Type",
                                                                                  "Vehicle Classification",
                                                                                  "Number of Vehicles"]]
print(dorchester_arr[0])


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


#print(totals)