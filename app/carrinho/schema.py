from ..extensions import ma
from .model import Carrinho


class CarrinhoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Carrinho
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    forma_pagamento=ma.String(required=True)
    preco_frete=ma.Integer(required=True)
    quantidade=ma.Integer(required=True)
    preco_total = ma.Integer(required=True)

      