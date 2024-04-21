import plotly.graph_objects as go

fig = go.Figure()

fig.add_scatter(x=[1,2,3],y=[4,2,3])
fig.add_scatter(x=[1,2,3,4], y=[4,5,2,3])

fig.layout.title="titulo"
fig.layout.xaxis.title="eje x"
fig.layout.yaxis.title="eje y"
fig.write_html("html_plot.html",
               config={"ToImageButtonOptions":{"format":"svg"}})

fig.show(config={"displaylogo":False,
                 "modeBarButtonsToAdd":["drawrect",
                                        "drawcircle",
                                        "eraseshape"]})