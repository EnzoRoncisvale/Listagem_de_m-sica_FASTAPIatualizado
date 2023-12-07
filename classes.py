from pydantic import BaseModel

class Musica(BaseModel):
    nome: str
    artista: str
    album: str
    ano: str
