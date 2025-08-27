"""Fix reservation_customer table

Revision ID: c98ca70c83af
Revises: 067a99bb7b61
Create Date: 2025-08-27 15:04:45.197820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c98ca70c83af'
down_revision = '067a99bb7b61'
branch_labels = None
depends_on = None


def upgrade():
    # Drop old table if it exists
    op.drop_table("reservation_customer")

    # Recreate correct association table
    op.create_table(
        "reservation_customer",
        sa.Column("reservation_id", sa.Integer, sa.ForeignKey("reservations.id"), primary_key=True),
        sa.Column("customer_id", sa.Integer, sa.ForeignKey("customers.id"), primary_key=True),
    )


def downgrade():
    op.drop_table("reservation_customer")
