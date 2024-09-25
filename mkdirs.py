import os

# Set the directory where you want to create the folders
#directory = "ACCTG521_Labs"  
directory = "ACCTG522_Labs"  
# Ensure the directory exists
if not os.path.exists(directory):
    print(f"The directory {directory} does not exist.")
else:
    # Create 20 folders named Class01, Class02, ..., Class20
    for i in range(1, 21):
        folder_name = f"Class{i:02d}"  # Formatting to ensure two-digit numbering (e.g., Class01, Class02, ...)
        folder_path = os.path.join(directory, folder_name)

        # Check if the folder already exists before creating it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")
        else:
            print(f"Folder {folder_name} already exists.")
