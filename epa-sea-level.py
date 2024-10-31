# Assign the data file to a variable 'df' for simplicity, and adjust the code accordingly

# Load the data from the uploaded CSV file
df = pd.read_csv('C:/Users/edj36/OneDrive/Documents/epa-sea-level.csv')

# Scatter plot of the data using Year and CSIRO Adjusted Sea Level
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='b', s=10)

# Perform linear regression on the entire dataset
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Generate x values from the starting year to 2050 for prediction
years_extended = pd.Series(range(df['Year'].min(), 2051))
predicted_sea_level_full = intercept + slope * years_extended

# Plot the line of best fit using the full dataset
plt.plot(years_extended, predicted_sea_level_full, label='Fit (1880-2050)', color='r')

# Filter data from the year 2000 onward and perform linear regression
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Predict sea level change from 2000 onward using the slope from recent data
predicted_sea_level_recent = intercept_recent + slope_recent * years_extended

# Plot the line of best fit using data from 2000 onward
plt.plot(years_extended, predicted_sea_level_recent, label='Fit (2000-2050)', color='g')

# Labeling the plot
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Show plot
plt.show()
