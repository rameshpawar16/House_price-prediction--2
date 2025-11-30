from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score,mean_absolute_error
import pandas as pd
import numpy as np

class HousePrice:
    def __init__(self):
        self.lr = LinearRegression()
    
    def model(self):
        data = pd.read_csv("data/train.csv")
        x = data.iloc[:,:-1]
        y = data.iloc[:,-1]
        
        self.lr.fit(x,y)
        print("model successfully fit")
        
    def predict(self,sqft,bed,bath,age):
        new_data = pd.DataFrame([{
            "square_feet": sqft,   
            "bedrooms": bed,        
            "bathrooms": bath,      
            "age": age              
        }])
        return self.lr.predict(new_data)[0]
    
    def _evaluate_on_file(self, path: str):
        data = pd.read_csv(path)
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        preds = self.lr.predict(X)

        r2 = r2_score(y, preds)
        mae = mean_absolute_error(y, preds)

        return {"r2": r2, "mae": mae}
    def evaluate_on_validation(self):
        return self._evaluate_on_file("data/valid.csv")

    def evaluate_on_test(self):
        return self._evaluate_on_file("data/test.csv")