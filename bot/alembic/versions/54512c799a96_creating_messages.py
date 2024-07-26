"""Creating Messages

Revision ID: 54512c799a96
Revises: 0f365e4ebf7f
Create Date: 2024-07-25 02:49:25.735608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54512c799a96'
down_revision: Union[str, None] = '0f365e4ebf7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('messages', sa.Column('phone_number', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'phone_number')
    op.drop_column('messages', 'date')
    # ### end Alembic commands ###
