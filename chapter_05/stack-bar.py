import plotly.express as px
import pandas as pd
import re

poverty = pd.read_csv('data\poverty.csv')
income_share_df=poverty.filter(regex="Country Name|^year$|Income share.*?20").dropna()

income_share_df = income_share_df.rename(columns={
    'Income share held by lowest 20%': '1 Income share held by lowest 20%',    
    'Income share held by second 20%': '2 Income share held by second 20%',    
    'Income share held by third 20%': '3 Income share held by third 20%',    
    'Income share held by fourth 20%': '4 Income share held by fourth 20%',    
    'Income share held by highest 20%': '5 Income share held by highest 20%'
    }).sort_index(axis=1)

income_share_df.columns=[re.sub("\d Income share held by ", "",col).title()
                         for col in income_share_df.columns]
income_share_cols=income_share_df.columns[:-2]

country="Indonesia"
fig=px.bar(income_share_df[income_share_df["Country Name"]==country].dropna(),
           x=income_share_cols,
           y="Year",
           hover_name="Country Name",
           orientation="h",
           barmode="stack",
           height=600,
           title=f"Income Share Quintiles - {country}")
fig.layout.legend.orientation="h"
fig.layout.legend.title=None
fig.layout.legend.title="Percent of Total Income"
fig.layout.legend.x=0.25
fig.write_html("chapter_05\stack-bar.html")