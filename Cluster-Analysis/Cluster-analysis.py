import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import OPTICS
import matplotlib.pyplot as plt

# MIN_SAMPLES parameter in the OPTICS (Ordering Points To Identify the Clustering Structure) 
# algorithm specifies the minimum number of samples (data points) required for a cluster to be formed. 
# It determines the density threshold for forming clusters.
min_samples = 30
max_eps=1.0
threshold = min_samples * 1.5

# Define the directory paths for the files
angle_directory = os.path.join(os.getcwd(), "Combined-Angle")
velo_directory = os.path.join(os.getcwd(), "Combined-Velo")

# Get all the files in the angle directory
angle_files = os.listdir(angle_directory)

# Iterate over the files
for angle_file in angle_files:
    # Extract the base filename without extension
    filename = os.path.splitext(angle_file)[0]
 
    # Construct the corresponding velo filename
    velo_filename = f"{filename}_vel.txt"
    
    # Check if the velo file exists
    if velo_filename in os.listdir(velo_directory):
        # Read values from file 1 (angle file)
        with open(os.path.join(angle_directory, angle_file), 'r') as file1:
            lines = file1.readlines()
            X1 = [float(line.strip().split()[1]) for line in lines]
    
        # Read values from file 2 (velo file)
        with open(os.path.join(velo_directory, velo_filename), 'r') as file2:
            lines = file2.readlines()
            X2 = [float(line.strip().split()[1]) for line in lines]
    
        # Combine the two datasets
        X = np.column_stack((X1, X2))
    
        # Perform standard scaling on the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    
        # Perform OPTICS clustering
        clusterer = OPTICS(min_samples=min_samples, max_eps=max_eps)
        clusterer.fit(X_scaled)
        labels = clusterer.labels_
    
        # Get the number of clusters
        unique_labels, counts = np.unique(labels, return_counts=True)
        num_clusters = len(set(labels))
   
    if num_clusters > 1:
        filtered_labels = []
        filtered_counts = []
        for label, count in zip(unique_labels, counts):
            if count > threshold:
                filtered_labels.append(label)
                filtered_counts.append(count)

        if len(filtered_labels) > 1:
            print(f"Number of clusters for pair {filename}: {len(filtered_labels)}")
            
            for label, count in zip(filtered_labels, filtered_counts):
                if count > threshold:
                    print(f"Cluster {label+1}: {count} points")

            # Create a new figure and axes for each graph
            fig, ax = plt.subplots()

            # Create a scatter plot of the data points colored by cluster labels
            ax.scatter(X2, X1, c=labels)
            ax.set_title(f"Clusters for {filename}")
            ax.set_xlabel("Velocity")
            ax.set_ylabel("Torsion Angle")
            plt.savefig(f"{filename}_clusters.png",dpi=600)
            plt.close(fig)  # Close the figure to prevent overlapping
