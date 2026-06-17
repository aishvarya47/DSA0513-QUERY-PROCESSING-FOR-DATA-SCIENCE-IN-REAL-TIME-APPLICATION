import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date':['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05'],
    'Volume':[1000000,1200000,1400000,1300000,1500000]
}

df = pd.DataFrame(data)

plt.bar(df['Date'], df['Volume'])
plt.title("Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()
