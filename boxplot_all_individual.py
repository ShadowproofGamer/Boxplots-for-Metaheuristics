import matplotlib.pyplot as plt

# Updated data with additional instances and methods (EAMI and EAMSA)
data = {
    "A-n32-k5": {
        "EA": [797, 833, 819, 14.74],
        "TS": [798, 829, 815, 14.17],
        "SA": [802, 829, 808, 10.56],
        "EAMI": [797, 797, 797, 0.00],
        "EAMSA": [797, 797, 797, 0.00],
        "Optimal": 784,
        "Greedy": 906
    },
    "A-n37-k6": {
        "EA": [951, 1010, 970, 18.01],
        "TS": [951, 986, 964, 10.22],
        "SA": [951, 970, 955, 6.16],
        "EAMI": [951, 951, 951, 0.00],
        "EAMSA": [951, 957, 952, 1.81],
        "Optimal": 949,
        "Greedy": 1063
    },
    "A-n39-k5": {
        "EA": [829, 843, 836, 4.12],
        "TS": [830, 878, 838, 14.27],
        "SA": [829, 837, 831, 2.55],
        "EAMI": [829, 829, 829, 0.00],
        "EAMSA": [830, 838, 833, 2.49],
        "Optimal": 822,
        "Greedy": 924
    },
    "A-n45-k6": {
        "EA": [962, 1015, 980, 14.54],
        "TS": [956, 982, 972, 10.09],
        "SA": [954, 981, 966, 10.41],
        "EAMI": [945, 945, 945, 0.00],
        "EAMSA": [945, 975, 959, 8.67],
        "Optimal": 944,
        "Greedy": 1122
    },
    "A-n48-k7": {
        "EA": [1074, 1250, 1113, 29.80],
        "TS": [1074, 1117, 1097, 16.70],
        "SA": [1074, 1127, 1102, 14.21],
        "EAMI": [1074, 1074, 1074, 0.00],
        "EAMSA": [1074, 1134, 1109, 17.09],
        "Optimal": 1073,
        "Greedy": 1260
    },
    "A-n54-k7": {
        "EA": [1175, 1250, 1207, 24.13],
        "TS": [1172, 1227, 1197, 18.78],
        "SA": [1173, 1229, 1195, 17.01],
        "EAMI": [1172, 1172, 1172, 0.00],
        "EAMSA": [1179, 1219, 1193, 13.58],
        "Optimal": 1167,
        "Greedy": 1385
    },
    "A-n60-k9": {
        "EA": [1368, 1499, 1442, 44.53],
        "TS": [1378, 1441, 1403, 21.38],
        "SA": [1364, 1413, 1391, 14.60],
        "EAMI": [1356, 1368, 1362, 3.30],
        "EAMSA": [1360,	1376,	1369,	5.64],
        "Optimal": 1354,
        "Greedy": 1548
    },
    "A-n80-k10": {
        "EA": [1860, 1964, 1908, 28.92],
        "TS": [1791, 1831, 1814, 17.43],
        "SA": [1802, 1838, 1822, 13.37],
        "EAMI": [1766, 1803, 1794, 10.53],
        "EAMSA": [1827, 1892, 1863, 17.02],
        "Optimal": 1763,
        "Greedy": 2045
    }
}


# Prepare boxplot data
def prepare_box_data(stats):
    min_val, max_val, avg, stddev = stats
    q1 = avg - stddev  # Q1 (1st Quartile)
    q3 = avg + stddev  # Q3 (3rd Quartile)
    return {
        'med': avg,  # Median is the average
        'q1': q1,  # Lower quartile (Q1)
        'q3': q3,  # Upper quartile (Q3)
        'whislo': min_val,  # Min value
        'whishi': max_val,  # Max value
        'fliers': []  # No outliers (fliers)
    }


# Create individual plots for each instance
for instance, algorithms in data.items():
    # Create figure
    fig, ax = plt.subplots(figsize=(7, 5))

    # Prepare boxplot data for EA, TS, SA, EAMI, EAMSA
    box_data = [
        prepare_box_data(algorithms["EA"]),
        prepare_box_data(algorithms["TS"]),
        prepare_box_data(algorithms["SA"]),
        prepare_box_data(algorithms["EAMI"]),
        prepare_box_data(algorithms["EAMSA"])
    ]

    # Create the boxplot
    ax.bxp(box_data, showmeans=False)

    # Add horizontal lines for Optimal and Greedy values
    ax.axhline(algorithms["Optimal"], color='red', linestyle='--', label="Optimal Value")
    ax.axhline(algorithms["Greedy"], color='blue', linestyle='--', label="Greedy")

    # Set title and labels
    ax.set_title(f'Comparison of Algorithms for {instance}')
    ax.set_xticklabels(["EA", "TS", "SA", "EAMI", "EAMSA"])
    ax.set_ylabel('Fitness')
    ax.legend()

    # Save the plot as an individual file
    plt.tight_layout()
    plt.savefig(f'{instance}_comparison_plot.png')
    plt.show()
