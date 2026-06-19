import pandas as pd

data = {
    'Year':[1986,1987,1989],
    'WHO Region':['Africa','Americas','Europe'],
    'Country':['Algeria','Canada','France'],
    'Beverage Types':['Wine','Beer','Spirits'],
    'Display Value':[0.5,2.0,1.8]
}

df = pd.DataFrame(data)

print("Shape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)
