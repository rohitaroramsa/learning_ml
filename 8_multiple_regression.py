import pandas
from sklearn import linear_model

df = pandas.read_csv("data\\data.csv")
# df.columns = ['Car', 'Model', 'Volume', 'Weight', 'CO2']
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[2300, 1300]])
print('Predicted value for CO2 is: {}'.format(predictedCO2[0]))
