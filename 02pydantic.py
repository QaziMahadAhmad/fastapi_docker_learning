from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:    str = Annotated[str, Field(max_length=50, title= 'Name of the patient', description= 'Give the name of the patient in less than 50 char', examples= ['Mahad','Fahad'])]
    email:   EmailStr
    linkedin_url: AnyUrl
    age:     int = Field(gt = 6 ,lt = 100)
    weight:  float = Field(gt = 0)
    married: bool
    allergies: Optional[List[str]] = None    # Optional is optional like if someone gives empty then its will point to None 
    contact_details: Dict[str , str]


def insert_patient_data(self: Patient):
    print(self.name)
    print(self.age)
    print(self.weight)
    print(self.married)
    print(self.allergies)
    print(self.contact_details)

    print("Inserted")

def update_patient_data(self: Patient):
    print(self.name)
    print(self.age)
    print("updated")

patient_info = {'name' : 'mahad','email': 'qazimahad07@gmail.com','linkedin_url':'http://linked.com/12', 'age' : 20, 'weight' : 74.3, 'married' : False, 'allergies' : ['pollen', 'flue'], 
                'contact_details': {'phone': '03238724496'}}

p1 = Patient(**patient_info)

insert_patient_data(p1)
update_patient_data(p1)



