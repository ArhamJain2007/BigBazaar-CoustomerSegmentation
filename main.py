
import subprocess
import sys
import os

print("\n====================================")
print(" BIG BAZAAR CUSTOMER SEGMENTATION")
print("====================================")

# Create output folders if they do not exist
os.makedirs("Data", exist_ok=True)
os.makedirs("Models", exist_ok=True)
os.makedirs("Output/Graphs", exist_ok=True)

# List of project files to run
project_files = [
    "Src/data_loader.py",
    "Src/preprocessing.py",
    "Src/visualization.py",
    "Src/clustering.py",
    "Src/cluster_analysis.py"
]

# Run each file one by one
for file in project_files:

    print("\n------------------------------------")
    print("Running:", file)
    print("------------------------------------")

    result = subprocess.run(
        [sys.executable, file],
        cwd=os.getcwd()
    )

    if result.returncode != 0:
        print("\nError while running:", file)
        print("Please check the error and try again.")
        sys.exit(1)

print("\n====================================")
print(" PROJECT PIPELINE COMPLETED!")
print("====================================")

print("\nYou can now start the dashboard using:")
print("streamlit run app.py")
