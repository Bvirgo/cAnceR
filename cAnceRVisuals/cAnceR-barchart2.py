#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd


# In[100]:


import numpy as np


# In[101]:


from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap


# In[102]:


output_file("cAnceR_HeadCancers_Horizontal.html")


# In[103]:


dt = pd.read_excel('/Users/ylhaart/TUNI.fi/Hanna-Riikka Rantamaa - Interaction techniques project/Data/HeadCancers.xlsx',usecols='A,B')


# In[104]:


dt


# In[105]:


dt2 = dt[::-1]


# In[106]:


dt2


# In[107]:


names = dt2['Cancer']


# In[108]:


names


# In[109]:


names[11]


# In[110]:


counts = dt2['Number']


# In[111]:


counts


# In[112]:


counts.max()


# In[113]:


source = ColumnDataSource(data=dict(names=dt2['Cancer'], counts=dt2['Number']))


# In[114]:


p = figure(y_range=names, toolbar_location=None, title="Head Cancers")


# In[115]:


p.hbar(y='names', right='counts', height=0.5, source=source, line_color='white', legend=None, fill_color='darkturquoise')


# In[116]:


p.ygrid.grid_line_color = None


# In[117]:


p.x_range.start = 0


# In[118]:


p.x_range.end = 1150


# In[119]:


show(p)


# In[ ]:





# In[ ]:





# In[ ]:




