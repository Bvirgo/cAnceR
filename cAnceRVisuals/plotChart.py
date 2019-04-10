# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:23:45 2019
"""

import csv
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show

#open .csv file
with open('plotData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in readCSV:
        #here we check only the line with the wanted cancer type
        if (line_count == 4):
            #here we create the plot chart with wanted cancer type and the right values.
            print(row[2].split(";")[0])
            line_count = line_count + 1
        else:
            line_count = line_count + 1

     
            #num = int(float(row[0].split(";")[]))
          