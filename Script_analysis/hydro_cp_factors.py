import pandas as pd
import numpy as np

def process_hydro(aha_file, pypsa_powerplants_file, output_file):
    """
    Process the African Hydropower Atlas (AHA) dataset and match it with PyPSA-Earth power plants.

    Parameters:
    -----------
    aha_file : str
        Path to the AHA dataset file.
    pypsa_powerplants_file : str
        Path to the PyPSA-Earth power plants file.
    output_file : str
        Path to save the processed capacity factors.

    Returns:
    --------
    None
    """
    # Load AHA dataset
    aha_data = pd.read_csv(aha_file)

    # Load PyPSA-Earth power plants
    pypsa_powerplants = pd.read_csv(pypsa_powerplants_file)

    # Match power plants by name or location (adjust matching logic as needed)
    matched_data = pd.merge(
        pypsa_powerplants,
        aha_data,
        left_on="name",  # Adjust column names as needed
        right_on="plant_name",
        how="inner"
    )

    # Clean and extract capacity factors
    capacity_factors = matched_data[["plant_id", "monthly_capacity_factors"]]

    # Save the processed capacity factors
    capacity_factors.to_csv(output_file, index=False)




def create_time_series(monthly_capacity_factors_file, output_file):
    """
    Convert monthly capacity factors into hourly time series.

    Parameters:
    -----------
    monthly_capacity_factors_file : str
        Path to the file containing monthly capacity factors.
    output_file : str
        Path to save the hourly time series.

    Returns:
    --------
    None
    """
    # Load monthly capacity factors
    monthly_data = pd.read_csv(monthly_capacity_factors_file)

    # Create an hourly time series for each plant
    hourly_data = {}
    for _, row in monthly_data.iterrows():
        plant_id = row["plant_id"]
        monthly_factors = row["monthly_capacity_factors"].split(",")  # Assuming comma-separated values
        monthly_factors = [float(factor) for factor in monthly_factors]

        # Generate hourly values for each month
        hourly_factors = []
        for month, factor in enumerate(monthly_factors, start=1):
            days_in_month = pd.Period(f"2020-{month:02d}").days_in_month  # Leap year-safe
            hourly_factors.extend([factor] * days_in_month * 24)

        hourly_data[plant_id] = hourly_factors

    # Convert to DataFrame
    hourly_df = pd.DataFrame(hourly_data)

    # Save the hourly time series
    hourly_df.to_csv(output_file, index=False)