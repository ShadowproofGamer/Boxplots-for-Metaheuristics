import matplotlib.pyplot as plt
import numpy as np

# Data - replace these with your actual statistics
min_vals = [954,
            1074,
            1387
            ]
max_vals = [977,
            1141,
            1488
            ]
means = [964,
         1111,
         1412
         ]
std_devs = [8, 16, 27]

data = [
    [954,	977,	964,	8.16]
]

# Calculate Q1 and Q3 based on mean and standard deviation
q1 = [mean - std for mean, std in zip(data[2], data[3])]
q3 = [mean + std for mean, std in zip(data[2], data[3])]

# Prepare data for boxplot (min, q1, mean, q3, max)
box_data = [
    [min_vals[0], q1[0], means[0], q3[0], max_vals[0]],
    # [min_vals[1], q1[1], means[1], q3[1], max_vals[1]],
    # [min_vals[2], q1[2], means[2], q3[2], max_vals[2]],
]

# Create figure and axis
fig, ax = plt.subplots()

print(box_data[0])
# Create the box plot using 'ax.bxp' for custom statistics
ax.bxp([{
    'whislo': min_val,
    'med': mean,
    'q1': q1,
    'q3': q3,
    'whishi': max_val,
    'fliers': []  # Add empty list for 'fliers'
} for min_val, q1, mean, q3, max_val in box_data], showmeans=False)

# Set category names and labels
ax.set_xticklabels(['Category 1'])
plt.ylabel('Values')
plt.title('Custom Box Plot with Min, Max, Mean, and Std Dev')

# Show the plot
plt.show()
