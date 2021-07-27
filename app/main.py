from sqlalchemy.sql.expression import delete, insert
from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL
from strawberry import Schema

from app.config import database
from app.query import Query
from app.mutations import Mutation
from app.models.schema import Films, Users

graphql_app = GraphQL(Schema(query=Query, mutation=Mutation))
routes = [
    Route('/graphql', graphql_app)
]


def create_app():
    app = Starlette(
        routes=routes,
        on_startup=[connect_database, insert_dummy_data],
        on_shutdown=[delete_dummy_data, disconnect_database],
    )
    return app


async def connect_database() -> None:
    await database.connect()


async def disconnect_database() -> None:
    await database.disconnect()


async def insert_dummy_data() -> None:
    await database.execute(insert(Films).values(
        [
            {'id': 1, 'name': 'Властелин колец'},
            {'id': 2, 'name': 'Звездные войны'},
            {'id': 3, 'name': 'Матрица'},
        ],
    ))
    await database.execute(insert(Users).values(
        [
            {'id': 1, 'name': 'Морти'},
        ],
    ))


async def delete_dummy_data() -> None:
    await database.execute(delete(Films))
    await database.execute(delete(Users))
