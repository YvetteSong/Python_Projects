
import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files

#file path
csvpath = os.path.join('Resources', 'election_data.csv')

# initiallize the variables
total_votes = 0
total_votes_won = {}
percentage = 0
winner_count = 0
candidate_list = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile) # csv.reader object - read the CSV file line by line.
    header = next(csvreader) # skip the header row
    
    for row in csvreader:
        # The total number of votes cast: count the amount of rows
        total_votes += 1
        candidate = row[2]
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2]) #create a list of candidates who received votes
            total_votes_won[row[2]] = 0
    
        total_votes_won[row[2]] += 1
        percentage = (total_votes_won[row[2]] / total_votes) * 100

# print out the result
print("Election Results\n")
print("--------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("--------------------------\n")

for candidate in total_votes_won:
    percentage = (total_votes_won[candidate] / total_votes) * 100
    if total_votes_won[candidate] >  winner_count:
        # Determine winning vote count and candidate
        winner_count = total_votes_won[candidate]
        winning_candidate = candidate
    
    print(f"{candidate}: {percentage:.3f}% ({total_votes_won[candidate]})\n")

print("--------------------------\n")
print(f"Winner: {winning_candidate}\n")
print("--------------------------")

# Print each candidate's voter count and percentage (to terminal)

# write a text file
textpath = os.path.join('analysis', 'election_data.txt')
with open(textpath, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("--------------------------\n")
    textfile.write(f"{candidate_list[0]}: {percentage:.3f}% ({total_votes_won[candidate_list[0]]})\n")
    textfile.write(f"{candidate_list[1]}: {percentage:.3f}% ({total_votes_won[candidate_list[1]]})\n")
    textfile.write(f"{candidate_list[2]}: {percentage:.3f}% ({total_votes_won[candidate_list[2]]})\n")


#    textfile.write(f"{candidate}: {percentage:.3f}% ({total_votes_won[candidate]})\n")
#    textfile.write(f"{candidate}: {percentage:.3f}% ({total_votes_won[candidate]})\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Winner: {winning_candidate}\n")
    textfile.write("--------------------------")
   
  



