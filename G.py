# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    costs = list(map(float, file.readline().split()))
    revenues = list(map(float, file.readline().split()))

# Вычисление ежемесячной прибыли
profits = [revenue - cost for cost, revenue in zip(costs, revenues)]

# Запись результатов в файл
with open('output.txt', 'w') as file:
    file.write(' '.join([f'{profit:.2f}' for profit in profits]))