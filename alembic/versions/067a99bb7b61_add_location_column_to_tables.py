"""add location column to tables

Revision ID: 067a99bb7b61
Revises: a60f79681c04
Create Date: 2025-08-27 12:01:10.169019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067a99bb7b61'
down_revision = 'a60f79681c04'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("tables", sa.Column("location", sa.String(), nullable=True))


def downgrade():
    op.drop_column("tables", "location")
