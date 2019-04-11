#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap


# In[4]:


output_file("cAnceR_TorsoCancers_Horizontal.html")


# In[5]:


dt = pd.read_excel('/Users/ylhaart/TUNI.fi/Hanna-Riikka Rantamaa - Interaction techniques project/Data/TorsoCancers.xlsx',usecols='A,B')


# In[6]:


dt


# In[9]:


dt2 = dt[::-1]


# In[10]:


dt2


# In[11]:


names = dt2['Cancer']


# In[12]:


names


# In[13]:


names[31]


# In[14]:


counts = dt2['Number']


# In[15]:


counts


# In[16]:


counts.max()


# In[18]:


source = ColumnDataSource(data=dict(names=dt2['Cancer'], counts=dt2['Number']))


# In[19]:


p = figure(y_range=names, toolbar_location=None, title="Torso Cancers")


# In[20]:


p.hbar(y='names', right='counts', height=1.0, source=source, line_color='white', legend=None, fill_color='blue')


# In[21]:


p.ygrid.grid_line_color = None


# In[22]:


p.x_range.start = 0


# In[23]:


p.x_range.end = 7500


# In[24]:


show(p)


# In[ ]:





# In[ ]:





# In[ ]:




