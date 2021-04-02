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

date = []
PL = []
total_months = []
net_PL = []
change_PL = []
avg_change_PL = []
max_change_PL = []
max_change_PL_date = []
min_change_PL = []
min_change_PL_date = []

with open(PyBank_csv,"r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        date.append(row[0])
        PL.append(int(row[1]))
    #~~~ Start the calculations needed to write to the txt file later! ~~~
    #Calculate the total number of months included in the dataset 
    #Count rows in the csv
    #skip headers (since there are headers present)
    """STEP 2 - Calculate the net total amount of "Profit/Losses" over the 
    entire period
    """
    
    #total # months
    for row in csv_reader:
        total_months.append(row[0])
        net_PL.append(int(row[1]))

    #individual row changes, avg change P&L, max change and min change with dates
    for i in range(1,len(PL)):
        change_PL.append(PL[i] - PL[i-1])
        avg_change_PL.append = sum(change_PL)/len(change_PL)
        max_change_PL.append = max(change_PL)
        max_change_PL_date.append = str(date[change_PL.index(max_change_PL)])
        min_change_PL.append = min(change_PL)
        min_change_PL_date.append = str(date[change_PL.index(min_change_PL)])

  
    #~~~ Print the analysis in terminal ~~~
    #print(f"""
    #Financial Analysis
    #---------------------------------
    #print("Total Months: " len(total_months))
    #print("Total: " sum(net_PL))
    #print("Average Change: " "$"avg_change_PL)
    #print("Greatest Increase in Profits: " max_change_PL_date "$"(max_change_PL))    
    #print("Greatest Increase in Profits: " min_change_PL_date "$"(min_change_PL))   
    #""")

#~~~ Write the analysis a text file ~~~

#Assign a variable to store the zip of the lists
Py_Bank_zip = zip(total_months, net_PL, change_PL, avg_change_PL, max_change_PL, max_change_PL_date, min_change_PL_date)

#Assign a variable to store the path to write to the new text file
output_text_file = os.path.join("PyBank_Analysis", "Py_Bank_Analysis.txt")

#Open the file in write mode as a variable to store the contents
with open(output_text_file, "w") as text_file:
    #Initialize the txt.writer (csv module, writer function)
    txt_writer = txt.writer(text_file)
    #Write in headers in the first column (writerow for list of strings)
    writer.writerow("")
    #Write in zipped rows (writerows for a list of lists)
    writer.writerows(Py_Bank_zip)
