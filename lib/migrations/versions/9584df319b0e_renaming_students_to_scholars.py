"""

Revision ID: 9584df319b0e
Revises: 791279dd0760
Create Date: 2023-12-14 06:25:13.731795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9584df319b0e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
