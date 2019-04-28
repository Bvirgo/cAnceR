# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:23:45 2019
"""

import csv
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from bokeh.models import HoverTool


#open .csv file
with open('age_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in readCSV:
        #here we check only the line with the wanted cancer type
        if (line_count == 1):
            #here we create the plot chart with wanted cancer type and the right values.
            b=float(row[0].split(";")[1])
            c=float(row[0].split(";")[2])
            d=float(row[0].split(";")[3])
            e=float(row[0].split(";")[4])
            f=float(row[0].split(";")[5])
            g=float(row[0].split(";")[6])
            h=float(row[0].split(";")[7])
            i=float(row[0].split(";")[8])
            j=float(row[0].split(";")[9])
            k=float(row[0].split(";")[10])
            l=float(row[0].split(";")[11])
            m=float(row[0].split(";")[12])
            n=float(row[0].split(";")[13])
            o=float(row[0].split(";")[14])
            x=float(row[0].split(";")[15])
            q=float(row[0].split(";")[16])
            r=float(row[0].split(";")[17])
            a=float(row[0].split(";")[18])
                
            output_file("Adrenal_gland.html")
            # create a new plot with a range set with a tuple
            p = figure(plot_width=900, plot_height=400, x_range=(["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"]))
            # set a range using a Range1d
            p.y_range = Range1d(0, 350)            
            p.circle([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5], [b, c, d, e, f, g, h, i, j, k, l, m, n, o, x, q, r, a], size=10)
            # Format the tooltip
            tooltips = [
                ("value", " @y")
            ]
            # Add the HoverTool to the figure
            p.add_tools(HoverTool(tooltips=tooltips))
            show(p)
            line_count = line_count + 1
        else:
            line_count = line_count + 1
