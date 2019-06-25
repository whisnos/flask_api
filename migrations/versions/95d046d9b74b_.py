"""empty message

Revision ID: 95d046d9b74b
Revises: b312a39b2732
Create Date: 2019-06-24 16:23:21.304532

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '95d046d9b74b'
down_revision = 'b312a39b2732'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('back_mobile', sa.String(length=11), nullable=True))
    op.add_column('user', sa.Column('mobile', sa.String(length=11), nullable=True))
    op.add_column('user', sa.Column('work', sa.DateTime(), nullable=True))
    op.drop_index('email', table_name='user')
    op.create_unique_constraint(None, 'user', ['mobile'])
    op.drop_column('user', 'add_time')
    op.drop_column('user', 'password')
    op.drop_column('user', 'address')
    op.drop_column('user', 'is_delete')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=30), nullable=True))
    op.add_column('user', sa.Column('is_delete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('address', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('user', sa.Column('add_time', mysql.DATETIME(), nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_column('user', 'work')
    op.drop_column('user', 'mobile')
    op.drop_column('user', 'back_mobile')
    # ### end Alembic commands ###