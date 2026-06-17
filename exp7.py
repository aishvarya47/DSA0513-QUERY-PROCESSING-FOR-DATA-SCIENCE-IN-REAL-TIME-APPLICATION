import pandas as pd

data = {
    'Item':['Television','Home Theater','Television','Cell Phone','Home Theater'],
    'Sale_amt':[113810,25000,43128,6075,30000]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(
    df,
    values='Sale_amt',
    index='Item',
    aggfunc=['min','max']
)

print(pivot)
