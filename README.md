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
  
  ### Water level trends for high discharge selected rivers
   ![water_high_level_trends_for_selected_rivers](https://github.com/user-attachments/assets/c32af35a-a341-4f07-9545-e4038da3ddbb)
 
  ### Water level trends comparison for selected high discharge rivers
   ![water_level_trends_selected_high_discharge_rivers](https://github.com/user-attachments/assets/c25c5958-ea82-4785-a337-394a5898522f)
 
  ### Water level trends for low discharge selected rivers
   ![water_level_trends_for_selected_rivers_new](https://github.com/user-attachments/assets/43176a6a-f692-4a0e-8dc6-b6548b09b133)
   
  ### Water level trends comparison selected low discharge rivers
   ![water_level_trends_selected_low_discharge_rivers](https://github.com/user-attachments/assets/bd5033f4-60da-4e48-8db4-72f64b44318d)
   
