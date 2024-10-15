import requests
import pandas as pd
from google.cloud import storage
import os
from io import StringIO

# Initialize Google Cloud Storage client
storage_client = storage.Client()

def fetch_and_append_data(request):
    # URL for fetching data
    url_csv = "http://danepubliczne.imgw.pl/api/data/hydro/format/csv"
    
    # GCS bucket and file details
    bucket_name = 'Hydro-data-store'
    file_name = 'Hydro_data.csv'
    
    # Fetch data from URL
    response = requests.get(url_csv)
    if response.status_code != 200:
        return f"Failed to fetch data from {url_csv}. Status code: {response.status_code}", 500

    # Convert the response content to a pandas DataFrame
    new_data = pd.read_csv(StringIO(response.text), usecols=['id_stacji', 'stacja', 'stan_wody', 'stan_wody_data_pomiaru'])
    
    # Reference the GCS bucket and file
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Check if the CSV file already exists in Cloud Storage
    if blob.exists():
        # Download the existing CSV file from Cloud Storage
        existing_data_string = blob.download_as_text()
        existing_data = pd.read_csv(StringIO(existing_data_string))
        
        # Filter out any rows that are already in the existing data
        new_data = new_data[~new_data['stan_wody_data_pomiaru'].isin(existing_data['stan_wody_data_pomiaru'])]
        
        # Append new data to the existing DataFrame
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        
        # Save the combined DataFrame back to Cloud Storage
        output = StringIO()
        combined_data.to_csv(output, index=False)
        blob.upload_from_string(output.getvalue())
        
        return f"New data appended to {file_name} in {bucket_name}", 200
    else:
        # If the CSV file does not exist, write the new data to Cloud Storage
        output = StringIO()
        new_data.to_csv(output, index=False)
        blob.upload_from_string(output.getvalue())
        
        return f"New data saved to {file_name} in {bucket_name}", 200
