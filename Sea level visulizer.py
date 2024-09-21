import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('sea_level_data.csv')

# Extract years and sea levels
years = data['Year']
sea_levels = data['Sea_Level']

# Fit a linear regression model to predict sea levels
# Calculate the slope and intercept using numpy
slope, intercept = np.polyfit(years, sea_levels, 1)

# Create a range of years from 2000 to 2050
future_years = np.arange(2000, 2051)

# Predict sea levels for future years
predicted_sea_levels = slope * future_years + intercept

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(years, sea_levels, label='Historical Sea Levels', marker='o')
plt.plot(future_years, predicted_sea_levels, label='Predicted Sea Levels', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Sea Level (mm)')
plt.title('Sea Level Rise Prediction')
plt.axvline(x=2050, color='red', linestyle='--', label='Year 2050')
plt.legend()
plt.grid()
plt.show()

# Print the predicted sea level for 2050
predicted_2050 = slope * 2050 + intercept
print(f'Predicted sea level in 2050: {predicted_2050:.2f} mm')
