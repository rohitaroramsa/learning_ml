import pandas
from sklearn import linear_model
import requests


def download_csv_data():
    response=requests.get(url)
    if response.status_code==200:
        with open(csv_file, 'wb') as file:
            file.write(response.content)


def perform_regression():
    df = pandas.read_csv(csv_file)
    X = df[['Weight', 'Volume']]
    y = df['CO2']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    predictedCO2 = regr.predict([[2300, 1300]])
    print('Predicted value for CO2 is: {}'.format(predictedCO2[0]))


if __name__ == '__main__':
    url = 'https://www.w3schools.com/python/data.csv'
    csv_file = 'data\\data.csv'
    download_csv_data()
    perform_regression()
