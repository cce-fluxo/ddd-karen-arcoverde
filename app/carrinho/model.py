from app.extensions import db
from app.models import BaseModel

# Carrinho
# tabela com as informações necessárias para poder pagar o que contem no carrinho
# id => chave primária
# forma_pagamento => pode ser PIX, boleto bancario, cartao de crédito etc.
# preco_frete => preço diferente para cada regiao e para cada transporte
# quantidade => quantidade de itens no carrinho
# preco_total => preço total, incluindo tudo que foi colocado no carrinho

class Carrinho(BaseModel):
        __tablename__ = 'carrinho'
        id = db.Column(db.Integer, primary_key = True)
        forma_pagamento = db.Column(db.String(40), nullable = False)
        preco_frete = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # carrinho(one) <-> cupons(one)
        cupons_id = db.Column(db.Integer, db.ForeignKey('cupons.id'))

        # motos carrinho(many) <-> carrinho(one)
        motos_carrinho = db.relationship('MotosCarrinho', backref = 'motosCarrinho_carrinho')

        # carros carrinho(many) <-> carrinho(one)
        carros_carrinho = db.relationship('CarrosCarrinho', backref = 'carrosCarrinho_carrinho')

        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))