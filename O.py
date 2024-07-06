import pandas as pd

# Загрузка датасета
df = pd.read_csv("BlackFriday.csv")

# Взглянем на первые несколько строк датасета
print(df.head())

# Характеристики датасета
print(df.info())

# Подсчет количества ненулевых значений в столбце Product_Category_2
non_null_count = df['Product_Category_2'].count()
print("Количество ненулевых значений в столбце Product_Category_2:", non_null_count)