!/usr/bin/env python3
import pandas as pd
import re
import argparse

# Empty lists to hold the extracted and calculated data
deployments = []
sizes = []
units = []
gib_values = []

file_name = 'my_b_l.txt'
# Function to convert the sizes to GiB
def convert_to_gib(size, unit):
    if unit == "KiB":
        return float(size) / (1024**2)
    elif unit == "MiB":
        return float(size) / 1024
    elif unit == "GiB":
        return float(size)
    elif unit == "TiB":
        return float(size)*1024

    else:
        return None  # handle other units as needed

parser = argparse.ArgumentParser(description='Process data and display in desired size unit.')
parser.add_argument('unit', choices=['GiB', 'TiB'], help='The target unit for display (GiB or TiB).')
args = parser.parse_args()
# Read the file and extract the data
with open(file_name, 'r') as file:
    for line in file:
        # Using regex to extract deployment name, size, and unit
        match = re.match(r'(.+)\s+Total Size: ([\d.]+) (\w+)', line)
        if match:
            deployment, size, unit = match.groups()
            deployments.append(deployment)
            sizes.append(float(size))
            units.append(unit)
            gib_values.append(convert_to_gib(size, unit))

# Create the DataFrame
df = pd.DataFrame({
    'Deployment': deployments,
    'Size': sizes,
    'Unit': units,
    'Size_in_GiB': gib_values
})

# Display the DataFrame
print(df)
print(df.Size_in_GiB.sum())
if args.unit:
    df = df[df.Unit==args.unit]
    print(df)
    print(df.Size_in_GiB.sum())
