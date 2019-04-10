#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show

output_file("cAnceR_plotchart1.html")
dt = pd.read_excel('/Users/ylhaart/TUNI.fi/Hanna-Riikka Rantamaa - Interaction techniques project/Data/Age_specific_incidence_by_cancer.xlsx', usecols='A:S',skiprows=0,nrows=1)
dt
dt['Cancer']
dt['0-4']
