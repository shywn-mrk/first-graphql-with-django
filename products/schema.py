import graphene
from graphene_django.types import DjangoObjectType
from .models import Product

from graphene_plugin import patch_object_type

patch_object_type()

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.String())

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)

