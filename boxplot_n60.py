import matplotlib.pyplot as plt
import numpy as np

# Data in the format [min, max, avg, stddev]
data = [
    [1368,	1499,	1442,	44.53],  # Category 1: [min, max, avg, stddev]
    [1392,	1451,	1425,	15.66],  # Category 2: [min, max, avg, stddev]
    [1387,	1488,	1412,	27.19],
]

# Prepare the boxplot data by calculating Q1, Q3, and setting median to avg
box_data = []
for d in data:
    min_val, max_val, avg, stddev = d
    q1 = avg - stddev  # Q1 (1st Quartile) = avg - stddev
    q3 = avg + stddev  # Q3 (3rd Quartile) = avg + stddev
    box_data.append({
        'med': avg,       # Median is the average
        'q1': q1,         # Lower quartile (Q1)
        'q3': q3,         # Upper quartile (Q3)
        'whislo': min_val,  # Min value
        'whishi': max_val,  # Max value
        'fliers': []      # No outliers (fliers)
    })

# Create figure and axis
fig, ax = plt.subplots()

# Create the box plot using 'ax.bxp' with the prepared statistics
ax.bxp(box_data, showmeans=False)

# Add a horizontal line for the Optimal and greedy
optimal_value = 1354
ax.axhline(optimal_value, color='red', linestyle='--', label=f'Optimal Value = {optimal_value}')
greedy = 1548
ax.axhline(greedy, color='blue', linestyle='--', label=f'Greedy = {optimal_value}')

# Set category names and labels
ax.set_xticklabels(['EA', 'TS', 'SA'])
plt.ylabel('Fitness')
plt.title('Fitness for problem A-n60-k9')

# Show the plot
plt.show()
