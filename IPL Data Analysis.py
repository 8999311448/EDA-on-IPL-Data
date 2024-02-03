#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[12]:


#loading the ipl match dataset
ipl=pd.read_csv(r'C:\Users\saksh\Downloads\matches.csv')


# In[14]:


#having a glance at the first 5 records of the dataset
ipl.head()


# In[18]:


#Number of rows and columns
ipl.shape


# In[19]:


#getting the frequency of most man of the match awards from the datatset
ipl['player_of_match'].value_counts()


# In[20]:


#getting the top 10 players with most man of the match awards from the datatset
ipl['player_of_match'].value_counts()[0:10]


# In[22]:


#getting the top 5 players with most man of the match awards from the datatset
ipl['player_of_match'].value_counts()[0:5]


# In[25]:


#making a bar plot for the top 5 players with most man of the match awards
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), list(ipl['player_of_match'].value_counts()[0:5]), color=['red', 'blue', 'green', 'pink', 'yellow'])
plt.show()


# In[26]:


#Getting the frequency of the result column
ipl['result'].value_counts()


# In[50]:


#making a bar plot for the frequency of the result column
plt.figure(figsize=(5,5))
plt.bar(list(ipl['result'].value_counts().keys()), list(ipl['result'].value_counts()), color=['red', 'blue', 'green',])
plt.show()


# In[31]:


#number of toss win w.r.t. each team
ipl['toss_winner'].value_counts()


# In[46]:


#making a pie chart for the percent of toss win w.r.t. each team
plt.figure(figsize=(8,8))
plt.pie(list(ipl['toss_winner'].value_counts()), labels= list(ipl['toss_winner'].value_counts().keys()), autopct='%0.1f%%')
plt.show()


# In[33]:


#Extract the records where team batting first won the match
batting_first=ipl[ipl['win_by_runs']!=0]


# In[34]:


#looking at the records in batting_first dataset
batting_first.head()


# In[39]:


#Making a histogram for visualizing the above data
plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'], color='green')
plt.title('Distribution of Runs')
plt.xlabel('Win by run')
plt.ylabel('Frequency')
plt.show()


# In[40]:


#Finding out the number of wins w.r.t each team post batting first
batting_first['winner'].value_counts()


# In[43]:


#making a bar graph to ploy the visualization of top 5 teams with most wins post batting first
plt.figure(figsize=(8,8))
plt.bar(list(batting_first['winner'].value_counts()[0:5].keys()), list(batting_first['winner'].value_counts()[0:5]), color=['blue', 'yellow', 'green', 'purple', 'red'])
plt.title('No of wins respect to teams')
plt.xlabel('Teams')
plt.ylabel('Frequency')
plt.show()


# In[70]:


#making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()), labels= list(batting_first['winner'].value_counts().keys()), autopct='%0.1f%%')
plt.show()


# In[51]:


#extracting records where a team won after batting second
batting_second= ipl[ipl['win_by_wickets']!=0]


# In[53]:


#vieing the first 5 records in batting_second
batting_second.head()


# In[68]:


#Making a histogram for visualizing the above data
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins= 20, color='pink')
plt.title('Distribution of Runs')
plt.xlabel('Win by wickets')
plt.ylabel('Frequency')
plt.show()


# In[55]:


#Finding out the number of wins w.r.t each team post batting second
batting_second['winner'].value_counts()


# In[64]:


#making a bar graph to plot the visualization of top 5 teams with most wins post batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:5].keys()), list(batting_second['winner'].value_counts()[0:5]), color=['purple', 'blue', 'red', 'yellow', 'crimson'])
plt.title('No of wins respect to teams')
plt.xlabel('Teams')
plt.ylabel('Frequency')
plt.show()


# In[69]:


#making a pie chart
plt.figure(figsize=(6,6))
plt.pie(list(batting_second['winner'].value_counts()), labels= list(batting_second['winner'].value_counts().keys()), autopct='%0.1f%%')
plt.show()


# In[71]:


#No of matches played each season
ipl['season'].value_counts()


# In[72]:


#No of matches held in each city
ipl['city'].value_counts()


# In[76]:


#making a bar graph
plt.figure(figsize=(5,5))
plt.bar(list(ipl['city'].value_counts()[0:5].keys()), list(ipl['city'].value_counts()[0:5]), color=['purple', 'blue', 'red', 'yellow', 'crimson'])
plt.title('No of wins respect to teams')
plt.xlabel('Teams')
plt.ylabel('Frequency')
plt.show()


# In[73]:


#finding out no of times a team has won the match after winning the toss
import numpy as np
np.sum(ipl['toss_winner']== ipl['winner'])


# In[ ]:




