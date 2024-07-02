# Чтение входных данных
costs = list(map(float, input().split()))
sales = list(map(float, input().split()))

# Вычисление прибыли
profits = [round(sales[i] - costs[i], 2) for i in range(len(costs))]

# Форматированный вывод результатов
print(' '.join(f'{profit:.2f}' for profit in profits))
