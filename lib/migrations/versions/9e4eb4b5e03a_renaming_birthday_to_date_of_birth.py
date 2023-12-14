"""Renaming birthday to date_of_birth

Revision ID: 9e4eb4b5e03a
Revises: 9584df319b0e
Create Date: 2023-12-14 08:32:44.187649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e4eb4b5e03a'
down_revision = '9584df319b0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_column('birthday', 'date of birth')
    pass


def downgrade() -> None:
    op.rename_column('date of birth', 'birthday')
    pass
