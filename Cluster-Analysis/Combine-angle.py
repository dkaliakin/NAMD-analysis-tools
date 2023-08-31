import os
import shutil

# Define the source directory path where the original files are located
source_directory = os.path.join(os.getcwd(), "Separate-Angle")

# Define the destination directory path where the combined files will be written
destination_directory = os.path.join(os.getcwd(), "Combined-Angle")

# Get all the files in the source directory
files = os.listdir(source_directory)

# Create a dictionary to store the pairs of files
file_pairs = {}

# Iterate over the files
for file in files:
    # Extract the base filename without extension
    filename = os.path.splitext(file)[0]

    # Determine the pair name and file type based on the filename
    if filename.endswith("-reacthopseries"):
        pair_name = filename[:-len("-reacthopseries")]
        file_type = "react"
    elif filename.endswith("-unreacthopseries"):
        pair_name = filename[:-len("-unreacthopseries")]
        file_type = "unreact"
    else:
        continue

    # Check if the pair already exists
    if pair_name in file_pairs:
        # Append the current file to the pair
        file_pairs[pair_name].append((file, file_type))
    else:
        # Create a new pair with the current file
        file_pairs[pair_name] = [(file, file_type)]

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Iterate over the file pairs
for pair_name, pair_files in file_pairs.items():
    # Check if the pair has both files
    if len(pair_files) == 2:
        # Sort the files in the pair based on file type
        pair_files.sort(key=lambda x: x[1])

        # Combine the file paths
        file1_path = os.path.join(source_directory, pair_files[0][0])
        file2_path = os.path.join(source_directory, pair_files[1][0])

        # Read the contents of the files
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_contents = file1.read()
            file2_contents = file2.read()

        # Combine the contents of the files
        combined_contents = file1_contents + file2_contents

        # Define the output file name
        output_filename = f"{pair_name}.txt"

        # Define the output file path
        output_filepath = os.path.join(destination_directory, output_filename)

        # Write the combined contents to the output file
        with open(output_filepath, 'w') as output_file:
            output_file.write(combined_contents)
