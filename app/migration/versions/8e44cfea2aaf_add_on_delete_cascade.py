"""Add on delete cascade

Revision ID: 8e44cfea2aaf
Revises: 649b6f98be7f
Create Date: 2025-03-12 21:27:39.285316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e44cfea2aaf'
down_revision: Union[str, None] = '649b6f98be7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint('dishes_restaurant_id_fkey', 'dishes', type_='foreignkey')
    op.create_foreign_key(
        'dishes_restaurant_id_fkey', 'dishes', 'restaurants',
        ['restaurant_id'], ['id'], ondelete='CASCADE'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('dishes_restaurant_id_fkey', 'dishes', type_='foreignkey')
    op.create_foreign_key(
        'dishes_restaurant_id_fkey', 'dishes', 'restaurants',
        ['restaurant_id'], ['id']
    )
