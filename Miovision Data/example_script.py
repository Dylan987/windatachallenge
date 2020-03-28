import pandas as pd

# Define the files we want to load
travel_time_file = "Travel Time - train dataset - Raw.csv"
tmc_file = "Dorchester Road and Huron Church Road_tmc_data_train.csv"

# Load the TMC data into a dataframe
tmc_df = pd.read_csv(tmc_file, parse_dates=["dt_bin"])
tt_df = pd.read_csv(travel_time_file, parse_dates=["Start time", "End time"])

# Some code to prepare and aggreagte the travel time data

tt_agg_df = tt_df.groupby(
    [
        pd.Grouper(key="Start time", freq="15Min"),  # You can adjust the frequency here
        "Source name",
        "Source ID",
        "Destination name",
        "Destination ID",
    ]
).agg(["mean", "median", "count"])

# Reset the index to make joining simpler
tt_agg_df.reset_index()

# And let's flatten the column hiearchy
tt_agg_df.columns = [" ".join(col).strip() for col in tt_agg_df.columns.values]

# We can also aggregate the TMC data
tmc_agg_df = tmc_df.groupby(["Intersection Name", "Intersection ID", "dt_bin"]).sum()
tmc_agg_df = tmc_agg_df.reset_index()

# Here's how you can join the datasets together

merged_df = pd.merge(
    tmc_agg_df,
    tt_agg_df,
    how="left",
    left_on=["dt_bin", "Intersection ID"],
    right_on=["Start time", "Source ID"],
)
