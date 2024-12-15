import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.models import Product, User, Order, db

class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = Product

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class OrderType(SQLAlchemyObjectType):
    class Meta:
        model = Order

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_users = graphene.List(UserType)

    def resolve_all_products(root, info):
        return Product.query.all()

    def resolve_all_users(root, info):
        return User.query.all()

schema = graphene.Schema(query=Query)
