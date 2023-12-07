import pandas as pd
from banco_de_dados import banco, comando
from fastapi.responses import JSONResponse
from classes import Musica


def abrir_lista():
    consulta_sql = "SELECT * FROM tabela_musica"
    df = pd.read_sql(consulta_sql, banco)
    dados = df.to_dict(orient='records')
    return JSONResponse(content={'dados': dados})

def incluir_musica(entrada: Musica):
    comando.execute("INSERT INTO tabela_musica VALUES('{}', '{}', '{}', '{}')".format(entrada.nome, entrada.artista, entrada.album, entrada.ano))
    banco.commit()
    banco.close()
    return 
