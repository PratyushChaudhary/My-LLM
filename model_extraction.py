# This file gets you the contents of specific columns of the csv file into an output file

import pandas as pd

# Load the CSV file from a specific path
csv_file = '~/Desktop/GPT_FROM_SCRATCH/BBC_DATASET.csv'
df = pd.read_csv(csv_file)

# Assume the text is in a column named 'text'
title = df['title']
description = df['description']

# Save the text data to a plain text file
with open('title.txt', 'w') as file:
    for line in title:
        file.write(f"{line}\n")

with open('description.txt', 'w') as file:
    for line in description:
        file.write(f"{line}\n")