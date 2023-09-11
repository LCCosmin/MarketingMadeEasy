from sqlalchemy import Column, String, Table, text, UUID, ForeignKey

from core.database import meta

users_credentials = Table(
    "users_credentials",
    meta,
    Column("id", UUID, nullable=False, unique=True, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column("user_id", UUID, ForeignKey("users_data.id"), nullable=False, unique=True),
    Column("hashed_password", String(50), nullable=False, unique=True),
)