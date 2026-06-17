import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Volume':[1000000,1200000,1400000,1300000,1500000],
    'Close':[103,107,109,111,114]
}

df = pd.DataFrame(data)

plt.scatter(df['Volume'], df['Close'])
plt.title("Volume vs Close Price")
plt.xlabel("Volume")
plt.ylabel("Close Price")
plt.show()
