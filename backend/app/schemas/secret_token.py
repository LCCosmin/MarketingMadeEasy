from sqlalchemy import Column, String, Table, text, UUID

from app.core.database import meta

secret_token = Table(
    "secret_token",
    meta,
    Column("id", UUID, nullable=False, unique=True, primary_key=True, server_default=text("gen_random_uuid()")),
    Column("name", String(50), nullable=False, unique=True),
    Column("token", String(150), nullable=True, unique=True),
)