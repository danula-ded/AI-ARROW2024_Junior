import numpy as np
import matplotlib.pyplot as plt

steps = np.array([6236, 10260, 6667, 7389, 7455, 8886, 7846, 9101, 10101, 7818, 11472, 10870, 10801, 8012, 15930, 7281, 8083, 8695, 17941, 14102, 11732, 18238, 20010, 10143, 15622, 21118, 13321, 16856, 12371, 13911])

cumulative_means = [np.round(np.mean(steps[:i+1]), 2) for i in range(len(steps))]

plt.figure(figsize=(12, 6))
plt.plot(range(1, len(steps)+1), cumulative_means, marker='o', color='b', linestyle='-')
plt.title("Кумулятивное среднее количество шагов за месяц")
plt.xlabel("День")
plt.ylabel("Среднее количество шагов")
plt.grid(True)
plt.show()

# Find the days with the most significant decrease in activity
max_drop_start = 0
max_drop_end = 0
max_drop_amount = 0

for i in range(1, len(cumulative_means)):
    drop_amount = cumulative_means[i-1] - cumulative_means[i]
    if drop_amount > max_drop_amount:
        max_drop_amount = drop_amount
        max_drop_start = i - 1
        max_drop_end = i

print(max_drop_start + 1, max_drop_end)