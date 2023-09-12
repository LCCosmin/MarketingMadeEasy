from sqlalchemy import Column, String, Table, text, UUID, ARRAY

from app.core.database import meta

users_data = Table(
    "users_data",
    meta,
    Column("id", UUID, nullable=False, unique=True, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column("name", String(50), nullable=False, unique=False),
    Column("forname", String(50), nullable=False, unique=False),
    Column("username", String(150), nullable=False, unique=True),
    Column("owned_projects_id", ARRAY(String(50)), nullable=False, unique=False),
)