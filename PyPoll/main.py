# Import Modules
# Give path to collct the data file from resource folder
# Read data file with csv.reader
# Create dictionary to store and count the number of votes for each candidate. Key:candidate, value:votes
# Give counter to track total number of votes cast
# Find winner based on heighest number of votes
# Set output path for analysis result text file
# write results in text files using textfile.writer

#modules
import os
import csv

#path to collect the data from the Resource folder
election_data_csv = os.path.join("Resources", "election_data.csv")

#create dictionary to hold data for individual Candidate
candidate_votes = {}

#counter to keep track of the total number of votes cast
Total_votes = 0

# Read in the csv file
with open (election_data_csv, 'r') as csvfile :
    csvReader = csv.reader(csvfile)
    header = next(csvReader)

    #Loop through all rows in the CSV file to collect data
    for row in csvReader:
        Total_votes += 1
        selected_candidate = row[2]

        if selected_candidate in candidate_votes:
            candidate_votes[selected_candidate] += 1
        else:
            candidate_votes[selected_candidate] =1
    
    #Find the wiiner based on maximum votes
    winner = max(candidate_votes , key=candidate_votes.get)

    #Set output of the text file
    output_path = os.path.join("analysis","Election_Outcome.txt")

    #write result analysis in text file
    with open(output_path, 'w') as textfile:

        textfile.write("Election Results\n")
        textfile.write("-------------------------\n")
        textfile.write(f'Total Votes: {Total_votes}\n')
        textfile.write("-------------------------\n")
        for selected_candidate, votes in candidate_votes.items():
            pct_vote = (votes / Total_votes)*100
            textfile.write(f'{selected_candidate} : {pct_vote:.3f}% ({votes})\n')
        textfile.write("-------------------------\n")
        textfile.write(f'Winner : {winner}\n')
        textfile.write("-------------------------\n")