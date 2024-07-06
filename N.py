from sklearn.manifold import TSNE
from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
irises = load_iris()
X= irises.data
markers=irises.target
transformer = TSNE(n_components=2, random_state=2)
X_gauss = transformer.fit_transform(X)
plt.scatter(X_gauss[:,0], X_gauss[:,1],c=markers) 
plt.show()