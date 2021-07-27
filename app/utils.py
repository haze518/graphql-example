from typing import List
from sqlalchemy.sql.elements import literal_column

import strawberry
from databases.core import Database
from asyncpg import Record
from sqlalchemy import select, insert

from app.models.schema import Base


async def fetch_all_records(
    table: Base,
    schema: strawberry.type,
    conn: Database,
) -> List[strawberry.type]:
    records = [
        unpack_object_data(data) for data in await conn.fetch_all(select([table]))
    ]
    return [schema(**record) for record in records]


async def fetch_records_by_user_id(
    user_id: int,
    table: Base,
    schema: strawberry.type,
    conn: Database,
) -> List[strawberry.type]:
    query = (
        select([table])
        .where(table.user_id==user_id)
    )
    records = [
        unpack_object_data(data) for data in await conn.fetch_all(query)
    ]
    return [schema(**record) for record in records]


async def insert_values(
    table: Base,
    schema: strawberry.type,
    values: List[dict],
    conn: Database,
) -> List[strawberry.type]:
    records = [
        unpack_object_data(data) for data in await conn.fetch_all(
            query=insert(table)
            .values(values)
            .returning(literal_column('*'))
        )
    ]
    return [schema(**record) for record in records]


def unpack_object_data(data: Record) -> dict:
    """
    Распаковка данных из выгруженного с БД объекта
    """
    return dict(zip(data, data.values()))
