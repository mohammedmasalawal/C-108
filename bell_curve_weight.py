import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],
                       show_hist=False)
fig.show()