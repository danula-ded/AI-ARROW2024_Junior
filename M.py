import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.random_projection import GaussianRandomProjection

# Загрузка датасета
iris = load_iris()
X = iris.data
y = iris.target

# Применение метода случайных проекций
rp = GaussianRandomProjection(random_state=2)
X_rp = rp.fit_transform(X)

# Отображение облака точек на плоскости
plt.scatter(X_rp[:, 0], X_rp[:, 1], c=y)
plt.show()