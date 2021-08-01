import graphene
from .models import Incredient, Category
from graphene_django import DjangoObjectType
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ['name','incredients',]


class IncredientTyoe(DjangoObjectType):
    class Meta:
        model = Incredient
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "notes": ["exact", "icontains"],
            "category": ["exact"],
            "category__name": ["exact"],
        }
class Query(graphene.ObjectType):
    category = Node.Field(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)

    ingredient = Node.Field(IncredientTyoe)
    all_ingredients = DjangoFilterConnectionField(IncredientTyoe)
schema = graphene.Schema(query=Query)