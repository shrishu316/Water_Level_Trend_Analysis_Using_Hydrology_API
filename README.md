# Water Level Trend Analysis Using Hydrology API

## Project Overview
This project automates the retrieval, cleaning, and visualization of water level data from the public hydrology API. Data is fetched at hourly intervals, and trends for selected rivers are analyzed using a moving average technique. The results are visualized using Seaborn and Matplotlib, highlighting key trends in water levels over specific periods.

## Features
- **Automated Data Fetching**: The pipeline pulls data from the hydrology API at hourly intervals.
- **Data Cleaning**: Ensures data consistency by removing duplicates and handling missing values.
- **Trend Analysis**: Calculates a rolling window moving average to reveal water level trends.
- **Visualization**: Generates plots of water levels over time, saved as high-resolution images.
- **Configurable Stations**: Users can specify the rivers they want to monitor.

## Data Pipeline Structure
1. **Data Ingestion**: 
   - Fetches water level data in CSV format from the external API.
   - Appends new data to a local CSV file.
   
2. **Data Cleaning**: 
   - Converts water level measurement timestamps to `datetime`.
   - Ensures water level data is numeric and handles missing values.

3. **Data Transformation**:
   - Filters data for specific rivers and timeframes.
   - Computes a 3-period rolling average to smooth water level fluctuations.
   
4. **Visualization**:
   - Line plots displaying actual and moving average water levels.
   - Separate visualizations for each selected river.
  ### Water level trends for selected rivers
   ![water_high_level_trends_for_selected_rivers](https://github.com/user-attachments/assets/c32af35a-a341-4f07-9545-e4038da3ddbb)
  ### Water level trends for selected high discharge rivers
   ![water_level_trends_selected_high_discharge_rivers](https://github.com/user-attachments/assets/6cb0c9cb-b25e-4ee9-853c-16734c731003)



## How to Run the Project
### Prerequisites:
- Python 3.x
- Install the required Python packages by running:
  ```bash
  pip install -r requirements.txt
