import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    Y = df["CSIRO Adjusted Sea Level"]
    X = df["Year"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(X, Y)

    # Create first line of best fit
    res = linregress(X, Y)
    X_pred = pd.Series([i for i in range(1880, 2051)])
    Y_pred = res.slope*X_pred + res.intercept
    plt.plot(X_pred, Y_pred, "r")

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    X2 = df2['Year']
    Y2 = df2["CSIRO Adjusted Sea Level"]
    res2 = linregress(X2, Y2)
    X2_pred = pd.Series([i for i in range(2000, 2051)])
    Y2_pred = res2.slope*X2_pred + res2.intercept
    plt.plot(X2_pred, Y2_pred, 'green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()