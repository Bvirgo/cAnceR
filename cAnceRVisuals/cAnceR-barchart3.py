#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[7]:


from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap


# In[8]:


output_file("cAnceR_OtherCancers_Horizontal.html")


# In[9]:


dt = pd.read_excel('/Users/ylhaart/TUNI.fi/Hanna-Riikka Rantamaa - Interaction techniques project/Data/OtherCancers.xlsx',usecols='A,B')


# In[10]:


dt


# In[11]:


dt2 = dt[::-1]


# In[12]:


dt2


# In[13]:


names = dt2['Cancer']


# In[14]:


names


# In[15]:


names[12]


# In[16]:


counts = dt2['Number']


# In[22]:


counts


# In[23]:


counts.max()


# In[24]:


source = ColumnDataSource(data=dict(names=dt2['Cancer'], counts=dt2['Number']))


# In[25]:


p = figure(y_range=names, toolbar_location=None, title="Other Cancers")


# In[27]:


p.hbar(y='names', right='counts', height=0.5, source=source, line_color='white', legend=None, fill_color='darkblue')


# In[28]:


p.ygrid.grid_line_color = None


# In[29]:


p.x_range.start = 0


# In[30]:


p.x_range.end = 1300


# In[31]:


show(p)


# In[ ]:





# In[ ]:





# In[ ]:




