import graphene
from graphql_jwt.decorators import login_required

from apps.book.graphql.resolvers import resolve_category, resolve_books, resolve_categories, resolve_genres
from apps.book.graphql.type import BookType, BookCategoryType, BookGenreType


class Query(graphene.ObjectType):
    books = graphene.List(BookType, id=graphene.Int(), ct_id=graphene.Int(), gn_id=graphene.List(graphene.Int),
                          search=graphene.String())
    categories = graphene.List(BookCategoryType)
    category = graphene.Field(BookCategoryType, id=graphene.Int())
    genres = graphene.List(BookGenreType, )

    @login_required
    def resolve_category(self, info, id):
        return resolve_category(id=id)

    def resolve_books(self, info, id=None, ct_id=None, gn_id=None, search=None, **kwargs):
        return resolve_books(id, ct_id, gn_id, search)

    def resolve_categories(self, info, **kwargs):
        return resolve_categories()

    def resolve_genres(self, info, **kwargs):
        return resolve_genres()
