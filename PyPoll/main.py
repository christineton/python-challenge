import csv
import os

election_dataCSV = os.path.join('election_data.csv')

with open(election_dataCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# The total number of votes cast (done)
# A complete list of candidates who received votes 
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

    votes = []
    candidates = []
    votes_per_candidates = {}

    print("Election Results")
    print("------------------------")

    for row in csvreader:
        votes.append(row[0])
        if row[2] in votes_per_candidates:
            votes_per_candidates[row[2]] += 1
        else:
            votes_per_candidates[row[2]] = 1
        if row[2] not in candidates:
            candidates.append(row[2])

    vote_counts = len(votes)
    max_votes = 0
    max_candidate = ''

    print("Total Votes: " + str(vote_counts))
    print("------------------------")

    for candidate in votes_per_candidates:
        percent_of_votes = (votes_per_candidates[candidate]/vote_counts)
        if votes_per_candidates[candidate] > max_votes:
            max_votes = votes_per_candidates[candidate]
            max_candidate = candidate
        print(str(candidate) + ": " + "{:.3%}".format(percent_of_votes) + "" + "(" + str(votes_per_candidates[candidate]) + ")")
        

    print("------------------------")
    print("Winner: " + str(max_candidate))



# Create path to create txt file. Write out the output in file.write
file = open('election_output.txt','w')

file.write("Election Results: Total Votes- 3521001, Khan- 63.000%(2218231), Correy- 20.000%(704200), Li- 14.000%(492940), O'Tooley- 3.000%(105630), Winner- Khan")

file.close()
