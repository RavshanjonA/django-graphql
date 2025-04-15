from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))), # Given that schema path is defined in GRAPHENE['SCHEMA'] in your settings.py
]