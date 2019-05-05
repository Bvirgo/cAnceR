import matplotlib.pyplot as plt
from numpy import pi, linspace, sin, cos, tan
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

#
# Create the first diagram. Scatter plot.
#

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
            
            # create a new plot with a range set with a tuple
            fig1 = figure(plot_width=900, toolbar_location=None, plot_height=400, x_range=(["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"]))
            # set a range using a Range1d
            fig1.y_range = Range1d(0, 350)            
            fig1.circle([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5], [b, c, d, e, f, g, h, i, j, k, l, m, n, o, x, q, r, a], size=10)
            # Format the tooltip
            tooltips = [
                ("value", " @y")
            ]
            # Add the HoverTool to the figure
            fig1.add_tools(HoverTool(tooltips=tooltips))
            line_count = line_count + 1
        else:
            line_count = line_count + 1


#
# Create the second diagram. Bar chart.
#

dt = pd.read_excel('HeadCancersCopy.xlsx',usecols='A,B')
dt2 = dt[::-1]
names = dt2['Cancer']
names[11]
counts = dt2['Number']
counts.max()
source = ColumnDataSource(data=dict(names=dt2['Cancer'], counts=dt2['Number']))

fig2 = figure(plot_width=600, plot_height=600, y_range=names, tools="tap", toolbar_location=None, title="Head Cancers")
fig2.hbar(y='names', right='counts', height=0.5, source=source, line_color='white', legend=None, fill_color='darkturquoise')
fig2.ygrid.grid_line_color = None
fig2.x_range.start = 0
fig2.x_range.end = 1150


#
# Create html file for diagrams
#

output_file("multiple.html")

# Configure the gridplot to get the diagrams horisontally
both_diagrams_gridplot = gridplot([[fig2, fig1]], 
                              toolbar_location='right')

#***tabbing multiple diagrams***#

# Increase the plot widths
fig1.plot_width = fig2.plot_width = 800

# Create two panels, one for each conference
east_panel = Panel(child=fig1, title='Eastern Conference')
west_panel = Panel(child=fig2, title='Western Conference')

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

# Show the tabbed layout
show(tabs)

