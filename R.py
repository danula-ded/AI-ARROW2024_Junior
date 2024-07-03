import pandas as pd
import sklearn
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression, Lasso, Ridge
data = pd.read_csv("Fish.csv")
data.drop("Species", axis=1, inplace=True)
y = data['Weight']
data.drop("Weight", axis=1, inplace=True)
x_train, x_test = data[:111], data[111:]
y_train, y_test = y[:111], y[111:]
lr = LinearRegression()
lr.fit(x_train, y_train)
#print(lr.coef_, lr.intercept_)
print(round(lr.intercept_, 4))
y_pred = lr.predict(x_test)
#print(y_pred)
mean_absolute_error(y_test, y_pred)