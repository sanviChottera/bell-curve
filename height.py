import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')

#x =  df["Weight(Pounds)"].tolist()
#fig = ff.create_distplot( [df["Weight(Pounds)"].tolist()],   ["Weight of students"] , show_hist=False)

x =  df["Height(Inches)"].tolist()
fig = ff.create_distplot( [df["Height(Inches)"].tolist()],   ["Height of students"] , show_hist=False)



fig.show()