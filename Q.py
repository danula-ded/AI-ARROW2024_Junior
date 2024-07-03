import pandas as pd

# Загрузка датасета
df = pd.read_csv('Students_Performance.csv')

# Группировка данных и вычисление среднего балла математики для бакалавров
bachelors_math_score = df[df['parental level of education'] == "bachelor's degree"]['math score'].mean()

# Вывод среднего балла математики у бакалавров
print(round(bachelors_math_score, 6))
