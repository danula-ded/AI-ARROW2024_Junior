import pandas as pd

# Загрузка данных из файла BlackFriday.csv
df = pd.read_csv('BlackFriday.csv')

# Подсчет количества пустых значений во всем датасете
total_missing_values = df.isnull().sum().sum()

print(total_missing_values)