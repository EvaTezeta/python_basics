import pandas as pd
import matplotlib.pyplot as plt

# Import the data using pandas
df = pd.read_csv("Flights-Trains.csv", sep = ",")

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

#Display the chart
plt.show()