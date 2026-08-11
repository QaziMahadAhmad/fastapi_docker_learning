from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:    str 
    email:   EmailStr
    linkedin_url: AnyUrl
    age:     int
    weight:  float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str , str] 

    @computed_field
    @property
    
    def bmi(self) -> float:
        return round(self.weight / (self.height**2))


def insert_patient_data(self: Patient):
    print(self.name)
    print(self.age)
    print(self.weight)
    print(self.height)
    print(self.bmi)
    print(self.married)
    print(self.allergies)
    print(self.contact_details)
    print("Inserted")


patient_info = {'name' : 'mahad','email': 'qazimahad07@hdfc.com','linkedin_url':'http://linked.com/12', 'age' : 20, 'weight' : 74.3, 'height' : 1.72, 'married' : False, 'allergies' : ['pollen', 'flue'], 
                'contact_details': {'phone': '03238724496'}}

p1 = Patient(**patient_info)

insert_patient_data(p1)