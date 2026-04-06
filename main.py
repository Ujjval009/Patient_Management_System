from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel ,computed_field , Field 
from typing import Annotated , Literal , Optional
import json

app = FastAPI() 



class Patient(BaseModel):
    id: Annotated[str, Field(..., description="The ID of the patient  in the DB", example="P001")]
    name: Annotated[str, Field(..., description="The name of the patient")]
    city: Annotated[str, Field(..., description="The city of the patient")]
    age: Annotated[int, Field(..., description="The age of the patient", gt=0, lt=120)]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="The gender of the patient")]
    height: Annotated[float, Field(..., description="The height of the patient in mtrs", gt=0)]
    weight: Annotated[float, Field(..., description="The weight of the patient in kgs", gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
        return bmi



    @computed_field
    @property
    def verdict(self) -> str:
        
        if self.bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= self.bmi < 25:
            return 'Normal weight'
        elif 25 <= self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'  


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
    



def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)

#HOME ROUTE

@app.get("/")
def hello():
    return {'message': 'Patient Management System!'}



#ABOUT ROUTE
@app.get('/about')
def about():
    return {'message': 'A fully functional patient management system built with FastAPI.'}



#VIEW ALL THE PATIENTS IN THE DB
@app.get('/view')
def view():
    data = load_data() 
    return data



#VIEW A PARTICULAR PATIENT IN THE DB
@app.get('/patient/{patient_id}')  
def view_patient(patient_id: str = Path(..., description="The ID of the patient  in the DB", examples={"example": {"value": "P001"}})):
    #load all the patient
    data = load_data() 

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")



#SORT THE PATIENTS IN THE DB ON THE BASIS OF HEIGHT, WEIGHT OR BMI IN ASCENDING OR DESCENDING ORDER
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data  

@app.post('/create')
def create_patient(patient: Patient):

    #load existing data
    data = load_data()


    #check if patient id already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient with this ID already exists')


    #if not create a new patient and save to the DB
    data[patient.id] = patient.model_dump(exclude=['id'])  # Convert the Pydantic model to a dictionary

    # save the updated data back to the JSON file
    save_data(data)
    
    return JSONResponse(content={"message": "Patient created successfully", "patient_id": patient.id}, status_code=201)



@app.put("/patient/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})
    

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)   
    

    return JSONResponse(status_code=200, content={'message':'patient deleted'})




