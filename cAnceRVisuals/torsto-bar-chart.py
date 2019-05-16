import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, TapTool, OpenURL

dt = pd.read_excel('TorsoCancers.xlsx',usecols='A,B')
dt2 = dt[::-1]
names = dt2['Cancer']
names[31]
counts = dt2['Number']
counts.max()
source = ColumnDataSource(data=dict(
        names=dt2['Cancer'], 
        counts=dt2['Number'],
        website=["https://areee.github.io/cAnceR/visualisoinnit/ureter.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/testis.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/stomach.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/smallintestine.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/retroperitoneumandperitoneum.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/renalpelvis.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/rectumandanus.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/rectum.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/prostate.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/pharynx.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/penis.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/pancreas.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/ovary.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/otherthoracicorgans.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/otherpharynx.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/othermalegenitalorgans.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/otherfemalegenitalorgans.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/oesophagus.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/mesothelioma.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/lung.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/liverandintrahepticbileducts.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/kidneyrenalpelvisandureter.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/kidney.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/gallbladderandbiliarytract.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/corpusuteriandunspecifieduterus.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/colonrectumandanus.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/colon.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/cervixuteri.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/breastfemale.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/bladder.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/anus.html",
                 "https://areee.github.io/cAnceR/visualisoinnit/Adrenal_gland.html"]
        ))

fig = figure(plot_width=600, plot_height=750, y_range=names, tools="pan, tap", toolabar_location=None, title="Torso area Cancers")
fig.hbar(y='names', right='counts', height=0.8, source=source, line_color='white', legend=None, fill_color='blue')
fig.ygrid.grid_line_color = None
fig.x_range.start = 0
fig.x_range.end = 7500

url = "@website"
taptool = fig.select(type=TapTool)
taptool.callback = OpenURL(url=url)


#
# Create html file for diagram
#

output_file("torso-bar-chart.html")
show(fig)
