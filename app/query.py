import strawberry
from typing import List

from app.config import database
from app.fields import Likes, Movie, User
from app.models.schema import Likes as SALikes
from app.models.schema import Films as SAMovie
from app.models.schema import Users as SAUser
from app.utils import fetch_all_records, fetch_records_by_user_id


async def get_likes(user_id: int) -> List[Likes]:
    return await fetch_records_by_user_id(user_id, SALikes, Likes, database)


async def get_movies() -> List[Movie]:
    return await fetch_all_records(SAMovie, Movie, database)


async def get_user_information(user_id: int) -> User:
    return (await fetch_records_by_user_id(user_id, SAUser, User, database))


@strawberry.type
class Query:
    movie: List[Movie] = strawberry.field(resolver=get_movies)
    likes: List[Likes] = strawberry.field(resolver=get_likes)
    user: User = strawberry.field(resolver=get_user_information)
