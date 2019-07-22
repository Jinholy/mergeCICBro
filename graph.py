import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


data = pd.read_csv("/home/hott/honeypot/mergeCICBro/csv/bro.csv")

print(data.head())

df = nx.from_pandas_edgelist(data, source='ts', target ='proto', edge_attr=True)
#print(df.nodes())

plt.figure(figsize=(12,8))
nx.draw_networkx(df, with_labels=True)
plt.show()