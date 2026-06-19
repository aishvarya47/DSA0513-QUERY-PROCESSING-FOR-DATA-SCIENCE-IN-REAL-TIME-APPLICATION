import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date':['10-03-16','10-04-16','10-05-16','10-06-16','10-07-16'],
    'Open':[774.25,776.03,779.30,779.00,779.65],
    'Close':[772.55,776.42,776.46,776.85,775.08]
}

df = pd.DataFrame(data)

plt.plot(df['Date'],df['Open'],label='Open')
plt.plot(df['Date'],df['Close'],label='Close')

plt.legend()
plt.show()
