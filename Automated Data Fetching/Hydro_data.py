import requests
import pandas as pd
import time
import os

def fetch_and_append_data(url_csv, filename):
    # Fetch data from URL
    dane_csv = requests.get(url_csv)
    
    # Check if the CSV file exists
    if os.path.exists(filename):
        # Read the existing CSV data into a DataFrame
        existing_data = pd.read_csv(filename)
        
        # Read the new CSV data into a DataFrame
        new_data = pd.read_csv(url_csv, usecols=['id_stacji', 'stacja', 'stan_wody', 'stan_wody_data_pomiaru'])
        
        # Filter out any rows that are already in the existing data
        new_data = new_data[~new_data['stan_wody_data_pomiaru'].isin(existing_data['stan_wody_data_pomiaru'])]
        
        # Append the new data to the existing DataFrame
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        
        # Write the combined DataFrame to the CSV file
        combined_data.to_csv(filename, index=False)
        print("New data appended to", filename)
    else:
        # If the CSV file does not exist, simply write the new data to the file
        new_data = pd.read_csv(url_csv, usecols=['id_stacji', 'stacja', 'stan_wody', 'stan_wody_data_pomiaru'])
        new_data.to_csv(filename, index=False)
        print("New data saved to", filename)

# URL for fetching data
url_csv = "http://danepubliczne.imgw.pl/api/data/hydro/format/csv"

# Filename for saving data
filename = 'Hydro_data.csv'

# Set the maximum number of iterations
max_iterations = 24
iterations = 0

# Run the data fetching and appending process
while iterations < max_iterations:
    fetch_and_append_data(url_csv, filename)
    iterations += 1
    # Wait for 1 hour before fetching data again
    time.sleep(3600)  # 3600 seconds = 1 hour

print("Automation stopped after", max_iterations, "iterations.")
