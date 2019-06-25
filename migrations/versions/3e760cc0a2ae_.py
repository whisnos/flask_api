"""empty message

Revision ID: 3e760cc0a2ae
Revises: a3e8e3b1246e
Create Date: 2019-06-24 11:17:15.005135

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3e760cc0a2ae'
down_revision = 'a3e8e3b1246e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'add_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('add_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
