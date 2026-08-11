from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    address: Address


def view(patient: Patient):
    print(patient.name)
    print(patient.gender)
    print(patient.address)
    print(patient.address.city)


display = {
    'name': 'Mahad',
    'gender': 'Male',
    'address': {
        'city': 'Peshawar',
        'state': 'KPK',
        'pin': '12333'
    }
}


p1 = Patient(**display)

view(p1)


# --------------------------------------------------
# 1. Convert Pydantic model → Python dictionary
# --------------------------------------------------

temp = p1.model_dump()

print(temp)
print(type(temp))


# --------------------------------------------------
# 2. Convert Pydantic model → JSON string
# --------------------------------------------------

temp1 = p1.model_dump_json()

print(temp1)
print(type(temp1))


# --------------------------------------------------
# 3. include
# --------------------------------------------------

temp2 = p1.model_dump(
    include={'name', 'gender'}
)

print(temp2)


# --------------------------------------------------
# 4. exclude
# --------------------------------------------------

temp3 = p1.model_dump(
    exclude={'gender'}
)

print(temp3)


# --------------------------------------------------
# 5. exclude_unset
# --------------------------------------------------

temp4 = p1.model_dump(
    exclude_unset=True
)

print(temp4)


# --------------------------------------------------
# 6. exclude_defaults
# --------------------------------------------------

temp5 = p1.model_dump(
    exclude_defaults=True
)

print(temp5)


# --------------------------------------------------
# 7. exclude_none
# --------------------------------------------------

temp6 = p1.model_dump(
    exclude_none=True
)

print(temp6)