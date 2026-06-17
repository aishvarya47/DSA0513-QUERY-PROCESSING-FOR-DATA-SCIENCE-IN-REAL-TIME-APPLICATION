import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date':['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05'],
    'Close':[103,107,109,111,114]
}

df = pd.DataFrame(data)

plt.plot(df['Date'], df['Close'])
plt.title("Alphabet Stock Prices")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()
