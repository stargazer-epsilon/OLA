import pandas as pd
import os

# File name stored in variable
input_file_name = "Export_68415514AE688183BDA813BABC41AD54B0E15995.csv"

# Construct the path to the Downloads directory for Windows
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", input_file_name)

# Read in the CSV file to a dataframe
df = pd.read_csv(downloads_path)

# Remove any records that don't have "Yes" under the column 'OLAPermissionShareResume'
df = df.loc[df['OLAPermissionShareResume'] == 'Yes']

# Create two new columns to extract the text to the right of the character "|" from the columns ResumePDF and ResumeWord
df['ResumePDF_Right'] = df['ResumePDF'].str.split("|").str[1]
df['ResumeWord_Right'] = df['ResumeWord'].str.split("|").str[1]

# Keep only the specific columns
df = df[['ProspectClassification', 'ResumePDF_Right', 'ResumeWord_Right', 'Email_Address', 'First_Name', 'Last_Name']]

# Create a new dataframe for each category of 'ProspectClassification'
dfs = {}
for classification in df['ProspectClassification'].unique():
    dfs[classification] = df[df['ProspectClassification'] == classification]

# To access a dataframe, you can use its corresponding 'ProspectClassification' value as the key
# For example, to access the dataframe for the classification 'Category1', you would use:
# print(dfs['Category1'])
