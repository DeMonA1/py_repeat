import pandas


data = pandas.read_csv('villains')
print(data)

dates = pandas.date_range('2024-01-01', periods=3, freq='MS')
dates