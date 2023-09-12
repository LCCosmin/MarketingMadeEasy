from sqlalchemy import Column, String, Table, text, UUID, ForeignKey, Integer

from app.core.database import meta

projects = Table(
    "projects",
    meta,
    Column("id", UUID, nullable=False, unique=True, primary_key=True, server_default=text("gen_random_uuid()")),
    Column("user_id", UUID, ForeignKey("users_data.id"), nullable=False, unique=False),
    Column("project_name", String(50), nullable=False, unique=False),
    Column("project_description", String(150), nullable=True, unique=False),
    Column("project_moto", String(50), nullable=True, unique=False),
    Column("number_of_custom_pictures", Integer, nullable=False, unique=False),
    Column("number_of_menus_pictures", Integer, nullable=False, unique=False),
    Column("logo_video", String(100), nullable=True, unique=False),
)