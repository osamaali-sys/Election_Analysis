
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

            #add a vote to candidate count
        candidate_votes[candidate_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

###
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    

    # Save the final vote count to the text file.
    txt_file.write(election_results)

###
# Print the candidate vote dictionary.
#print(candidate_votes)
# Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    txt_file.write(winning_candidate_summary)


#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

#Make a copy of the PyPoll.py file that you used throughout this module and rename it PyPoll_Challenge.py.
#done
#Create a list for the counties.
county = []
county_votes = 0
#Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
counties_dict = {}
counties_dict["county"] = 0
#Create an empty string that will hold the county name that had the largest turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

#Declare a variable that represents the number of votes that a county received. 
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        county_votes += 1 
        
        # Print the county name from each row.
        county_name = row[1]
             
# Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. If not, add it to the list of county names.
        if county_name not in county:
          # Add the county name to the county list.
            county.append(county_name)

           # 2. Begin tracking that counties vote count. 
            counties_dict[county_name] = 0

            #add a vote to counties count
        counties_dict[county_name] +=1



#Inside the with open() function where you are outputting the file, do the following:
with open(file_to_save, "w") as txt_file:
    
    voters_outcome = (
        f"\nLargest County Turnout: {county[1]}\n"
        f"-------------------------\n")
        #f"Total Votes: {county_votes:,}\n"
        #f"-------------------------\n")
    


    txt_file.write(election_results)


        # 1. Iterate through the county list.
    for county in counties_dict:
        # 2. Retrieve vote count of a county.
        votes = counties_dict[county]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the county name and percentage of votes.
        
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        
        txt_file.write(county_results)

#Create three if statements to print out the voter turnout results similar to the results shown above.
        if (county_votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_county = county

#Add the results to the output file.

        
#Print the results to the command line.

print(voters_outcome, end="")
print("\n")
