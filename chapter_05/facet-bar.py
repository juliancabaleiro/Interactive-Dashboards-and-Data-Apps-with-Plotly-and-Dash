import pandas as pd
import plotly.express as px

poverty = pd.read_csv('data\poverty.csv')
gini= "GINI index (World Bank estimate)"
gini_df=poverty[poverty[gini].notna()]

countries =["Algeria","Japan","Argentina"]
df=gini_df[gini_df["Country Name"].isin(countries)].dropna(subset=[gini])

fig=px.bar(df,
       x="year",
       y=gini,
       facet_row="Country Name",
       labels={gini:"Gini Index"},
       color="Country Name",
       title="<b>".join([gini, ", ".join(countries)]),
       height=100+205*len(countries))
fig.write_html(r"chapter_05\facet-bar.html")
