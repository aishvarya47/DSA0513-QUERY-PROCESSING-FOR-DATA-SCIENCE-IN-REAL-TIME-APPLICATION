import matplotlib.pyplot as plt
import numpy as np

men = (22,30,35,35,26)
women = (25,32,30,35,29)

x = np.arange(len(men))
width = 0.35

plt.bar(x, men, width, label='Men')
plt.bar(x+width, women, width, label='Women')

plt.legend()
plt.show()
