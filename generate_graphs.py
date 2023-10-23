import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

if not os.path.exists('performance_graphs'):
    os.makedirs('performance_graphs')

# Assuming you have a CSV with the data. Format:
# core_count, container_type, avg_latency, requests_sec, transfer_sec
data = pd.read_csv('results.csv')

container_types = data['container_type'].unique()
core_counts = data['core_count'].unique()
bar_width = 0.15  # Adjusted bar width for smaller bars
spacing = 0.1  # White space between each group of bars
index = np.arange(len(core_counts)) * (len(container_types) * bar_width + spacing)

num_containers = len(container_types)
middle_container = (num_containers - 1) / 2  # This finds the middle position of grouped bars

for metric, label in zip(['avg_latency', 'requests_sec', 'transfer_sec'], 
                         ['Average Latency (ms)', 'Requests/sec', 'Transfer/sec (MB)']):
    
    plt.figure(figsize=(10, 6))
    
    for i, container in enumerate(container_types):
        subset = data[data['container_type'] == container]
        plt.bar(index + i * bar_width, subset[metric], bar_width, label=container, alpha=0.8)

    plt.title(f'{label} by Number of CPU Cores')
    plt.xlabel('Number of CPU Cores')
    plt.ylabel(label)
    
    # Adjust the xticks to be centered
    plt.xticks(index + middle_container * bar_width, core_counts)  
    
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Save the figure
    plt.savefig(f'performance_graphs/{metric}.png')

plt.show()
