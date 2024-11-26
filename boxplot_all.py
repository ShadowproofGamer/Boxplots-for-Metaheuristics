import matplotlib.pyplot as plt

# Data for each instance in the format [min, max, avg, stddev]
data = {
    "A-n32-k5": {
        "EA": [797, 833, 819, 14.74],
        "TS": [798, 829, 815, 14.17],
        "SA": [802, 829, 808, 10.56],
        "Optimal": 784,
        "Greedy": 906
    },
    "A-n37-k6": {
        "EA": [951, 1010, 970, 18.01],
        "TS": [951, 986, 964, 10.22],
        "SA": [951, 970, 955, 6.16],
        "Optimal": 949,
        "Greedy": 1063
    },
    "A-n39-k5": {
        "EA": [829, 843, 836, 4.12],
        "TS": [830, 878, 838, 14.27],
        "SA": [829, 837, 831, 2.55],
        "Optimal": 822,
        "Greedy": 924
    },
    "A-n45-k6": {
        "EA": [962, 1015, 980, 14.54],
        "TS": [956, 982, 972, 10.09],
        "SA": [954, 981, 966, 10.41],
        "Optimal": 944,
        "Greedy": 1122
    },
    "A-n48-k7": {
        "EA": [1074, 1250, 1113, 29.80],
        "TS": [1074, 1117, 1097, 16.70],
        "SA": [1074, 1127, 1102, 14.21],
        "Optimal": 1073,
        "Greedy": 1260
    },
    "A-n54-k7": {
        "EA": [1175, 1250, 1207, 24.13],
        "TS": [1172, 1227, 1197, 18.78],
        "SA": [1173, 1229, 1195, 17.01],
        "Optimal": 1167,
        "Greedy": 1385
    },
    "A-n60-k9": {
        "EA": [1368, 1499, 1442, 44.53],
        "TS": [1378, 1441, 1403, 21.38],
        "SA": [1364, 1413, 1391, 14.60],
        "Optimal": 1354,
        "Greedy": 1548
    }
}

# Prepare boxplot data
def prepare_box_data(stats):
    min_val, max_val, avg, stddev = stats
    q1 = avg - stddev  # Q1 (1st Quartile)
    q3 = avg + stddev  # Q3 (3rd Quartile)
    return {
        'med': avg,       # Median is the average
        'q1': q1,         # Lower quartile (Q1)
        'q3': q3,         # Upper quartile (Q3)
        'whislo': min_val,  # Min value
        'whishi': max_val,  # Max value
        'fliers': []      # No outliers (fliers)
    }

# Create figure and axes for 7 subplots
fig, axes = plt.subplots(2, 4, figsize=(18, 12), squeeze=True)
axes = axes.flatten()  # Flatten the axes array for easier iteration

for idx, (instance, algorithms) in enumerate(data.items()):
    ax = axes[idx]
    # Prepare boxplot data for EA, TS, SA
    box_data = [
        prepare_box_data(algorithms["EA"]),
        prepare_box_data(algorithms["TS"]),
        prepare_box_data(algorithms["SA"])
    ]
    # Create the boxplot
    ax.bxp(box_data, showmeans=False)
    ax.axhline(algorithms["Optimal"], color='red', linestyle='--', label="Optimal Value")
    ax.axhline(algorithms["Greedy"], color='blue', linestyle='--', label="Greedy")
    ax.set_title(instance)
    ax.set_xticklabels(["EA", "TS", "SA"])
    ax.legend()

# Adjust layout
plt.tight_layout()
fig.delaxes(axes[-1])  # Remove the extra subplot (since we have 7 instances, not 9)
# fig.delaxes(axes[-2])
plt.suptitle('Comparison of Algorithms Across Instances', fontsize=16, y=1.05)
fig.text(0.5, 0.0, 'Algorithms', ha='center', fontsize=12)
fig.text(0.0, 0.5, 'Fitness Values', va='center', rotation='vertical', fontsize=12)

# Save and display the plot
plt.savefig('comparison_box_plots.png')
plt.show()
