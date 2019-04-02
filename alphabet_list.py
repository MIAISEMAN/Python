#!/usr/bin/env python
# coding: utf-8

# In[6]:


from string import (ascii_lowercase, ascii_uppercase)


# In[7]:


ascii_lowercase


# In[12]:


enumerate('a')


# In[15]:


name = 'mia'

enumerate(name)
# In[16]:


enumerate(name)


# In[17]:


enumerate(ascii_lowercase)


# In[19]:


letters_list = list(ascii_lowercase)

letters_list
# In[20]:


letters_list


# In[35]:


numbers=list(range(0,26))


# letters

# In[23]:


letters_list


# In[36]:


numbers


# In[26]:


dict(zip(letters_list, numbers))


# In[27]:


alphabet_data = dict(zip(letters_list, numbers))


# In[28]:


alphabet_data


# In[29]:



# In[32]:


list(enumerate(letters_list))


# In[33]:


alpha_data= dict(enumerate(letters_list))


# In[34]:


{l:n for (n,l) in alpha_data.items()}


# In[40]:


alpha_data2={}
for i in numbers:
    alpha_data2[letters_list[i]]=i
print (alpha_data2)


# In[ ]:





# In[ ]:




