import matplotlib.pyplot as plt

# Данные о количестве шагов
steps = np.array([6236, 10260, 6667, 7389, 7455, 8886, 7846, 9101, 10101, 7818, 
                  11472, 10870, 10801, 8012, 15930, 7281, 8083, 8695, 17941, 
                  14102, 11732, 18238, 20010, 10143, 15622, 21118, 13321, 
                  16856, 12371, 13911])

# Вычисляем кумулятивные средние
cumulative_means = np.cumsum(steps) / np.arange(1, len(steps) + 1)

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(np.arange(1, len(steps) + 1), cumulative_means, marker='o', linestyle='-', color='b')
plt.title('Кумулятивные средние шагов за месяц')
plt.xlabel('День')
plt.ylabel('Кумулятивное среднее')
plt.grid(True)
plt.show()
