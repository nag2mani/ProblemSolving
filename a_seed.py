#----------- To make folder in current directory -------------

import os
from datetime import datetime, timedelta

start_date = datetime(2024, 1, 2)
for i in range(30):
    current_date = start_date + timedelta(days=i)
    file_name = current_date.strftime("%d_%b_%Y.py")

    with open(file_name, "w") as file:
        file.write("# Your Python code here")

print("Files created successfully in current folder.")



#----------- To make folder in current directory -------------

import os
folder_path = "C:/Users/nag2m/Desktop/Problem_Solving/kk"
os.makedirs(folder_path, exist_ok=True)

for i in range(1, 51):
    file_name = f"nag{i}.py"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write(" # Start your code")

print("Files created successfully in the folder.")