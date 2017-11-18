
# coding: utf-8

# In[274]:


import pandas as pd
import numpy as np


# In[275]:


schools_path = "schools_complete.csv"
students_path = "students_complete.csv"


# In[276]:


schools_file = pd.read_csv(schools_path)


# In[277]:


students_file = pd.read_csv(students_path)


# In[278]:


print("District Summary")
print("-------------------")


# In[279]:


total_schools = schools_file["School ID"].count()
print("Total number of schools is " + str(total_schools))


# In[280]:


total_students = students_file["name"].count()
print("Total number of students is " + str(total_students))


# In[281]:


total_budget = schools_file["budget"].sum()
print("Total budget for all schools is $" + str(total_budget))


# In[282]:


mean_math_score = students_file["math_score"].mean()
print("Mean math score for all students is " + str("%.2f" % mean_math_score))


# In[283]:


mean_reading_score = students_file["reading_score"].mean()
print("Mean reading score for all students is " + str("%.2f" % mean_reading_score))


# In[284]:


# bootcamp_name.loc[(bootcamp_name["Count"] > 9)
percent_passing_math = students_file.loc[students_file["math_score"] > 69]
percent_passing_math = percent_passing_math["name"].count() / total_students * 100
print("Percent of students who passed math: "+ "%.2f" % percent_passing_math + "%")


# In[285]:


percent_passing_reading = students_file.loc[students_file["reading_score"] > 69]
percent_passing_reading = percent_passing_reading["name"].count() / total_students * 100
print("Percent of students who passed reading: "+ "%.2f" % percent_passing_reading + "%")


# In[286]:


percent_passing_overall = students_file.loc[students_file["reading_score"] > 69]
percent_passing_overall = percent_passing_overall["name"].count() / total_students * 100
print("Overall passing rate: "+ "%.2f" % ((percent_passing_math + percent_passing_reading) / 2 )+ "%")


# In[287]:


summary_table = pd.DataFrame({"Total Schools":[total_schools],
                             "Total Students":[total_students],
                            "Total Budget":[total_budget],
                            "Mean Math Score":["%.2f" % mean_math_score],
                            "Mean Reading Score":["%.2f" % mean_reading_score],
                            "% Passing Math":["%.2f" % percent_passing_math],
                            "% Passing Reading":["%.2f" % percent_passing_reading],
                            "% Overall Passing Rate":["%.2f" % percent_passing_overall]})
summary_table


# In[288]:


print("School Summary")
print("-------------------")


# In[289]:


merged_table = pd.merge(schools_file, students_file, how='left', left_on=["name"], right_on=["school"])
del merged_table["School ID"]
del merged_table["school"]
merged_table.rename(columns={"name_x":"school_name"}, inplace=True)
merged_table.rename(columns={"name_y":"student_name"}, inplace=True)
merged_table.head(10)


# In[290]:


#In [29]: df.groupby(['Col X','Col Y']).size().unstack('Col Y', fill_value=0)
grouped_table = merged_table.groupby(["school_name"]).count()


# In[291]:


schools_file.head()


# In[292]:


schools_file["Avg Math Score"] = schools_file.groupby([students_file["math_score"]]).mean()


# In[ ]:


#Can't figure out if I need to merge both tables and then do calculation or if I should just add columns with corresponding calculations
#Either way, cannot figure out groupby....

