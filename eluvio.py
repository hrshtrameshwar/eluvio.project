#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
data= pd.read_csv('/Users/harshitrameshwar/Downloads/Eluvio_DS_Challenge.csv')


# In[4]:


data.head()


# In[5]:


data.dtypes


# In[6]:


data.columns


# In[7]:


data['up_votes'].sort_values(ascending=True).value_counts().head()


# In[8]:


data['down_votes'].sort_values(ascending=True).value_counts().head()


# In[9]:


#most upvoted headline
[title for title in data.sort_values('up_votes', ascending=False)['title'][:10]]


# In[10]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style("dark")

data.groupby('date_created')['up_votes'].mean().plot()
data.groupby('date_created')['up_votes'].mean().rolling(window=120).mean().plot(figsize= (12, 4))


# In[11]:


#stories were deemed to be over 18
data.over_18.value_counts()


# In[12]:


#top 10 from over 18 stories
nsfwstory= data[data['over_18']== True]
[story for story in nsfwstory.sort_values('up_votes', ascending=False)['title'][:10]]


# In[13]:


attf= data.author.value_counts()[:20]
attf.plot.bar(figsize= (12, 4))


# In[14]:


taff= data[data['author'] == "davidreiss666"]
#taff.sort_values('up_votes', ascending= False)['title'].value_counts()
[story for story in taff.sort_values('up_votes', ascending=False)['title'][:10]]
#htaff= taff[taff['up_votes'] > 5]


# In[15]:


cand= ['Obama', 'Hillary', 'Trump']
for sole in cand:
   print( data.title.str.contains(sole).value_counts(),sole )


# In[16]:


from nltk import word_tokenize
tokens = data.title.map(word_tokenize)

def tell_me_about(x):
    x_l = x.lower()
    x_t = x.title()
    return data.loc[tokens.map(lambda sent: x_l in sent or x_t in sent).values]


# some headlines related to Apple Inc

# In[17]:


tell_me_about("Apple")['title'].values.tolist()[:10]


# In[18]:


tell_me_about("Hilary")['title'].values.tolist()[:10]


# In[19]:


tell_me_about("Donald")['title'].values.tolist()[:10]


# In[ ]:




