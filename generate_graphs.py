import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

if not os.path.exists('performance_graphs'):
    os.makedirs('performance_graphs')

# Load data from CSV
data = pd.read_csv('results.csv')

container_types = data['container_type'].unique()
index = np.arange(len(container_types))
bar_width = 0.5  # Width of the bars

for metric, label in zip(['avg_latency', 'requests_sec', 'transfer_sec'], 
                         ['Average Latency (ms)', 'Requests/sec', 'Transfer/sec (MB)']):
    
    plt.figure(figsize=(10, 6))
    
    metric_values = [data[data['container_type'] == container][metric].values[0] for container in container_types]
    plt.bar(index, metric_values, bar_width, label=container_types, alpha=0.8)

    plt.title(f'{label}')
    plt.xlabel('Container Type')
    plt.ylabel(label)
    
    # Adjust the xticks
    plt.xticks(index, container_types)  
    
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Save the figure
    plt.savefig(f'performance_graphs/{metric}.png')

plt.show()
