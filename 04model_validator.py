from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:    str 
    email:   EmailStr
    linkedin_url: AnyUrl
    age:     int
    weight:  float
    married: bool
    allergies: List[str]
    contact_details: Dict[str , str]


    @model_validator(mode = 'after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:

            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name', mode = 'after') 
    @classmethod
    def  upper_case_name(cls, value):
        return value.upper()
    


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

patient_info = {'name' : 'mahad','email': 'qazimahad07@hdfc.com','linkedin_url':'http://linked.com/12', 'age' : 20, 'weight' : 74.3, 'married' : False, 'allergies' : ['pollen', 'flue'], 
                'contact_details': {'phone': '03238724496'}}

p1 = Patient(**patient_info)

insert_patient_data(p1)
update_patient_data(p1)



