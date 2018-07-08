import graphene
import graphql_jwt

import ridemywayapp.schema
import users.schema


class Query(users.schema.Query, ridemywayapp.schema.Query, graphene.ObjectType):

    """
        Class Query to loads all queries
    """

    pass


class Mutation(users.schema.Mutation, ridemywayapp.schema.Mutation, graphene.ObjectType):

    """
        Class Mutation to create new instance of class methods
    """

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
