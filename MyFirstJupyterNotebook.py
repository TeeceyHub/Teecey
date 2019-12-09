#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello Anaconda")


# In[1]:


print("Hello Anaconda")


# In[3]:


# Import the panda command first before use so python can understand the pd command
import pandas as pd
data=[1,2,3,4]
series1=pd.Series(data)
series1


# In[4]:


# How to cheeck type
type(series1)


# In[5]:


# How to change the index name of a series object
series1=pd.Series(data, index=['a','b','c','d'])
series1


# In[6]:


# How to create a dataframe using a list
import pandas as pd
data=[1,2,3,4,5]
df=pd.DataFrame(data)
df


# In[7]:


# Creating a dataframe using a dictionary
dictionary={'fruits':['apples','banana','mangoes','oranges','pineapples'],'count':[10,15,20,25,30]}
df=pd.DataFrame(dictionary)
df


# In[10]:


# Creating a dataframe using a series
series=pd.Series([6,12,18,24],index=['a','b','c','d'])
df=pd.DataFrame(series)
df


# In[28]:


# Creating a dataframe using a numpy array
import numpy as np
numpyarray=np.array([[50000,60000,70000,80000],['Ivan','Sergio','Luis','Leo']])
df=pd.DataFrame({'Name':numpyarray[1], 'Salary':numpyarray[0]})
df


# In[19]:


# How to perform a merge operation
player = ['Gerard', 'Samuel', 'Ousmane', 'Nelson']
point = [8,7.5,8.5,8]
title = ['Game1', 'Game2', 'Game3', 'Game4']
df1 = pd.DataFrame({'Player':player, 'Points':point, 'Title':title})
df1


# In[20]:


player = ['Andre', 'Frenkie', 'Arthur', 'Ousmane']
strength = ['Reflex', 'Movement', 'Rhythym', 'Positioning']
title = ['Game1', 'Game6', 'Game7', 'Game8']
df2 = pd.DataFrame({'Player':player, 'Strength':strength, 'Title':title})
df2


# In[21]:


# Inner Merge
df1.merge(df2, on='Title', how= 'inner')


# In[22]:


# Inner Merge
df1.merge(df2, on='Player', how= 'inner')


# In[23]:


# Left Merge
df1.merge(df2, on='Player', how = 'left')


# In[24]:


# Right Merge
df1.merge(df2, on='Player', how = 'right')


# In[25]:


# Outer Merge
df1.merge(df2, on='Player', how = 'outer')


# In[31]:


# How to perform Join operation
player = ['Andre', 'Frenkie', 'Arthur', 'Ousmane']
strength = ['Reflex', 'Movement', 'Rhythym', 'Positioning']
title = ['Game1', 'Game6', 'Game7', 'Game8']
df3 = pd.DataFrame({'Player':player, 'Strength':strength, 'Title':title}, index = ['GK', 'CM', 'AM', 'WF'])
df3


# In[44]:


player = ['Gerard', 'Samuel', 'Ousmane', 'Nelson']
point = [8,7.5,8.5,8]
title = ['Game5', 'Game2', 'Game3', 'Game4']
df4 = pd.DataFrame({'Players':player, 'Point':point, 'Titles':title}, index = ['SW', 'CM', 'WF', 'RB'])
df4


# In[45]:


# Inner Join (join operation is done on the basis of index value therefore there is no 'on' command)
df3.join(df4, how = 'inner')


# In[46]:


# Left join
df3.join(df4, how = 'left')


# In[47]:


# Right join
df3.join(df4, how = 'right')


# In[48]:


# Outer join
df3.join(df4, how = 'outer')


# In[ ]:


#Moving on


# In[ ]:


# Now


# In[50]:


# How to Concatenate two dataframes in panda
pd.concat([df3,df4])


# In[ ]:


# Importing a dataset using pandas
import pandas as pd
# Read dataset and store as dataframe e.g as a .csv file. For a dataframe named cars we have
cars.pd.read_csv(specify path to csv file)
#print
You should see CARS printed.
# Output will show the dataframe i.e a tabulated list of cars under various columns and rows


# In[ ]:


# Analyzing  the imported dataset
type(cars)
# Output should show DataFrame


# In[ ]:


# View only the first five records in the dataframe
cars.head()

# View first ten
cars.head(10)

# View only last five records in the dataframe
cars.tail()

# View last ten
cars.tail(10)

# View total number of row and columns in the dataframe
cars.shape

# Print a concise summary of the columns
cars.info(null_counts=True)

# Mean (gives mean of each column)
cars.mean()

# Median
cars.median()

# Standard deviation
cars.std()

# Maximum value for each column
cars.max()

# Minimum value
cars.min()

# Number of non-null records in each column
cars.count()

# Descriptive statistics summary
cars.describe()


# In[9]:


import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    print (df)
    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()


# In[21]:


import pandas as pd
Sales = pd.read_excel(r"C:\Users\user\Desktop\Sales.xlsx", "Sheet1")
print (Sales)


# In[23]:


Sales=pd.read_excel("C:/Users/user/Desktop/Sales.xlsx")
Sales


# In[24]:


Sales.head()


# In[25]:


Sales.head(54)


# In[26]:


Sales.tail()


# In[27]:


Sales.max()


# In[28]:


Sales.describe()


# In[30]:


Sales.shape


# In[31]:


Sales.count()


# In[32]:


Sales.info(null_counts=True)


# In[33]:


# Data Cleaning

# First, Rename a column
Sales = Sales.rename(columns={'Category':'Categories'})
Sales


# In[ ]:


# Fill null values with mean of the column (This doesn't really apply to my dataframe "Sales" so i'll use df instead as example)
df.columnwithnullvalues = df.columnwithnullvalues.fillna(df.columnwithnullvalues.mean())
df


# In[ ]:


# Drop unwanted column
df = df.drop(columns=['nameofcolumn'])
df


# In[40]:


# Finding correlation matrix
SalesCorr = Sales[['Postcode', 'Sales']].corr()
SalesCorr


# In[42]:


# Changing data type
Sales.Sales=Sales.Sales.astype(int)

# See the change
Sales.info(null_counts=True)


# In[43]:


# Verify the change
Sales.head(51)


# In[45]:


# Indexing by position

# I want to view Buyer column only
Sales.iloc[:,9]


# In[46]:


# View first five records of the Buyer column
Sales.iloc[0:5,9]


# In[47]:


# All rows and columns
Sales.iloc[:,:]


# In[50]:


# View from 6th row, 4th column till the end
Sales.iloc[5:,4:]


# In[51]:


# View all rows but only one column. This is indexing by columns number
Sales.iloc[:,7]


# In[53]:


# View all rows but only one column. This is indexing by columns name
Sales.loc[:,'Manager']


# In[54]:


# Display the records from index o to index 6 from Buyer column
Sales.loc[:6,'Buyer']


# In[55]:


Sales.loc[0:6,'Buyer']


# In[56]:


Sales.loc[:5,'Buyer']


# In[57]:


# See first seven records from Financial Year to Sales
Sales.loc[:6,'Financial Year':'Sales']


# In[ ]:


# Setting a specific value to an entire column
df['columnname'] = specificvalue
df


# In[59]:


# Applying function
# Lets say i want to double up records in postcode using lambda fxn
f=lambda x: x*2
Sales['Postcode']=Sales['Postcode'].apply(f)
Sales


# In[64]:


# Sorting column in ascending order
Sales.sort_values(by='Postcode')


# In[ ]:





# # Let me import my dataframe afresh so i can have the original data in the table for this sorting.

# In[4]:


Sales2014=pd.read_csv("C:\\Users\\user\\Desktop\\JDS\\EXCEL\\Sales2014.csv")
Sales2014


# In[5]:


#Sorting column by values
Sales2014.sort_values(by='Order Quantity')


# In[32]:


# Sorting by Descending order
Sales2014.sort_values(by='Order Quantity', ascending=False)


# In[11]:


Sales2014.sort_values(by='Order ID', ascending=True)


# In[34]:


# Filtering
Filter1 = Sales2014['Order Quantity'] > 5
Filter1


# In[35]:


Filter1.shape


# In[36]:


Filter1.count()


# In[37]:


Filter2 = Sales2014[Filter1]
Filter2


# In[39]:


Filter3 = Sales2014['Unit Sell Price'] > 20
Filter3


# In[40]:


Filter4 = Sales2014[Filter3]
Filter4


# In[61]:


#This operation with ampersand joins two filters therefore showing me only columns with unit price above 20 AND quantity above 5
NFilter = ((Sales2014['Unit Sell Price'] > 20) & (Sales2014['Order Quantity'] > 5))
FilterN = Sales2014[NFilter]
FilterN


# In[ ]:


# Machine Learning


# In[ ]:




