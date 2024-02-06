import os

# Specify the path to the directory containing your CSV files
directory_path = '.'

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        # Construct the full path to the file
        file_path = os.path.join(directory_path, filename)
        # Open the file in write mode and overwrite it with an empty string
        with open(file_path, 'w') as file:
            pass  # Opening in 'w' mode and closing will empty the file

print("All CSV files have been emptied.")
