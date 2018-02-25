
# coding: utf-8

# In[28]:


import pandas as pd

bdg_file1 = pd.read_csv("budget_data_1.csv")
bdg_file1.head(2)


# In[29]:


bdg_file2 = pd.read_csv("budget_data_2.csv")
bdg_file2.head(2)


# In[108]:


print("Financial Analysis")
print("----------------------------")


# In[53]:


bdg1_df = pd.DataFrame(bdg_file1)
bdg2_df = pd.DataFrame(bdg_file2)
combined_df = bdg1_df.append(bdg2_df)


# In[109]:


#Task 1: The total number of months included in the dataset
total_months = combined_df["Date"].count()
print("Total Months: " + str(total_months))


# In[110]:


#Task 2: The total amount of revenue gained over the entire period
total_rev = combined_df["Revenue"].sum()
print("Total Revenue: $ " + str(total_rev))


# In[100]:


#Task 3: The average change in revenue between months over the entire period
avg_change = combined_df["Revenue"].mean()
print("Average Revenue Change: $" + str(avg_change))


# In[105]:


#Task 4: The greatest increase in revenue (date and amount) over the entire period
max_rev = combined_df["Revenue"].max()
max_record = combined_df.loc[combined_df["Revenue"] == max_rev]
print("Greatest Increase in Revenue: " + str(max_record.iloc[0,0]) + " ($ " + str(max_record.iloc[0,1]) + ")" )


# In[107]:


#Task 5: The greatest decrease in revenue (date and amount) over the entire period
min_rev = combined_df["Revenue"].min()
min_record = combined_df.loc[combined_df["Revenue"] == min_rev]
print("Greatest Decrease in Revenue: " + str(min_record.iloc[0,0]) + " ($ " + str(min_record.iloc[0,1]) + ")" )


# In[111]:


#Exercise completed!
print("----------------------------")
print("Hooray, I finished this exercise!")

