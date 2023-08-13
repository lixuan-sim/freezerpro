# Purpose of freezerpro_2.py
Automation of file downloading and compilation for audits. The current process of completing FreezerPro audits is manual and involves collating massive Excel files (> 30 000 samples), taking up time and introduce space for mistakes. I have written this script to automate these processes:

- compile all .csv files with samples that have been downloaded from FreezerPro website;
- delete unwanted data: xTrash, DNA;
- generate an Excel with 10 random samples.


# Workflow
## Before starting
- Download and install latest version of python
- Run terminal as administrator
- Run these commands to install libraries:
```
pip install pandas
pip install wheel
```
## To run script
- Save 'python_2.py', noting file directory
- Change the following variable in python_2.py to working directory containing FreezerPro Sample Report files:<br>

**downloaded_FP_sample_report_directory**<br>

- Navigate to file directory in terminal
- Run script with this command:
```
python freezerpro_2.py
```

## Output
- Excel of all live samples as 'Month-Year_all_FreezerPro_samples_combined.csv'
- Excel of 10 randomly generated samples as 'Month_Year_generated_audit_samples.csv'

# To do:

- user testing (with and without previous Python experience)
- figure out how to pull .csv data from FreezerPro into a file on Drive automatically
