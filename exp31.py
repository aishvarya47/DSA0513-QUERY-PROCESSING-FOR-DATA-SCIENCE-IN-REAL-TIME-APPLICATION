import matplotlib.pyplot as plt
import numpy as np

menMeans = (22,30,35,35,26)
womenMeans = (25,32,30,35,29)

menStd = (4,3,4,1,5)
womenStd = (3,5,2,3,3)

ind = np.arange(5)

plt.bar(ind, menMeans, yerr=menStd)
plt.bar(ind, womenMeans, bottom=menMeans, yerr=womenStd)

plt.show()
