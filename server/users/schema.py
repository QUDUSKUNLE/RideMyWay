import graphene

from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):

    """
        Class UserType to loads user model
    """

    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):

    """
        Class Query to query all manner of users
    """

    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        user = info.context.user
        if not user.is_superuser:
            raise Exception('Authentication credentials were not provided')

        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return Exception('Authentication credentials were not provided')

        return user


class CreateUser(graphene.Mutation):

    """
        Class CreateUser to create a new user
    """

    user = graphene.Field(UserType)

    class Arguments:

        """
            Class Arguments method
        """

        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        check_email = get_user_model().objects.filter(email=email).first()
        if check_email:
            return Exception('User already exist')

        check_username = get_user_model().objects.filter(
            username=username).first()
        if check_username:
            return Exception('Username already exist')

        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):

    """
        Class Mutation to alter, create a new instance of user
    """

    create_user = CreateUser.Field()
