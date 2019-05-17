import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, TapTool, OpenURL, HoverTool

#
# Create a scatter plot diagram 
#

dt = pd.read_excel('HeadCancersCopy.xlsx',usecols='A,B')
dt2 = dt[::-1]
names = dt2['Cancer']
names[11]
counts = dt2['Number']
counts.max()
source = ColumnDataSource(data=dict(
        names=dt2['Cancer'], 
        counts=dt2['Number'], 
        website=["https://areee.github.io/cAnceR/visualisoinnit/tongue.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/thyroidgland.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/salivaryglands.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/nasopharynx.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/nasalcavityandsinuses.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/mouth.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/liporalcavityandpharynx.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/lip.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/larynx.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/hodgkinslymphoma.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/eyeandadnexa.html", 
                 "https://areee.github.io/cAnceR/visualisoinnit/brainandotherCNS.html"]
        ))

fig2 = figure(plot_width=600, plot_height=600, y_range=names, tools="tap, pan", toolbar_location=None, title="Head area Cancers")
fig2.hbar(y='names', right='counts', height=0.5, source=source, line_color='white', legend=None, fill_color='darkturquoise', hover_line_color='black')
fig2.ygrid.grid_line_color = None
fig2.x_range.start = 0
fig2.x_range.end = 1150

url = "@website"
taptool = fig2.select(type=TapTool)
taptool.callback = OpenURL(url=url)

# Format the tooltip
fig2.add_tools(HoverTool(tooltips=None))

#
# Create html file for diagram
#

output_file("head-bar-chart.html")

# Plot the two visualizations in a horizontal configuration
show(fig2)
