def carregar_musicas():
     try:
         with open("musicas.txt", "r") as arquivo:
             conteudo = arquivo.read()
             if conteudo:
                 return json.loads(conteudo)
             else:
                 return []
     except FileNotFoundError:
         return []
     except json.JSONDecodeError:
         return []

# Função para salvar as músicas no arquivo
def salvar_musicas(musicas):
    with open("musicas.txt", "w") as arquivo:
        json.dump(musicas, arquivo)

# Rota para listar todas as músicas
@app.get("/musicas", response_model=List[Musica], tags=["Músicas"])
async def listar_musicas():
    return carregar_musicas()

# Rota para criar uma nova música
@app.post("/musicas", response_model=Musica, tags=["Músicas"])
async def adicionar_musica(musica: Musica):
    musicas = carregar_musicas()
    musicas.append(musica.dict())
    salvar_musicas(musicas)
    return musica

# Rota para obter detalhes de uma música específica
@app.get("/musicas/{musica_id}", response_model=Musica, tags=["Músicas"])
async def obter_musica(musica_id: int):
    musicas = carregar_musicas()
    if 1 <= musica_id <= len(musicas):
        return musicas[musica_id - 1]
    else:
        raise HTTPException(status_code=404, detail="Música não encontrada")

# Rota para atualizar uma música existente
@app.put("/musicas/{musica_id}", response_model=Musica, tags=["Músicas"])
async def atualizar_musica(musica_id: int, musica: Musica):
    musicas = carregar_musicas()
    if 1 <= musica_id <= len(musicas):
        musicas[musica_id - 1] = musica.dict()
        salvar_musicas(musicas)
        return musica
    else:
        raise HTTPException(status_code=404, detail="Música não encontrada")

# Rota para remover uma música
@app.delete("/musicas/{musica_id}", response_model=Musica, tags=["Músicas"])
async def remover_musica(musica_id: int):
    musicas = carregar_musicas()
    if 1 <= musica_id <= len(musicas):
        musica_removida = musicas.pop(musica_id - 1)
        salvar_musicas(musicas)
        return {"mensagem": "Música removida com sucesso!", "musica_removida": musica_removida}
    else:
        raise HTTPException(status_code=404, detail="Música não encontrada")

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
