import matplotlib.pyplot as plt
import pandas as pd
import os

if not os.path.exists('performance_graphs'):
    os.makedirs('performance_graphs')

# Assuming you have a CSV with the data. Format:
# core_count, container_type, avg_latency, requests_sec, transfer_sec
data = pd.read_csv('results.csv')

container_types = data['container_type'].unique()

for metric, label in zip(['avg_latency', 'requests_sec', 'transfer_sec'], 
                         ['Average Latency (ms)', 'Requests/sec', 'Transfer/sec (MB)']):
    plt.figure(figsize=(10, 6))

    for container in container_types:
        subset = data[data['container_type'] == container]
        plt.plot(subset['core_count'], subset[metric], label=container, marker='o')

    plt.title(f'{label} by Number of Cores')
    plt.xlabel('Number of Cores')
    plt.ylabel(label)
    plt.xticks(data['core_count'].unique())
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the figure
    plt.savefig(f'performance_graphs/{metric}.png')

plt.show()
