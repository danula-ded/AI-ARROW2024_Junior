import numpy as np

# Создание одномерного массива расстояний для воскресной прогулки
distances = np.arange(2, 25, 2)

# Создание массива средних скоростей пешехода
speeds = np.full(12, 4)

# Вычисление времени в пути для каждого расстояния
times = distances / speeds

# Нахождение суммарного времени, потраченного на воскресные прогулки
total_time = np.sum(times)

# Округление времени до одного знака после запятой
total_time_rounded = round(total_time, 1)

print("Суммарное время на воскресные прогулки:", total_time_rounded)
