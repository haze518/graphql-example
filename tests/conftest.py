import os
import pytest
import databases

from alembic import command
from alembic.config import Config
from sqlalchemy import insert
from sqlalchemy.sql.expression import delete
from sqlalchemy_utils import create_database, drop_database

from app.models.schema import Films, Likes, Users
from app.config import SQLALCHEMY_DATABASE_URL


@pytest.fixture(scope='session')
def temp_db() -> str:
    """
    Создание БД для тестов
    """
    create_database(SQLALCHEMY_DATABASE_URL)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")
    try:
        yield SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(SQLALCHEMY_DATABASE_URL)


@pytest.fixture
async def session(temp_db: str) -> databases.Database:
    conn = databases.Database(temp_db)
    try:
        await conn.connect()
        yield conn
    finally:
        await conn.disconnect()


@pytest.fixture
@pytest.mark.asyncio
async def fill_movies_table(session: databases.Database) -> None:
    values = [
        {'id': 1, 'name': 'Властелин колец'},
        {'id': 2, 'name': 'Звездные войны'},
        {'id': 3, 'name': 'Матрица'},
    ]
    await session.execute_many(query=insert(Films), values=values)
    yield
    await session.execute(query=delete(Films))


@pytest.fixture
@pytest.mark.asyncio
async def fill_users_table(session: databases.Database) -> None:
    query = (
        insert(Users)
        .values({'id': 1, 'name': 'Морти'})
    )
    await session.execute(query=query)
    yield
    await session.execute(query=delete(Users))


@pytest.fixture
@pytest.mark.asyncio
async def fill_likes_table(
    fill_movies_table: None,
    fill_users_table: None,
    session: databases.Database
) -> None:
    values = [
        {'user_id': 1, 'film_id': 1},
        {'user_id': 1, 'film_id': 2},
        {'user_id': 1, 'film_id': 3},
    ]
    await session.execute_many(query=insert(Likes), values=values)
    yield
    await session.execute(query=delete(Likes))
