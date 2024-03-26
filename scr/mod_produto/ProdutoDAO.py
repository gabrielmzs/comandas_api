from fastapi import APIRouter
from mod_produto.Produto import Produto

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])
def get_produto():
    return {"msg": "get todos executado"}, 200

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/produto/", tags=["Produto"])
def post_produto(p: Produto):
    return {"msg": "post executado", "nome": p.nome, "descrição": p.descricao, "foto": p.foto, "valor": p.valor }, 200

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, p: Produto):
    return {"msg": "put executado", "nome": p.nome, "descrição": p.descricao, "foto": p.foto, "valor": p.valor }, 201
    

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201