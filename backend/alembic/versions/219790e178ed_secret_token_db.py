"""secret_token_db

Revision ID: 219790e178ed
Revises: ca123caeff50
Create Date: 2023-09-13 14:15:57.151465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.schemas.secret_token import secret_token


# revision identifiers, used by Alembic.
revision: str = '219790e178ed'
down_revision: Union[str, None] = 'ca123caeff50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "secret_token",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            unique=True,
        ),
        sa.Column("name", sa.String(50), nullable=False, unique=True,),
        sa.Column("token", sa.String(150), nullable=False, unique=True,),
    )
    
    op.bulk_insert(
        secret_token,
        [
            {
                "name": "jwt_secret_token",
                "token": "1c217fe0687ad2d8874f0f19dedc8f32403c32340a1a8d3d38e029a35719fb10",
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("secret_token")
