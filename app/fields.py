from typing import List

import strawberry


@strawberry.type
class Movie:
    id: int
    name: str


@strawberry.type
class Likes:
    user_id: int
    film_id: int


@strawberry.type
class User:
    id: int
    name: str
    likes: List[Likes]
