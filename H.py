import numpy as np

# Данные о количестве шагов
steps = np.array([6236, 10260, 6667, 7389, 7455, 8886, 7846, 9101, 10101, 7818, 
                  11472, 10870, 10801, 8012, 15930, 7281, 8083, 8695, 17941, 
                  14102, 11732, 18238, 20010, 10143, 15622, 21118, 13321, 
                  16856, 12371, 13911])

# Вычисляем кумулятивные средние
cumulative_means = np.cumsum(steps) / np.arange(1, len(steps) + 1)

# Отбираем каждое седьмое значение
selected_values = cumulative_means[6::7]

# Округляем до сотых
rounded_values = np.round(selected_values, 2)

# Формируем строку для вывода
result_string = ' '.join(map(str, rounded_values))

print(result_string)
