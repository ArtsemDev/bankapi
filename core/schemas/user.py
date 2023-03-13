from pydantic import BaseModel, Field, EmailStr, root_validator


class RegisterForm(BaseModel):
    email: EmailStr = Field(
        title='User Email',
        description='User Unique Email'
    )
    username: str = Field(
        title='Username',
        description='Unique Username',
        max_length=128,
        min_length=2
    )
    password: str = Field(
        title='User password',
        description='User password',
        min_length=8,
        max_length=64,
        regex=r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})'
    )
