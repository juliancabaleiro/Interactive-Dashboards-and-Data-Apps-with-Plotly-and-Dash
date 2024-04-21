import pandas as pd
import plotly.express as px

poverty = pd.read_csv('data\poverty.csv')
series = pd.read_csv("data\PovStatsSeries.csv")
gini= "GINI index (World Bank estimate)"

country="Sweden"
df=poverty[poverty["Country Name"]==country].dropna(subset=gini)

fig=px.bar(df,
           x="year",
           y=gini,
           title=" - ".join([gini,country])
)
fig.write_html(r"chapter_05\bar2.html")