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
PyPoll_csv = os.path.join("PyPoll_Resources", "election_data.csv")

"""Open the csv file, then read it - 
##'with open as' will open AND close the file for you
##first line - opens the csv, we're wanting to read it as csv_file variable 
##next indented line - initalize csv.reader (csv module, reader function) which
##reads the csv_file and establishes the delimiter, 
##which sets up the list of lists,
##and stores the csv contents in the csv_reader variable
##"""

#Set up variables assigned to lists to store data to write to txt file later
votes = []
results = {}

#Open and read csv
with open(PyPoll_csv,"r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Skip header row
    csv_header = next(csv_reader)
    
    #Gather voter IDs & profits & losses data
    for row in csv_reader:
        votes.append(row[0])
        ##PL.append(int(row[1]))
        #Get the unique candidates as the keys in the dictionary
        #Build the dictionary
        #If this dictionary key exists, add 1 to that key's the value, 
        #count the votes every time that candidate exists
        if results.get(row[2]):
            results[row[2]] += 1
        else:
        #If this is the first time OR they only show up once in the data, 
        #count that vote once
            results[row[2]] = 1

    #Count all the votes    
    total_votes = len(votes)
    #Provide all values in the dictionary, into a list
    all_results = results.values()
    #Find the max value in the dictionary
    max_result = max(all_results)

    #Create the first print statement (outside of loop)
    first_print = f"""\nElection Results
-----------------------
Total Votes: {total_votes}
-----------------------"""
    print(first_print)

    #Now that the dictionary is built, iterate over it to get percent and winner
    #Set up second print variable (to add a string to it)
    second_print = ""
    for candidate,count in results.items():
        #First get percent
        vote_percent = (count/total_votes)
        #Format the percent to three decimal points
        formatted_vote_percent = "{:.3%}".format(vote_percent)
        #Store the winner as a variable (find the key) based on max value
        if count == max_result:
            winner = candidate
        #add the second print strings within the loop to the string we set up    
        second_print += f"\n{candidate}: {formatted_vote_percent} ({count})"
    print(second_print)
    
    #Set up the third print statement outside of loop
    third_print = f"""\n-----------------------
Winner: {winner}
-----------------------"""
    print(third_print)

#~~~ Write the analysis a text file ~~~

#Assign a variable to store the path to write to the new text file
output_text_file = os.path.join("PyPoll_Analysis", "Py_Poll_Analysis.txt")
print_all = first_print + second_print + third_print
#Open the file in write mode as a variable to store the contents
with open(output_text_file, "w") as text_file:
    text_file.writelines(print_all)