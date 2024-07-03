from sklearn import datasets
from sklearn import random_projection

# Загрузка датасета для примера
iris = datasets.load_iris()
X = iris.data

# Использование метода GaussianRandomProjection с измененным значением параметра eps
transformer = random_projection.GaussianRandomProjection(eps=0.1, random_state=2)
X_new = transformer.fit_transform(X)

print("Размерность X после преобразования:", X_new.shape)