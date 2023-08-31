import os
import numpy as np
import matplotlib.pyplot as plt

# Define the directory paths for the files
velo_directory = os.path.join(os.getcwd(), "Separate-Velo")
angle_directory = os.path.join(os.getcwd(), "Separate-Angle")

# Prompt for partial names
print("The name of desired coordinate")
coordinate=input("enter here:")
partial_name_1 = f"{coordinate}_vel-reacthop"
partial_name_2 = f"{coordinate}-reacthop"
partial_name_3 = f"{coordinate}_vel-unreacthop" 
partial_name_4 = f"{coordinate}-unreacthop"
coord_name = coordinate

# Function to find the full file name based on the partial name
def find_file(directory, partial_name):
    matching_files = [file for file in os.listdir(directory) if partial_name in file]
    if matching_files:
        return matching_files[0]
    else:
        return None

# Find the full file names for the red dot set
velo_filename_1 = find_file(velo_directory, partial_name_1)
angle_filename_1 = find_file(angle_directory, partial_name_2)

# Find the full file names for the blue dot set
velo_filename_2 = find_file(velo_directory, partial_name_3)
angle_filename_2 = find_file(angle_directory, partial_name_4)

# Check if the files exist
if velo_filename_1 and angle_filename_1 and velo_filename_2 and angle_filename_2:
    # Read values from the first Separate-Velo file (second column)
    with open(os.path.join(velo_directory, velo_filename_1), 'r') as velo_file_1:
        lines = velo_file_1.readlines()
        velo_values_1 = [float(line.strip().split()[1]) for line in lines]

    # Read values from the first Separate-Angle file (second column)
    with open(os.path.join(angle_directory, angle_filename_1), 'r') as angle_file_1:
        lines = angle_file_1.readlines()
        angle_values_1 = [float(line.strip().split()[1]) for line in lines]

    # Read values from the second Separate-Velo file (second column)
    with open(os.path.join(velo_directory, velo_filename_2), 'r') as velo_file_2:
        lines = velo_file_2.readlines()
        velo_values_2 = [float(line.strip().split()[1]) for line in lines]

    # Read values from the second Separate-Angle file (second column)
    with open(os.path.join(angle_directory, angle_filename_2), 'r') as angle_file_2:
        lines = angle_file_2.readlines()
        angle_values_2 = [float(line.strip().split()[1]) for line in lines]

    # Create a scatter plot of the values
    plt.scatter(velo_values_1, angle_values_1, c='red', label='Productive')
    plt.scatter(velo_values_2, angle_values_2, c='blue', label='Unproductive')
    plt.title(coord_name)
    plt.xlabel("Velocity")
    plt.ylabel("Torsion Angle")
    plt.legend()
    plt.savefig(f"Actual_{coord_name}.png",dpi=600)
else:
    print("Files not found in the specified directories.")
