import plotly.express as px
import pandas as pd

df = pd.read_csv('df.csv')

fig = px.bar(df, x="singer", y="count", title='Count of Singers')
#fig.update_traces(contours_coloring="fill", contours_showlabels = True)
fig.show()