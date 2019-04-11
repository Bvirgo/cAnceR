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

#open .csv file
with open('plotData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in readCSV:
        #here we check only the line with the wanted cancer type
        if (line_count == 4):
            #here we create the plot chart with wanted cancer type and the right values.
            b=float(row[2].split(";")[0])
            c=float(row[3].split(";")[0])
            d=float(row[4].split(";")[0])
            e=float(row[5].split(";")[0])
            f=float(row[6].split(";")[0])
            g=float(row[7].split(";")[0])
            h=float(row[8].split(";")[0])
            i=float(row[9].split(";")[0])
            j=float(row[10].split(";")[0])
            k=float(row[11].split(";")[0])
            l=float(row[12].split(";")[0])
            m=float(row[13].split(";")[0])
            n=float(row[14].split(";")[0])
            o=float(row[15].split(";")[0])
            p=float(row[16].split(";")[0])
            q=float(row[17].split(";")[0])
            r=float(row[18].split(";")[0])
            a=float(row[19].split(";")[0])
            
            output_file("title.html")
            # create a new plot with a range set with a tuple
            p = figure(plot_width=900, plot_height=400, x_range=(["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"]))
            # set a range using a Range1d
            p.y_range = Range1d(0, 3000)


            #seuraavaksi vielä tehtävä luuppi joka tarkistaa kaikki taulukon arvot a-r ja jos 
            #arvo on alle 1 niin muuttaa sen 1 jotta se näkyy taulukossa
            

            p.circle([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5], [b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, a], size=10)

            show(p)
            line_count = line_count + 1
        else:
            line_count = line_count + 1
