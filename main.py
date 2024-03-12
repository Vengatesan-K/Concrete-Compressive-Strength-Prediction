from fastapi import FastAPI, Request
from pydantic import BaseModel
import numpy as np
import pickle
from joblib import load
app = FastAPI()

regressor = load('C:/Users/VENKA/Desktop/Data Science/Project/concrete/notebook/model.pkl')

# Create a new StandardScaler instance)

class Strength(BaseModel):
    Age: float
    Fly_Ash: float
    Average_Aggregate: float
    Water_Cement_Ratio: float
    Blast_Furnace_Slag: float
    Super_Plasticizer: float

@app.post('/predict')
async def predict_data(request: Request, data: Strength):
    data_dict = data.dict()
    print(data_dict)
    
    Age = data_dict['Age']
    Fly_Ash = data_dict['Fly_Ash']
    Average_Aggregate = data_dict['Average_Aggregate']
    Water_Cement_Ratio = data_dict['Water_Cement_Ratio']
    Blast_Furnace_Slag = data_dict['Blast_Furnace_Slag']
    Super_Plasticizer = data_dict['Super_Plasticizer']
    
    pred_array = np.array([[Age, Fly_Ash, Average_Aggregate, Water_Cement_Ratio, Blast_Furnace_Slag, Super_Plasticizer]])
    results = regressor.predict(pred_array)
    
    return {"results": results[0]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
