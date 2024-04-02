from fastapi import APIRouter
from mod_produto.Produto import Produto

import db
from mod_produto.ProdutoModel import ProdutoDB

router = APIRouter()


@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()
        produtos = session.query(ProdutoDB).all()
        return produtos, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto_by_id(id: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return produto, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(produto: Produto):
    try:
        session = db.Session()
        novo_produto = ProdutoDB(None,produto.nome,produto.descricao,produto.foto,produto.valor)
        session.add(novo_produto)
        session.commit()
        return {"id": novo_produto.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, produto: Produto):
    try:
        session = db.Session()
        produto_existente = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        produto_existente.nome = produto.nome
        produto_existente.descricao = produto.descricao
        produto_existente.foto = produto.foto
        produto_existente.valor = produto.valor
        session.add(produto_existente)
        session.commit()
        return {"id": produto_existente.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(produto)
        session.commit()
        return {"id": produto.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
