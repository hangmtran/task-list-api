"""empty message

Revision ID: 2300c6f47584
Revises: 54ca55a8043f
Create Date: 2022-11-07 16:55:28.500843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2300c6f47584'
down_revision = '54ca55a8043f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
