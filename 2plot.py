import plotly.express as px
import pandas as pd

df = pd.read_csv('df.csv')

fig = px.bar(df, x="singer", y="count",
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
fig.show()