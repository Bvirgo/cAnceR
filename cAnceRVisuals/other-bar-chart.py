import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, TapTool, OpenURL

dt = pd.read_excel('OtherCancers.xlsx',usecols='A,B')
dt2 = dt[::-1]
names = dt2['Cancer']
names[12]
counts = dt2['Number']
counts.max()
source = ColumnDataSource(data=dict(
        names=dt2['Cancer'], 
        counts=dt2['Number'],
        website=["https://areee.github.io/cAnceR/visualisoinnit/softtissue.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/primarysiteunknown.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/otherleukemias.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/otherendocrineglands.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/nonhodkinlymphoma.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/myeloma.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/myeloidandmonocyticleukemia.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/melanomaoftheskin.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/lymphocyticleukemia.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/leukemia.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/kaposisarcoma.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/endocrine.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/bonesandjoints.html"]
        ))

fig = figure(y_range=names, tools="pan, tap", toolbar_location=None, title="Cancers in other body parts")
fig.hbar(y='names', right='counts', height=0.5, source=source, line_color='white', legend=None, fill_color='darkblue')
fig.ygrid.grid_line_color = None
fig.x_range.start = 0
fig.x_range.end = 1300

url = "@website"
taptool = fig.select(type=TapTool)
taptool.callback = OpenURL(url=url)


#
# Create html file for diagram
#

output_file("other-bar-chart.html")
show(fig)
