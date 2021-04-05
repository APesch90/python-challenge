#Import the os and csv modules to be able to use them
#os will allow us to create file paths across operating systems
import os
import csv

#Set directory to read files
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
os.chdir(dir_path)

#~~~ Reading the budget_data.csv file and analyzing ~~~
#Assign a varaible to store source csv file pathway with os.path.join function
PyBank_csv = os.path.join("PyBank_Resources", "budget_data.csv")

"""Open the csv file, then read it - 
'with open as' will open AND close the file for you
first line - opens the csv, we're wanting to read it as csv_file variable 
next indented line - initalize csv.reader (csv module, reader function) which
reads the csv_file and establishes the delimiter, 
which sets up the list of lists,
and stores the csv contents in the csv_reader variable
"""

#Set up variables assigned to lists to store data to write to txt file later
months = []
PL = []
change_PL = []

#Open and read csv
with open(PyBank_csv,"r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Skip header row
    csv_header = next(csv_reader)
    
    #Gather months & profits & losses data
    for row in csv_reader:
        months.append(row[0])
        PL.append(int(row[1]))
   
    #individual row changes, avg change P&L, max change and min change with months
    for i in range(1,len(PL)):
        change_PL.append(PL[i] - PL[i-1])

    avg_change_PL = sum(change_PL)/len(change_PL)
    max_change_PL = max(change_PL)
    """compare two lists (months and change_PL, find the index in the months 
    list, that aligns with the index that represents the max change value, 
    then add 1 because the first change will be non-existent"""
    max_change_PL_months = str(months[change_PL.index(max_change_PL) +1])
    min_change_PL = min(change_PL)
    min_change_PL_months = str(months[change_PL.index(min_change_PL) +1])

#~~~ Print the analysis in terminal ~~~
    #Assign a variable to represent a list of strings
    
    text_output = f"""\nFinancial Analysis
-------------------
Total Months: {len(months)}
Total: ${sum(PL)}
Average Change: ${round(avg_change_PL,2)}
Greatest Increase in Profits: {max_change_PL_months} (${max_change_PL})   
Greatest Decrease in Profits: {min_change_PL_months} (${min_change_PL})"""

print(text_output)

#~~~ Write the analysis a text file ~~~

#Assign a variable to store the path to write to the new text file
output_text_file = os.path.join("PyBank_Analysis", "Py_Bank_Analysis.txt")

#Open the file in write mode as a variable to store the contents
with open(output_text_file, "w") as text_file:
    text_file.writelines(text_output)