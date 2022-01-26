#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas for the notebook
import pandas as pd

#link for the tables
giiLink="https://en.wikipedia.org/wiki/Gender_Inequality_Index"

# fetching the tables
giidata=pd.read_html(giiLink,header=0,flavor="bs4",attrs={'class':"wikitable sortable"})


# In[3]:


#you will get a list, not a table with previous code. Remember Python starts with zero
giiVars=giidata[0].copy()
# first rows
giiVars.head()


# In[4]:


# these are:
giiVars.columns


# In[5]:


giiVars.columns=giiVars.columns.str.replace("\s|\xad","",regex=True)
giiVars.columns


# In[6]:


giiVars.to_csv("giiVars.csv",index=False)


# In[16]:


linkDataIso='https://github.com/EvansDataScience/CTforGA_integrating/raw/main/isodata.csv'

# using 'read_csv' with a link - this is how you read in a csv file!
DataIso=pd.read_csv(linkDataIso)


# In[18]:


linkDataWho='https://github.com/Kent253/computuer-analysis/raw/main/GenderProject/NHA_indicators.csv'

DataWho=pd.read_csv(linkDataWho)


# In[19]:


DataWho.columns


# In[20]:


allData=giiVars.merge(DataWho)


# In[21]:


allData.head()


# In[22]:


giiVars.shape


# In[23]:


allData.shape


# In[26]:


allData2=giiVars.merge(DataWho,how='outer',indicator='True')


# In[28]:


allData2.shape


# In[34]:


# The countries unmatched
UnmatchedLeft=allData2[allData2['True']=='left_only'].Country.to_list()
UnmatchedRight=allData2[allData2['True']=='right_only'].Country.to_list()


# In[35]:


UnmatchedLeft[0]


# In[36]:


from thefuzz import process
#process extractOne gives you the best match, process extract requires limit (shown belw)
process.extractOne(UnmatchedLeft[0], UnmatchedRight)


# In[39]:


UnmatchedLeft=allData2[allData2['True']=='left_only'].Country.to_list()
UnmatchedLeft


# In[40]:


[(left, process.extractOne(left, UnmatchedRight)) for left in sorted(UnmatchedLeft)]


# In[44]:


TotallyWrong=[('Albania', ('United Republic of Tanzania', 64)),
              ('Libya', ('Bolivia Plurinational States of ', 54)),
              ('Macedonia', ('The Republic of North Macedonia', 90)),
              ('Syrian Arab Republic', ('Venezuela (Bolivarian Republic of)', 86)),
              ('UAE', ('Equatorial Guinea', 60)),
              ('Taiwan', ('United Republic of Tanzania', 60)),
              ('Yemen', ('Turkmenistan', 54))]


# In[ ]:





# In[45]:


omitLeft=[leftName for (leftName,rightFuzzy) in TotallyWrong] #parenthesis not needed
omitLeft


# In[46]:


{process.extractOne(left, UnmatchedRight)[0]:left for left in UnmatchedLeft if left not in omitLeft}


# In[49]:


changesRight={process.extractOne(left, UnmatchedRight)[0]:left for left in UnmatchedLeft if left not in omitLeft}
DataWho.Country.replace(changesRight,inplace=True)


# In[50]:


bruteForceChanges={'United Republic of Tanzania':'Tanzania', 
                'Bolivia Plurinational States of ':'Bolivia',
                'The Republic of North Macedonia':'North Macedonia', 
                'Venezuela (Bolivarian Republic of)':'Venezuela',
                'Equatorial Guinea':'Guinea',
                "Turkmenistan":'Turkmenistan'}

# replacing
DataWho.Country.replace(bruteForceChanges,inplace=True)


# In[52]:


allData3=giiVars.merge(DataWho)

# current dimension
allData3.shape


# In[54]:


allData3.to_csv('allData3.csv',index=False)


# In[55]:


## one more dataset
#link for the tables
educationLink="https://en.wikipedia.org/wiki/List_of_countries_by_spending_on_education_(%25_of_government_expenditure)"

# fetching the tables
EDdata=pd.read_html(educationLink,header=0,flavor="bs4",attrs={'class':"wikitable sortable"})


# In[56]:


#you will get a list, not a table with previous code. Remember Python starts with zero
EDVars=EDdata[0].copy()
# first rows
EDVars.head()


# In[58]:


allData4=allData3.merge(EDVars,how='outer',indicator='True')


# In[59]:


allData4.columns


# In[60]:


# explore matched and unmatched counts:
allData4['True'].value_counts()


# In[61]:


UnmatchedLeft=allData4[allData4['True']=='left_only'].Country.to_list()
UnmatchedRight=allData4[allData4['True']=='right_only'].Country.to_list()


# In[62]:


from thefuzz import process
#process extractOne gives you the best match, process extract requires limit (shown belw)
process.extractOne(UnmatchedLeft[0], UnmatchedRight)


# In[64]:


UnmatchedLeft=allData4[allData4['True']=='left_only'].Country.to_list()
UnmatchedLeft


# In[65]:


[(left, process.extractOne(left, UnmatchedRight)) for left in sorted(UnmatchedLeft)]


# In[66]:


TotallyWrong=[('Algeria', ('United States of America', 64)),
              ('Angola', ('Congo', 55)),
              ('Bahamas', ('Brunei Darussalam', 45)),
              ('Bosnia and Herzegovina', ('Guinea', 60)),
              ('Botswana', ('United Republic of Tanzania', 56)),
              ('Canada', ('Grenada', 62)),
              ('Central African Republic', ('Republic of Moldova', 56)),
              ('China', ('Guinea', 55)),
              ('Costa Rica', ('United States of America', 54)),
              ('Cuba', ('United States of America', 60)),
              ('Dominican Republic', ('Dominica', 90)),
              ('Egypt', ('Timor-Leste', 40)),
              ('Greece', ('Grenada', 46)),
              ('Iraq', ('Albania', 60)),
              ('Kuwait', ('Vanuatu', 46)),
              ('Montenegro', ('Congo', 53)),
              ('Morocco', ('Comoros', 57)),
              ('Nicaragua', ('Guinea', 60)),
              ('Panama', ('Brunei Darussalam', 50)),
              ('Papua New Guinea', ('Guinea', 90)),
              ('Paraguay', ('Guinea', 43)),
              ('Philippines', ('Guinea', 45)),
              ('Saudi Arabia', ('Albania', 60)),
              ('South Korea', ('South Sudan', 64)),
              ('Sudan', ('South Sudan', 90)),
              ('Suriname', ('Guinea', 57)),
              ('Tonga', ('Congo', 60)),
              ('Trinidad and Tobago', ('Saint Vincent and the Grenadines', 86)),
              ('Venezuela', ('Vanuatu', 50)),
              ('Zambia', ('United Republic of Tanzania', 66))]


# In[67]:


omitLeft=[leftName for (leftName,rightFuzzy) in TotallyWrong] #parenthesis not needed
omitLeft


# In[68]:


{process.extractOne(left, UnmatchedRight)[0]:left for left in UnmatchedLeft if left not in omitLeft}


# In[69]:


changesRight={process.extractOne(left, UnmatchedRight)[0]:left for left in UnmatchedLeft if left not in omitLeft}
EDVars.Country.replace(changesRight,inplace=True)


# In[71]:


bruteForceChanges={'United States of America':'United States',
              'Congo':'Republic of the Congo',
              'Brunei Darussalam':'Brunei',
              'United Republic of Tanzania':'Tanzania', 
              'Republic of Moldova':'Moldova'}
              
                
# replacing
EDVars.Country.replace(bruteForceChanges,inplace=True)


# In[72]:


allData5=allData4.merge(EDVars)

# current dimension
allData5.shape


# In[73]:


allData5.to_csv('allData5.csv',index=False)

