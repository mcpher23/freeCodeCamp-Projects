import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, linewidths=0.1)


    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(x,y)

    extended = pd.Series(range(1880, 2051, 1))

    future_line = [slope*oldx + intercept for oldx in extended]

    plt.plot(extended, future_line, 'r', label='fitted line')


    # Create second line of best fit

    sample = df[df['Year'] >= 2000]

    sample_dates = pd.Series(range(2000, 2051, 1))

    sample_slope, sample_intercept, sample_r_value, sample_p_value, sample_std_err = linregress(sample['Year'],sample['CSIRO Adjusted Sea Level'])

    line = [sample_slope*oldx + sample_intercept for oldx in sample['Year']]

    sample_line = [sample_slope*oldx + sample_intercept for oldx in sample_dates]

    # If the slope of the line after the dataset indicated a continue in rising sea levels plot the prediction otherwise just plot the most recent years from 2000
    if sample_slope >= slope:
        plt.plot(sample_dates, sample_line, 'g', label='fitted line')
    else:
        plt.plot(sample['Year'], line, 'g', label='fitted line')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()