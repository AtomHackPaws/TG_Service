"""init

Revision ID: 7d9d4c1d1e03
Revises:
Create Date: 2024-06-16 02:11:18.706214

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "7d9d4c1d1e03"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profile",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_profile_id"), "profile", ["id"], unique=False)
    op.create_table(
        "quiz",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("id_photo", sa.String(), nullable=False),
        sa.Column("id_mark", sa.String(), nullable=False),
        sa.Column("label", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_quiz_id"), "quiz", ["id"], unique=False)
    op.create_table(
        "result",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("result", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("profile_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(["profile_id"], ["profile.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_result_id"), "result", ["id"], unique=False)
    op.create_index(
        op.f("ix_result_profile_id"), "result", ["profile_id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_result_profile_id"), table_name="result")
    op.drop_index(op.f("ix_result_id"), table_name="result")
    op.drop_table("result")
    op.drop_index(op.f("ix_quiz_id"), table_name="quiz")
    op.drop_table("quiz")
    op.drop_index(op.f("ix_profile_id"), table_name="profile")
    op.drop_table("profile")
    # ### end Alembic commands ###
