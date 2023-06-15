# install Python
# run cmd as admin - pip install wheel
# run cmd as admin - pip install pandas

#import modules

import glob
import pandas as pd
import os
import datetime

# CHANGE DIRECTORY TO FILEPATH WITH DOWNLOADED FREEZERPRO SAMPLE REPORT CSV
downloaded_FP_sample_report_directory = r'\\Breakthrough\breakthrough\Shared\- MOLECULAR ONCOLOGY LAB\FUNCTIONAL\Li Xuan\freezerpro\downloaded\test'

def get_columns(columns):
    # Define a list of columns to be placed at the top of the final list
    my_columns = ['UID', 'NAME', 'SAMPLE TYPE', 'DATE SAMPLE TAKEN', 'FREEZER', 'LEVEL1', 'LEVEL2', 'BOX', 'POSITION']
    # Loop through the list of columns to be placed at the top in reverse order
    # needs to be reverse as it removes column and puts on top of the list, from first to last. 
    # e.g. list = 1, 2, 3, 4     output = 4, 3, 2, 1 (not reversed)     output = 1, 2, 3, 4 (reversed)
    for column in my_columns[::-1]:
        # Check if the current column is in the list of columns passed to the function
        if column in columns:
            # Remove the current column from its current position in the list
            columns.remove(column)
            # Insert the current column at the beginning of the list
            columns.insert(0, column)
            
    # Return the final list of columns
    return columns


# set work directory to where Excel files are downloaded
# use backslash for directory to ensure it reads, do not just copy & paste
# or use r'directory'

os.chdir(downloaded_FP_sample_report_directory)

# Use glob to match the regular expression 'csv'
extension = 'csv'
all_files = [i for i in glob.glob('*.{}'.format(extension))]

# list all files
li = []

# read csv into dataframe
# df = pd.read_csv()
for filename in all_files:
    df = pd.read_csv(filename, low_memory=False, index_col=None, header=0)
    df.columns = df.columns.str.upper()
    li.append(df)


# join all the DataFrames and then drop empty columns
result_frame = pd.concat(li, ignore_index=True).dropna(axis=1, how='all')


# eliminate data that has been trashed 'xTrash Bag' in column 'FREEZER' (uppercase due to line 46)
# delete "SAMPLES" string contains DNA
filtered_rf = result_frame[~result_frame.FREEZER.str.contains("xTrash")]
filtered_rf = filtered_rf[~filtered_rf["SAMPLE TYPE"].str.contains("DNA")]

# reorder columns to desired order with function get_columns
ordered_fr = filtered_rf[get_columns(filtered_rf.columns.tolist())]


# export the result to a csv file named "all_freezer_samples_combined"
date_today = datetime.datetime.today().strftime('%Y-%b')

ordered_fr.to_csv(date_today + '_all_FreezerPro_samples.csv', index=None)

all_samples_file = pd.read_csv(date_today + '_all_FreezerPro_samples.csv', low_memory=False, index_col=None, header=0)
audit_samples = all_samples_file.sample(10)

audit_samples.to_csv(date_today + '_generated_audit_samples.csv', index = None)



# to run script: 
# 1. Change work directory of this python script to where downloaded FreezerPro Excel files are stored. 
# 2. Open cmd. 
# 2. Set cmd directory to where this Python script is stored. 
# 3. Run "python freezerpro_2.py"