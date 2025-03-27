import xarray as xr

# Load the NetCDF file
hydro_profile = xr.open_dataset('C:/Users/hie/pe_tan/pypsa-earth/resources/renewable_profiles/profile_hydro.nc')

# Display the structure of the dataset
print(hydro_profile)

# Display the variables in the dataset
print(hydro_profile.variables)

# Display the data for a specific variable (e.g., "inflow")
if "inflow" in hydro_profile:
    print(hydro_profile["inflow"])


import matplotlib.pyplot as plt

# Plot the inflow time series for a specific location (if applicable)
if "inflow" in hydro_profile:
    hydro_profile["inflow"].isel(plant=0).plot(figsize=(15, 5))  # Replace "bus=0" with the appropriate dimension
    plt.title("Hydro Inflow Time Series")
    plt.ylabel("Inflow")
    plt.xlabel("Time")
    plt.show()


    #import pandas as pd

    # Convert the NetCDF dataset to a pandas DataFrame
    #hydro_df = hydro_profile.to_dataframe()

    # Save the DataFrame to an Excel file
    #hydro_df.to_excel('C:/Users/hie/pe_tan/pypsa-earth/resources/renewable_profiles/profile_hydro.xlsx')

    #print("Hydro profile has been saved to Excel.")

