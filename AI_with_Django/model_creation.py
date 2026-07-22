import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv('house_price.csv')
# print(df.head())
x=df[['Area','Bedrooms','Bathrooms','Age']]
# print(x)
y=df['Price']
# print(y)
model=LinearRegression()
model.fit(x,y)
print([f"{coefficient:.2f}" for coefficient in model.coef_])
print(f"{model.intercept_:.2f}")

joblib.dump(model, 'house_model.pkl')