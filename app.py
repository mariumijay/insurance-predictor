from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import pandas as pd
import pickle

with open("model.pkl","rb") as f:
    model = pickle.load(f)

app = FastAPI()

tier_1 = [
    "Chennai",
    "Mumbai",
    "Hyderabad",
    "Delhi",
    "Pune",
    "Kolkata",
    "Bangalore"
]

tier_2 = [
    "Jaipur",
    "Indore",
    "Kota",
    "Chandigarh",
    "Lucknow",
    "Gaya",
    "Jalandhar",
    "Mysore"
]


class UserInput(BaseModel):
    age: Annotated[int, Field(...,description="Enter the age")]
    weight: Annotated[float, Field(...,description="Enter the Weight")]
    height: Annotated[float,Field(...,description="Enter the height")]
    income_lpa: Annotated[float,Field(...,description="enter the Income_LPA")]
    smoker: Annotated[bool,Field(...,description="identify the Smoker")]
    city: Annotated[str, Field(...,description="Enter the city")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
    'business_owner', 'unemployed', 'private_job'], Field(...,description="Enter the Occupation")]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "High"
        elif self.smoker or self.bmi > 27:
            return  " Medium"
        else:
            return "Low"
        
    @computed_field
    @property
    def age_group(self) -> int:
        if self.age < 25:
            return "Young"
        elif self.age > 40:
            return "Middle Age"
        elif 25 < self.age <59:
            return "Adult"
        return "Senior"
    
    @computed_field
    @property
    def city_tier(self) -> str:
        if self.city in tier_1:
            return 1
        elif self.city in tier_2:
            return 2
        else:
            return 3

@app.post("/predict")
def predict(data: UserInput):
    input = pd.DataFrame([{
        "bmi" : data.bmi,
        "age_group" : data.age_group,
        "lifestyle" : data.lifestyle_risk,
        "city_tier" : data.city_tier,
        "occupation" : data.occupation,
        "income_lpa" : data.income_lpa
    }])

    prediction = model.predict(input)[0]

    return JSONResponse(status_code=200, content={"predicted_category" : prediction})