import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Загрузка данных
data = pd.read_csv('Fish.csv')

# Удаление столбца с текстовыми данными
data = data.drop('Species', axis=1)

# Выделение целевого столбца
y = data['Weight']
X = data.drop('Weight', axis=1)

# Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели линейной регрессии
lr = LinearRegression()
lr.fit(X_train, y_train)

# Вывод коэффициентов линейной регрессии
print(lr.coef_, lr.intercept_)

# Для решения задачи В поле ввода внесите значение lr.intercept_ до 4 знака после запятой включительно.
print(f"В поле ввода внесите значение lr.intercept_ до 4 знака после запятой включительно: {lr.intercept_:.4f}")