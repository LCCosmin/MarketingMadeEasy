"""init_setup_db

Revision ID: ca123caeff50
Revises: 
Create Date: 2023-09-11 20:02:22.982008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca123caeff50'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users_data",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            unique=True,
        ),
        sa.Column("name", sa.String(50), nullable=False, unique=False),
        sa.Column("forname", sa.String(50), nullable=False, unique=False),
        sa.Column("username", sa.String(150), nullable=False, unique=True),
        sa.Column("owned_projects_id", sa.ARRAY(sa.String(50)), nullable=False, unique=False),
    )
    
    op.create_table(
        "users_credentials",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            unique=True,
        ),
        sa.Column("user_id", sa.UUID, nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(50), nullable=False, unique=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users_data.id"]
        ),
    )
    
    op.create_table(
        "projects",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            unique=True,
        ),
        sa.Column("user_id", sa.UUID, nullable=False, unique=False),
        sa.Column("project_name", sa.String(50), nullable=False, unique=False),
        sa.Column("project_description", sa.String(150), nullable=True, unique=False),
        sa.Column("project_moto", sa.String(50), nullable=True, unique=False),
        sa.Column("number_of_custom_pictures", sa.Integer, nullable=False, unique=False),
        sa.Column("number_of_menus_pictures", sa.Integer, nullable=False, unique=False),
        sa.Column("logo_video", sa.String(100), nullable=True, unique=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users_data.id"]
        ),
    )


def downgrade() -> None:
    op.drop_table("projects")
    op.drop_table("users_credentials")
    op.drop_table("users_data")
