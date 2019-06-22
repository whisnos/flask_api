"""empty message

Revision ID: ca0e9ac811a5
Revises: 
Create Date: 2019-06-22 23:53:10.708169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca0e9ac811a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'add_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('add_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
