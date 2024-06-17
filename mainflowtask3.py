import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# example  data
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
sales = np.random.randint(100, 500, size=12)

# Plotting the bar chart
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='skyblue')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data - Bar Chart')
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()

# Plotting the line chart
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data - Line Chart')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
