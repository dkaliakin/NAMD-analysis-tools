import os
import numpy as np
import matplotlib.pyplot as plt

# Define the directory paths for the files
velo_directory = os.path.join(os.getcwd(), "Avg-Velo")

# Get all the files in the velo directory
velo_files = os.listdir(velo_directory)

# Coordinate of choice
sel_velo = input("Enter the name of coordinate: ")
choice_file = f"avg.{sel_velo}_vel.dat.fhlf.csv"

# Remove the extension from the coordinate name
coord_name = sel_velo.split('.')[0]

# Time range of choice
start_index = int(input("Enter the starting index of the range: "))
end_index = int(input("Enter the ending index of the range: "))

# Choice of number of top results
top_number = int(input("Enter desired number of top results: "))

# Load the data for selected coordinate
with open(os.path.join(velo_directory, choice_file), 'r') as file2:
    lines = file2.readlines()
    x1 = [float(line.strip().split()[1]) for line in lines]
    x1 = np.array(x1)

# Initialize variables to track the smallest values
smallest_rmsd = [float('inf')] * top_number
smallest_rmsd_inv = [float('inf')] * top_number
best_rmsd_files = [None] * top_number
best_rmsd_inv_files = [None] * top_number

# Iterate over the files
for velo_file in velo_files:
    if velo_file != choice_file:
        # Read values from file 1 (velo file)
        with open(os.path.join(velo_directory, velo_file), 'r') as file1:
            lines = file1.readlines()
            x2 = [float(line.strip().split()[1]) for line in lines]
            x2 = np.array(x2)

            # Calculate RMSD and inverted RMSD only for the selected range
            rmsd = np.sqrt(np.mean((x2[start_index:end_index] - x1[start_index:end_index])**2))
            rmsd_inv = np.sqrt(np.mean((-x2[start_index:end_index] - x1[start_index:end_index])**2))

            # Update smallest values and file names
            for i in range(top_number):
                if rmsd < smallest_rmsd[i]:
                    smallest_rmsd.insert(i, rmsd)
                    smallest_rmsd.pop()
                    best_rmsd_files.insert(i, velo_file)
                    best_rmsd_files.pop()
                    break

                if rmsd_inv < smallest_rmsd_inv[i]:
                    smallest_rmsd_inv.insert(i, rmsd_inv)
                    smallest_rmsd_inv.pop()
                    best_rmsd_inv_files.insert(i, velo_file)
                    best_rmsd_inv_files.pop()
                    break

# Print the results for three smallest values
for i in range(top_number):
    if best_rmsd_files[i] is not None:
        print(f"Smallest RMSD {i + 1}: {smallest_rmsd[i]} ({best_rmsd_files[i].replace('.dat.fhlf.csv', '')})")

    if best_rmsd_inv_files[i] is not None:
        print(f"Smallest inverted RMSD {i + 1}: {smallest_rmsd_inv[i]} ({best_rmsd_inv_files[i].replace('.dat.fhlf.csv', '')})")
