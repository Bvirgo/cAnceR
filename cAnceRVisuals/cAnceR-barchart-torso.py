#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap

output_file("cAnceR_TorsoCancers_Horizontal.html")
dt = pd.read_excel('/Users/ylhaart/TUNI.fi/Hanna-Riikka Rantamaa - Interaction techniques project/Data/TorsoCancers.xlsx',usecols='A,B')
dt
dt2 = dt[::-1]
dt2
names = dt2['Cancer']
names
names[31]
counts = dt2['Number']
counts
counts.max()
source = ColumnDataSource(data=dict(names=dt2['Cancer'], counts=dt2['Number']))
p = figure(y_range=names, toolbar_location=None, title="Torso Cancers")
p.hbar(y='names', right='counts', height=1.0, source=source, line_color='white', legend=None, fill_color='blue')
p.ygrid.grid_line_color = None
p.x_range.start = 0
p.x_range.end = 7500
show(p)
