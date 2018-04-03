
# coding: utf-8

# In[1]:


import pandas as pd
import json
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


crime_file = "_Change_Notice__Police_Department_Incidents.csv"
crime_data_All_DF = pd.read_csv(crime_file)
crime_data_All_DF.head(2)


# In[3]:


len(crime_data_All_DF)


# In[4]:


crime_data_All_DF = crime_data_All_DF.sort_values(["Date"], ascending=False)
crime_data_All_DF.head(2)


# In[5]:


# Get a reference to the column names
crime_data_All_DF.columns


# In[6]:


# Rename column headers
crime_data_All_DF = crime_data_All_DF.rename(columns={"IncidntNum":"ID",
                                       "Category":"Category",
                                       "Descript":"Descript",
                                       "DayOfWeek":"Day Of Week",
                                       "Date":"Date",
                                       "Time":"Time",
                                       "PdDistrict":"District",
                                       "Resolution":"Resolution"})
crime_data_All_DF.columns


# In[7]:


# Extract some columns
crime_data_All_DF = crime_data_All_DF.loc[:,['Category', 'Descript', 'Day Of Week', 'Date', 'Time', 'District',
       'Resolution', 'Address', 'X', 'Y']]
crime_data_All_DF.head(2)


# In[8]:


# Create a new columns for Year, Day and Month
crime_data_All_DF["Year"] = crime_data_All_DF["Date"].str.rstrip('/').str.split('/').str[2]
crime_data_All_DF["Day"] = crime_data_All_DF["Date"].str.rstrip('/').str.split('/').str[1]
crime_data_All_DF["Month"] = crime_data_All_DF["Date"].str.rstrip('/').str.split('/').str[0]
crime_data_All_DF["Hour"] = crime_data_All_DF["Time"].str.rstrip(':').str.split(':').str[0].astype(int)  

crime_data_All_DF = crime_data_All_DF.sort_values(["Year"], ascending=False)

crime_data_All_DF.head(2)


# In[9]:


bins = [0, 7, 14, 20, 23]
group_names = ['EarlyMorning', 'Morning', 'Evening', 'Night']


crime_data_All_DF["Hour_Bin"] = pd.cut(crime_data_All_DF["Hour"], bins, labels=group_names)
crime_data_All_DF.head(2)


# In[10]:


crime_data_All_DF = crime_data_All_DF.sort_values(['Year','Month', 'Day'], ascending=[False, True,True])
crime_data_All_DF.head(2)


# In[11]:


crime_data_All_DF["Year"].value_counts()


# In[12]:


# Creating a data frame for each year
crime_data_2003_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2003",:]
crime_data_2004_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2004",:]
crime_data_2005_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2005",:]
crime_data_2006_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2006",:]
crime_data_2007_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2007",:]
crime_data_2008_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2008",:]
crime_data_2009_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2009",:]
crime_data_2010_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2010",:]
crime_data_2011_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2011",:]
crime_data_2012_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2012",:]
crime_data_2013_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2013",:]
crime_data_2014_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2014",:]
crime_data_2015_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2015",:]
crime_data_2016_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2016",:]
crime_data_2017_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2017",:]
crime_data_2018_DF = crime_data_All_DF.loc[crime_data_All_DF["Year"] == "2018",:]


# In[13]:


crime_data_All_DF["Resolution"].value_counts()


# # 2016 Heatmap

# In[14]:


#Cross-tabulate Category and PdDistrict
crime_data_2016_CT = pd.crosstab(crime_data_2016_DF.District,crime_data_2016_DF.Category,margins=True)
del crime_data_2016_CT['All'] #delete the All column
crime_data_2016_CT = crime_data_2016_CT.iloc[:-1]# delete last row (All)

#set the labels
column_labels_2016 = list(crime_data_2016_CT.columns.values)
row_labels_2016 = crime_data_2016_CT.index.values.tolist()

#plot to a heatmap using matplotlib  
fig,ax = plt.subplots()
heatmap = ax.pcolor(crime_data_2016_CT,cmap='Reds')

#format
 
fig.set_size_inches(15,5)
 

# Tick placement 

ax.set_yticks(np.arange(crime_data_2016_CT.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(crime_data_2016_CT.shape[1])+0.5, minor=False)

 
ax.set_xticklabels(column_labels_2016, minor=False)
ax.set_yticklabels(row_labels_2016, minor=False)
#rotate
plt.xticks(rotation=90)
plt.title("Heatmap for Crimes in SF : 2016", fontsize=20, weight='bold')
plt.colorbar(heatmap)
plt.savefig ("Heat_map_2016.png")
plt.show()


# # 2017 Heatmap

# In[25]:


#Cross-tabulate Category and PdDistrict
crime_data_2017_CT = pd.crosstab(crime_data_2017_DF.District,crime_data_2017_DF.Category,margins=True)
del crime_data_2017_CT['All'] #delete the All column
crime_data_2017_CT = crime_data_2017_CT.iloc[:-1]# delete last row (All)

#set the labels
column_labels_2017 = list(crime_data_2017_CT.columns.values)
row_labels_2017 = crime_data_2017_CT.index.values.tolist()

#plot to a heatmap using matplotlib  
fig,ax = plt.subplots()
heatmap = ax.pcolor(crime_data_2017_CT,cmap='Reds')

#format
 
fig.set_size_inches(15,5)
 

# Tick placement 

ax.set_yticks(np.arange(crime_data_2017_CT.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(crime_data_2017_CT.shape[1])+0.5, minor=False)

 
ax.set_xticklabels(column_labels_2017, minor=False)
ax.set_yticklabels(row_labels_2017, minor=False)
#rotate
plt.xticks(rotation=90)
plt.title("Heatmap for Crimes in SF : 2017", fontsize=20, weight='bold')
plt.colorbar(heatmap)
plt.savefig ("Heat_map_2017.png")
plt.show()


# # 2018 Heatmap

# In[24]:


#Cross-tabulate Category and PdDistrict
crime_data_2018_CT = pd.crosstab(crime_data_2018_DF.District,crime_data_2018_DF.Category,margins=True)
del crime_data_2018_CT['All'] #delete the All column
crime_data_2018_CT = crime_data_2018_CT.iloc[:-1]# delete last row (All)

#set the labels
column_labels_2018 = list(crime_data_2018_CT.columns.values)
row_labels_2018 = crime_data_2018_CT.index.values.tolist()

#plot to a heatmap using matplotlib  
fig,ax = plt.subplots()
heatmap = ax.pcolor(crime_data_2018_CT,cmap='Reds')

#format
 
fig.set_size_inches(15,5)
 

# Tick placement 

ax.set_yticks(np.arange(crime_data_2018_CT.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(crime_data_2018_CT.shape[1])+0.5, minor=False)

 
ax.set_xticklabels(column_labels_2018, minor=False)
ax.set_yticklabels(row_labels_2018, minor=False)
#rotate
plt.xticks(rotation=90)
plt.title("Heatmap for Crimes in SF : 2018", fontsize=20, weight='bold')
plt.colorbar(heatmap)
plt.savefig ("Heat_map_2018.png")
plt.show()


# In[17]:


#Category_crimes_2016_df.head()


# # Frequency of Crimes per Category 2016

# In[18]:


#frequency count for Category
Category_crimes_2016_df = pd.DataFrame(crime_data_2016_DF.Category.value_counts())


Category_crimes_2016_df["Percentage"] = Category_crimes_2016_df["Category"]/Category_crimes_2016_df["Category"].sum()
Category_crimes_2016_df
 
fig = Category_crimes_2016_df["Percentage"].plot(kind="bar", figsize = (20,10), rot=75) 

fig.set_title("Frequency of Crimes by Category", fontsize=15, weight = "bold")
fig.set_ylabel("Percentage of Crimes", fontsize=12)
plt.savefig('perc_crime_category_2016.png')
plt.show()


#Average daily crime per category
avg_daily_crime = pd.DataFrame(crime_data_2016_DF["Day Of Week"].value_counts()/52)

avg_daily_crime.columns=['avg']
avg_daily_crime.reset_index(inplace=True)
avg_daily_crime.rename(columns = {"index": "day"},   inplace=True)
avg_daily_crime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mapping = {day: i for i, day in enumerate(weekdays)}
key = avg_daily_crime['day'].map(mapping)
avg_daily_crime = avg_daily_crime.iloc[key.argsort()]

ax= avg_daily_crime.plot(x='day', kind="bar", figsize = (20,7), width = 0.5, rot=45, color= "salmon", legend=False)
ax.set_xlabel('')

ax.set_title("Average Daily Crime", fontsize=20, weight='bold')
ax.set_ylabel("Number of Crimes ", fontsize= 15)
plt.savefig('avg_daily2016.png')
plt.show()


# # Frequency of Crime per Category 2017

# In[19]:


# Percentage of crime per category
Category_crimes_2017_df = pd.DataFrame(crime_data_2017_DF.Category.value_counts())


Category_crimes_2017_df["Percentage"] = Category_crimes_2017_df["Category"]/Category_crimes_2017_df["Category"].sum()
 
fig = Category_crimes_2017_df["Percentage"].plot(kind="bar", figsize = (20,10), rot=75) 

fig.set_title("Frequency of Crimes by Category", fontsize=15, weight = "bold")
fig.set_ylabel("Percentage of Crimes", fontsize=12)
plt.savefig('perc_crime_category_2017.png')
plt.show()


# Average daily crime per category
avg_daily_crime = pd.DataFrame(crime_data_2017_DF["Day Of Week"].value_counts()/52)

avg_daily_crime.columns=['avg']
avg_daily_crime.reset_index(inplace=True)
avg_daily_crime.rename(columns = {"index": "day"},   inplace=True)
avg_daily_crime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mapping = {day: i for i, day in enumerate(weekdays)}
key = avg_daily_crime['day'].map(mapping)
avg_daily_crime = avg_daily_crime.iloc[key.argsort()]

ax= avg_daily_crime.plot(x='day', kind="bar", figsize = (20,7), width = 0.5, rot=45, color= "salmon", legend=False)
ax.set_xlabel('')

ax.set_title("Average Daily Crime", fontsize=20, weight='bold')
ax.set_ylabel("Number of Crimes ", fontsize= 15)
plt.savefig('avg_daily2017.png')
plt.show()


# # Frequency of Crime per Category 2018

# In[20]:


# Percentage of crime per category

Category_crimes_2018_df = pd.DataFrame(crime_data_2018_DF.Category.value_counts())


Category_crimes_2018_df["Percentage"] = Category_crimes_2018_df["Category"]/Category_crimes_2018_df["Category"].sum()
 
fig = Category_crimes_2018_df["Percentage"].plot(kind="bar", figsize = (20,10), rot=75) 

fig.set_title("Frequency of Crimes by Category", fontsize=15, weight = "bold")
fig.set_ylabel("Percentage of Crimes", fontsize=12)
plt.savefig('perc_crime_category_2018.png')
plt.show()


# Average daily crime per category

avg_daily_crime = pd.DataFrame(crime_data_2018_DF["Day Of Week"].value_counts()/8)

avg_daily_crime.columns=['avg']
avg_daily_crime.reset_index(inplace=True)
avg_daily_crime.rename(columns = {"index": "day"},   inplace=True)
avg_daily_crime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mapping = {day: i for i, day in enumerate(weekdays)}
key = avg_daily_crime['day'].map(mapping)
avg_daily_crime = avg_daily_crime.iloc[key.argsort()]

ax= avg_daily_crime.plot(x='day', kind="bar", figsize = (20,7), width = 0.5, rot=45, color= "salmon", legend=False)
ax.set_xlabel('')

ax.set_title("Average Daily Crime", fontsize=20, weight='bold')
ax.set_ylabel("Number of Crimes ", fontsize= 15)
plt.savefig('avg_daily2018.png')
plt.show()


# # Heatmap:  crime by District and time 2016

# In[21]:


df_gb = pd.DataFrame(crime_data_2016_DF.groupby(['District', 'Hour']).size())
df_gb.reset_index(inplace=True)
df_gb.rename(columns={0:"Crimes"}, inplace=True)
df_h = df_gb.pivot("District", "Hour", "Crimes")
fig, ax = plt.subplots()
fig.set_size_inches(16, 4)
ax = sns.heatmap(df_h, ax=ax, cmap= sns.cm.rocket_r )
plt.savefig ("heatmap_time_2016.png")
plt.show()


# # Heatmap: crime by District and Time 2017

# In[22]:


df_gb2 = pd.DataFrame(crime_data_2017_DF.groupby(['District', 'Hour']).size())
df_gb2.reset_index(inplace=True)
df_gb2.rename(columns={0:"Crimes"}, inplace=True)
df_h2 = df_gb2.pivot("District", "Hour", "Crimes")
fig, ax = plt.subplots()
fig.set_size_inches(16, 4)
plt.savefig ("heatmap_time_2017.png")
ax = sns.heatmap(df_h2, ax=ax, cmap= sns.cm.rocket_r)
plt.show()


# # Heatmap: crime by District and Time 2018

# In[23]:


df_gb3 = pd.DataFrame(crime_data_2018_DF.groupby(['District', 'Hour']).size())
df_gb3.reset_index(inplace=True)
df_gb3.rename(columns={0:"Crimes"}, inplace=True)
df_h3 = df_gb3.pivot("District", "Hour", "Crimes")
fig, ax = plt.subplots()
fig.set_size_inches(16, 4)
plt.savefig ("heatmap_time_2018.png")
ax = sns.heatmap(df_h3, ax=ax, cmap= sns.cm.rocket_r)
plt.show()

print("I am done")