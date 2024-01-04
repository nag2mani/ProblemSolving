import os
from datetime import datetime, timedelta

# folder_name = "POTD"
# os.makedirs(folder_name, exist_ok=True)

# Set the start date
start_date = datetime(2024, 1, 2)

# Create 30 files
for i in range(30):
    current_date = start_date + timedelta(days=i)
    file_name = current_date.strftime("%d_%b_%Y.py")
    # file_path = os.path.join(folder_name, file_name)

    # with open(file_path, "w") as file:
    with open(file_name, "w") as file:
        file.write("# Your Python code here")

print("Files created successfully in the 'POTD' folder.")
