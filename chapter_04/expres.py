import plotly.express as px
gapminder=px.data.gapminder()
print(gapminder.info())
print(gapminder)

fig=px.scatter(data_frame=gapminder,
           x="gdpPercap",
           y="lifeExp",
           size="pop",
           facet_col="continent",
           color="continent",
           title="Life expectancy and GDP per capita 1952 - 2007",
           labels={"gdpPercap":"GDP per Capita",
                   "lifeExp":"Life Expentancy"},
            log_x=True,
            range_y=[20,100],
            hover_name="country",
            animation_frame="year",
            height=600,
            size_max=90)

fig.write_html("chapter_04\expres.html")