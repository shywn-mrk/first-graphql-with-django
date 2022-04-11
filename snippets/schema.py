import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet
from graphene_plugin import patch_object_type

patch_object_type()

class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet

class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)

    def resolve_all_snippets(self, info, **kwargs):
        return Snippet.objects.all()
