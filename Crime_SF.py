
# coding: utf-8

# In[2]:


import pandas as pd
import json
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[3]:


crime_file = "_Change_Notice__Police_Department_Incidents.csv"
crime_data_All_DF = pd.read_csv(crime_file)
crime_data_All_DF.head(2)


# In[4]:


len(crime_data_All_DF)


# In[5]:


crime_data_All_DF = crime_data_All_DF.sort_values(["Date"], ascending=False)
crime_data_All_DF.head(2)


# In[6]:


# Get a reference to the column names
crime_data_All_DF.columns


# In[7]:


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


# In[8]:


# Extract some columns
crime_data_All_DF = crime_data_All_DF.loc[:,['Category', 'Descript', 'Day Of Week', 'Date', 'Time', 'District',
       'Resolution', 'Address', 'X', 'Y']]
crime_data_All_DF.head(2)


# In[9]:


# Create a new columns for Year, Day and Month
crime_data_All_DF["Year"] = crime_data_All_DF["Date"].str.rstrip('/').str.split('/').str[2]
crime_data_All_DF["Day"] = crime_data_All_DF["Date"].str.rstrip('/').str.split('/').str[1]
crime_data_All_DF["Month"] = crime_data_All_DF["Date"].str.rstrip('/').str.split('/').str[0]
crime_data_All_DF["Hour"] = crime_data_All_DF["Time"].str.rstrip(':').str.split(':').str[0].astype(int)  

crime_data_All_DF = crime_data_All_DF.sort_values(["Year"], ascending=False)

crime_data_All_DF.head(2)


# In[10]:


bins = [0, 7, 14, 20, 23]
group_names = ['EarlyMorning', 'Morning', 'Evening', 'Night']


crime_data_All_DF["Hour_Bin"] = pd.cut(crime_data_All_DF["Hour"], bins, labels=group_names)
crime_data_All_DF.head(2)




# In[11]:


crime_data_All_DF = crime_data_All_DF.sort_values(['Year','Month', 'Day'], ascending=[False, True,True])
crime_data_All_DF.head(2)

crime_data_All_DF["Resolved"] = np.where(crime_data_All_DF["Resolution"]=='NONE', "Unresolved","Resolved")



# In[12]:


crime_data_All_DF["Year"].value_counts()


# In[13]:


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


# In[14]:


crime_data_All_DF["Resolution"].value_counts()


# # 2016 Heatmap

# In[15]:


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
plt.savefig ("Heat_map_2016.png")
plt.show()


# # 2017 Heatmap

# In[16]:


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
plt.savefig ("Heat_map_2017.png")
plt.show()


# # 2018 Heatmap

# In[17]:


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
plt.savefig ("Heat_map_2018.png")
plt.show()


# In[19]:


#Category_crimes_2016_df.head()


# # Frequency of Crimes per Category 2016

# In[20]:


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

# In[21]:


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

# In[22]:


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

# In[23]:


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

# In[24]:


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

# In[25]:


df_gb3 = pd.DataFrame(crime_data_2018_DF.groupby(['District', 'Hour']).size())
df_gb3.reset_index(inplace=True)
df_gb3.rename(columns={0:"Crimes"}, inplace=True)
df_h3 = df_gb3.pivot("District", "Hour", "Crimes")
fig, ax = plt.subplots()
fig.set_size_inches(16, 4)
plt.savefig ("heatmap_time_2018.png")
ax = sns.heatmap(df_h3, ax=ax, cmap= sns.cm.rocket_r)
plt.show()

# In[110]:


##Getting 2016 unresolved crimes in series
district_2016 = crime_data_2016_DF.groupby(by = ['District',"Resolved"])
district_2016= district_2016.count()
district_2016 = district_2016.drop(["Descript","Day Of Week","Date","Time","Resolution","Address","X","Y","Year","Day","Month","Hour","Hour_Bin"
                   ],axis =1)
district_2016_df=pd.DataFrame(district_2016)
district_2016_df = district_2016_df.rename(columns={"Category":"Count"})
district_2016_df = district_2016_df.reset_index()
unresolved_2016 = district_2016_df.loc[district_2016_df["Resolved"] =="Unresolved","Count"]
district_2016 = district_2016_df["District"].unique()
##district_2017_df

district_2017 = crime_data_2017_DF.groupby(by = ['District',"Resolved"])
district_2017= district_2017.count()
district_2017 = district_2017.drop(["Descript","Day Of Week","Date","Time","Resolution","Address","X","Y","Year","Day","Month","Hour","Hour_Bin"
                   ],axis =1)
district_2017_df=pd.DataFrame(district_2017)
district_2017_df = district_2017_df.rename(columns={"Category":"Count"})
district_2017_df = district_2017_df.reset_index()
unresolved_2017 = district_2017_df.loc[district_2017_df["Resolved"] =="Unresolved","Count"]
district_2017 = district_2017_df["District"].unique()


# In[112]:


##Getting 2015 unresolved crimes in series
district_2015 = crime_data_2015_DF.groupby(by = ['District',"Resolved"])
district_2015= district_2015.count()
district_2015 = district_2015.drop(["Descript","Day Of Week","Date","Time","Resolution","Address","X","Y","Year","Day","Month","Hour","Hour_Bin"
                   ],axis =1)
district_2015_df=pd.DataFrame(district_2015)
district_2015_df = district_2015_df.rename(columns={"Category":"Count"})
district_2015_df = district_2015_df.reset_index()
unresolved_2015 = district_2015_df.loc[district_2015_df["Resolved"] =="Unresolved","Count"]
district_2015 = district_2015_df["District"].unique()


# In[113]:


##Getting 2014 unresolved crimes in series
district_2014 = crime_data_2014_DF.groupby(by = ['District',"Resolved"])
district_2014= district_2014.count()
district_2014 = district_2014.drop(["Descript","Day Of Week","Date","Time","Resolution","Address","X","Y","Year","Day","Month","Hour","Hour_Bin"
                   ],axis =1)
district_2014_df=pd.DataFrame(district_2014)
district_2014_df = district_2014_df.rename(columns={"Category":"Count"})
district_2014_df = district_2014_df.reset_index()
unresolved_2014 = district_2014_df.loc[district_2014_df["Resolved"] =="Unresolved","Count"]
district_2014 = district_2014_df["District"].unique()


# In[116]:


## building the plot

plt.figure(figsize=(15,5))
## plotting 2016 Data
data1 = plt.scatter(district_2016,unresolved_2016,
                    marker= 'o',color='red',label ='2016 Unresolved',s=(unresolved_2016/100))
data2 = plt.scatter(district_2017,unresolved_2017,marker='o',color='blue',label ='2017 Unresolved',s=(unresolved_2017/100))

## plotting 2017 Data
data3 = plt.scatter(district_2015,unresolved_2015,
                    marker= 'o',color='yellow',label ='2015 Unresolved',s=(unresolved_2015/100))
data4 = plt.scatter(district_2014,unresolved_2014,marker='o',color='green',label ='2014 Unresolved',s=(unresolved_2014/100))

plt.legend(handles=[data1,data2,data3,data4],loc="best")
plt.show()



