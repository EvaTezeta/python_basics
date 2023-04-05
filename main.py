import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import the data using pandas
df = pd.read_csv("Flights-Trains.csv", sep = ",")

###### Barplot
#Group WeeksAhead and calculate the sum of Ticket price per week
plot_df = df.groupby('WeeksAhead')['Ticket price'].sum()

#Create a bar chart with x and y axes
plt.bar(plot_df.index, plot_df.values)

#X-axis label
plt.xlabel('Weeks Ahead')

#Y-axis label
plt.ylabel('Sum of Ticket Prices')

#Set the title
plt.title('Total Ticket Prices by Weeks Ahead')

#Display the chart (doesn't work in replit)
#plt.show()

#Save plot in folder to the left
plt.savefig('barplot.png')

###### Line plot with for loop
routes = df['Route'].unique() 
#Loop each route for a separate plot
for route in routes:
    fig, ax = plt.subplots()
    plt.title(route)
    #Loop each mode for separate lines
    for mode in ['Plane', 'Train']:
        subset = df[(df['Route'] == route) & (df['Mode'] == mode)]
        #WeeksAhead on x-axis and price on y-axis, line = red if Plane
        ax.plot(subset['WeeksAhead'], subset['Ticket price'], color='red'
                if mode == 'Plane' else 'blue', label=mode)
    plt.legend()
    #plt.show() -> doesn't work in replit
    #Save the plot to a file
    filename = f"{route}.png"
    plt.savefig(filename)
    #Close the plot
    plt.close()

###### Basic scatter plot
# Generate some random data for x and y
x = np.random.randn(50)
y = np.random.randn(50)

# Create a new plt object for the scatter plot (otherwise it will take the data from the barplot)
fig, ax = plt.subplots()

# Create a scatter plot
ax.scatter(x, y)

# Add labels and title
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')
ax.set_title('Basic Scatter Plot')

# Show the plot 
#plt.show() -> doesn't work in replit

#Save plot in folder to the left
plt.savefig('scatterplot.png')

###### Histogram
# Generate some random data for the histogram
a = np.random.normal(170, 10, 250)

# Create a new plt object for the histogram plot
fig2, ax2 = plt.subplots()

# Create the histogram
ax2.hist(a)

# Add labels and title
ax2.set_xlabel('Data')
ax2.set_ylabel('Frequency')
ax2.set_title('Histogram of Random Data')

#plt.show()  -> doesn't work in replit

# Save the histogram plot to a file
plt.savefig('histogram.png')

