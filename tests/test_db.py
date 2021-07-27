import databases
import pytest
from sqlalchemy import select

from app.models.schema import Films, Likes, Users
from app.utils import unpack_object_data


@pytest.mark.asyncio
async def test_movies_table_data(fill_movies_table: None, session: databases.Database):
    expected = [
        {'id': 1, 'name': 'Властелин колец'},
        {'id': 2, 'name': 'Звездные войны'},
        {'id': 3, 'name': 'Матрица'}
    ]
    query = (
        select([Films])
    )
    result = [unpack_object_data(data) for data in await session.fetch_all(query)]
    assert result == expected


@pytest.mark.asyncio
async def test_users_table_data(fill_users_table: None, session: databases.Database):
    query = (
        select([Users])
    )
    result = unpack_object_data(await session.fetch_one(query))
    assert result == {'id': 1, 'name': 'Морти'}


@pytest.mark.asyncio
async def test_likes_table_data(fill_likes_table: None, session: databases.Database):
    query = (
        select([Likes])
    )
    result = [unpack_object_data(data) for data in await session.fetch_all(query)]
    assert result
