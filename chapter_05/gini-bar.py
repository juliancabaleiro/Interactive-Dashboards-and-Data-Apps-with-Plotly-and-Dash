import pandas as pd
import plotly.express as px

poverty = pd.read_csv('data\poverty.csv')
series = pd.read_csv("data\PovStatsSeries.csv")
gini= "GINI index (World Bank estimate)"

#print(series.info())
print(series[series['Indicator Name']==gini]['Long definition'].values[0])
#print(poverty[gini].min(),poverty[gini].max())
#print(poverty[gini].describe())

year=2000
df=poverty[poverty['year']==year].sort_values(gini).dropna(subset=[gini])
n_countries=len(df["Country Name"])
fig=px.bar(df,
       x="Country Name",
       y=gini,
       title=" - ".join([gini,str(year)]),
       height=200+20*n_countries,
       orientation='h')
fig.write_html(r"chapter_05\bar.html")