import matplotlib.pyplot as plt

group1_height = [150, 155, 160, 165]
group1_weight = [50, 55, 60, 65]

group2_height = [145, 150, 155, 160]
group2_weight = [45, 50, 55, 58]

group3_height = [160, 165, 170, 175]
group3_weight = [65, 70, 75, 80]

plt.scatter(group1_height, group1_weight, label='Group 1')
plt.scatter(group2_height, group2_weight, label='Group 2')
plt.scatter(group3_height, group3_weight, label='Group 3')

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.legend()

plt.show()
