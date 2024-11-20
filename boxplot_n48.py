import matplotlib.pyplot as plt
import numpy as np

# Data in the format [min, max, avg, stddev]
data = [
    [1074,	1250,	1113,	29.80],  # Category 1: [min, max, avg, stddev]
    [1074,	1133,	1111,	19.68],  # Category 2: [min, max, avg, stddev]
    [1074,	1141,	1111,	15.71],
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
optimal_value = 1073
ax.axhline(optimal_value, color='red', linestyle='--', label=f'Optimal Value = {optimal_value}')
greedy = 1260
ax.axhline(greedy, color='blue', linestyle='--', label=f'Greedy = {optimal_value}')

# Set category names and labels
ax.set_xticklabels(['EA', 'TS', 'SA'])
plt.ylabel('Fitness')
plt.title('Fitness for problem A-n48-k7')

# Show the plot
plt.show()
