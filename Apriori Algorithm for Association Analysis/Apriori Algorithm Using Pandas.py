import pandas as pd
from collections import Counter

data = pd.read_csv('1.csv')
l=data.groupby('order_id')['product_id'].apply(list).tolist()

c=Counter(tuple(x) for x in iter(l))
for x in c:
    if c[x]>10:
        print(x," : ",c[x])