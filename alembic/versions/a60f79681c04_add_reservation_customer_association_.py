"""add reservation_customer association table

Revision ID: a60f79681c04
Revises: eb2727e9190c
Create Date: 2025-08-27 11:01:29.310914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a60f79681c04'
down_revision = 'eb2727e9190c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "reservation_customer",
        sa.Column("reservation_id", sa.Integer(), sa.ForeignKey("reservations.id"), primary_key=True),
        sa.Column("customer_id", sa.Integer(), sa.ForeignKey("customers.id"), primary_key=True)
    )


def downgrade():
    op.drop_table("reservation_customer")
