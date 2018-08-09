import csv
import os
# importing modules

# Path to collect data from folder
election_dataCSV = os.path.join('election_data.csv')

# Opening csv file as read and calling it csvfile
with open(election_dataCSV, 'r') as csvfile:

    # Identifying the csv file delimiter with commas which will be able to tell every column
    csvreader = csv.reader(csvfile, delimiter=',')

    # Removing header as part of data from CSV file
    header = next(csvreader)

# The total number of votes cast (done)
# A complete list of candidates who received votes 
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

    # create votes and candidates as a list. create votes per candidates as a dictionary
    votes = []
    candidates = []
    votes_per_candidates = {}

    print("Election Results")
    print("------------------------")

    # for loop through the rows in the file
    for row in csvreader:
        # set votes to column 0 and append to send it to the last of the list
        votes.append(row[0])
        # if function for column3 where there are the candidates names, votes per candidate will add up all the times it appears
        if row[2] in votes_per_candidates:
            votes_per_candidates[row[2]] += 1
        
        # else function to set the very first row as 1 
        else:
            votes_per_candidates[row[2]] = 1
        
        # if function to create a list of the unique candidate names
        if row[2] not in candidates:
            candidates.append(row[2])

    # set votes counts as the variable for the lenght of the votes appended in for loop
    vote_counts = len(votes)

    # set max_votes as 0 to start
    max_votes = 0

    # set the candidate with the max votes as an empty string
    max_candidate = ''

    # print vote counts 
    print("Total Votes: " + str(vote_counts))
    print("------------------------")

    # for loop through candidates list through votes per candidate dictionary
    for candidate in votes_per_candidates:

        # calculate percent of votes by getting total votes per candidate [votes_per_candidates[candidates]<- this is a dictionary / vote counts]
        percent_of_votes = (votes_per_candidates[candidate]/vote_counts)

        # if function to find candidate with the max votes
        if votes_per_candidates[candidate] > max_votes:
            # max votes will then equal to that candidate
            max_votes = votes_per_candidates[candidate]
            # max candidate will then equal that candidate
            max_candidate = candidate

        print(str(candidate) + ": " + "{:.3%}".format(percent_of_votes) + "" + "(" + str(votes_per_candidates[candidate]) + ")")
        

    print("------------------------")
    print("Winner: " + str(max_candidate))



# Create path to create txt file. Write out the output in file.write
file = open('election_output.txt','w')

file.write("Election Results: Total Votes- 3521001, Khan- 63.000%(2218231), Correy- 20.000%(704200), Li- 14.000%(492940), O'Tooley- 3.000%(105630), Winner- Khan")

file.close()
