
# coding: utf-8

# In[9]:


import pandas as pd

poll_file = pd.read_csv("election_data_2.csv")
poll_df = pd.DataFrame(poll_file)
poll_df.head(5)


# In[5]:


print("Election Results")
print("-------------------------")


# In[59]:


#Task 1:The total number of votes cast

total_votes = poll_df["Voter ID"].count()
print("Total Votes: " + str(total_votes))
print("-------------------------")


# In[65]:


#Task 2: A complete list of candidates who received votes
results_df = pd.DataFrame(poll_df["Candidate"].unique())
results_df["Percent of Votes"] = 0


# In[67]:


results_df.rename(columns={0: "Candidates"}, inplace=True)
results_df.head()


# In[62]:


#Task 3: The percentage of votes each candidate won
khan_count = poll_df.loc[poll_df["Candidate"] == "Khan"].count() / total_votes
khan_count


# In[69]:


#I am trying to create a variable that is equal to count of "Khan" in second column and divide by total_votes
#somehow it creates a new dataframe with the value across the record...
#Couldnt figure it out.
#End of attempt...

