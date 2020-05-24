import graphene
from snippets.schema import Query as snippets_query
from products.schema import Query as products_query

class Query(snippets_query, products_query):
    pass

schema = graphene.Schema(query=Query)