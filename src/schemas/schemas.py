from pydantic import BaseModel
from typing import Optional

#  nome varchar(50) not null,
#         email varchar(255) not null unique,
#         senha varchar(255) not null,
#         ativo boolean default false,
#         admin boolean default false,
class UserSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

