import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, TapTool, OpenURL

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
        website=["https://yle.fi/uutiset", "https://areena.yle.fi/tv", "https://yle.fi/urheilu", "https://yle.fi/saa/", "https://yle.fi/saa/artikkelit/", "https://yle.fi/uutiset/3-8045550", "https://yle.fi/uutiset/tuoreimmat", "https://yle.fi/uutiset/18-220306", "https://yle.fi/uutiset/18-204933", "https://yle.fi/uutiset/18-34953", "https://yle.fi/uutiset/18-34837", "https://vastuullistajournalismia.fi/"]
        ))

fig2 = figure(plot_width=600, plot_height=600, y_range=names, tools="tap", toolbar_location=None, title="Head Cancers")
fig2.hbar(y='names', right='counts', height=0.5, source=source, line_color='white', legend=None, fill_color='darkturquoise')
fig2.ygrid.grid_line_color = None
fig2.x_range.start = 0
fig2.x_range.end = 1150

url = "@website"
taptool = fig2.select(type=TapTool)
taptool.callback = OpenURL(url=url)



#
# Create html file for diagram
#

output_file("head-bar-chart.html")

# Plot the two visualizations in a horizontal configuration
show(fig2)