import databases
import pytest
from sqlalchemy.sql.expression import delete

from app.models.schema import Films as SAMovie
from app.models.schema import Likes as SALikes
from app.fields import Likes, Movie
from app.utils import fetch_all_records, fetch_records_by_user_id, insert_values


@pytest.mark.asyncio
async def test_fetch_all_records(fill_movies_table: None, session: databases.Database):
    result = await fetch_all_records(SAMovie, Movie, session)
    assert result == [
        Movie(id=1, name='Властелин колец'),
        Movie(id=2, name='Звездные войны'),
        Movie(id=3, name='Матрица'),
    ]


@pytest.mark.asyncio
async def test_insert_values(session: databases.Database):
    result = await insert_values(
        SAMovie,
        Movie,
        [
            {'id': 2077, 'name': 'Futurama'},
            {'id': 1337, 'name': 'Simpsons'},
        ], session
    )
    assert result == [Movie(id=2077, name='Futurama'), Movie(id=1337, name='Simpsons')]
    await session.fetch_one(query=delete(SAMovie).where(SAMovie.id==2077 or SAMovie.id==1337))


@pytest.mark.asyncio
async def test_fetch_records_by_user_id(fill_likes_table: None, session: databases.Database):
    result = await fetch_records_by_user_id(1, SALikes, Likes, session)
    assert result == [Likes(user_id=1, film_id=1), Likes(user_id=1, film_id=2), Likes(user_id=1, film_id=3)]
