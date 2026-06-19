import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,25,30]
y2 = [30,25,20,10]

plt.subplot(1,2,1)
plt.plot(x,y1)

plt.subplot(1,2,2)
plt.plot(x,y2)

plt.show()
