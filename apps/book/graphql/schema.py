import graphql_jwt

from apps.book.graphql.queries import Query
from apps.book.graphql.mutation import Mutation
import graphene


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(Query, graphene.ObjectType):
    pass


class Mutation(Mutation, AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

__all__ = ("schema",)
