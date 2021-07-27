from typing import List

import strawberry

from app.config import database
from app.models.schema import Likes as SALikes
from app.fields import Likes
from app.utils import insert_values


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def save_like(user_id: int, film_ids: List[int]) -> List[Likes]:
        values = [{'user_id': user_id, 'film_id': film_id} for film_id in film_ids]
        return await insert_values(SALikes, Likes, values, database)
