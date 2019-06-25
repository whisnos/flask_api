"""empty message

Revision ID: 35421d79ad22
Revises: 07cb01470ba7
Create Date: 2019-06-24 14:26:44.663553

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '35421d79ad22'
down_revision = '07cb01470ba7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=20), nullable=True))
    op.drop_index('username', table_name='user')
    op.create_unique_constraint(None, 'user', ['name'])
    op.drop_column('user', 'last_login_ip')
    op.drop_column('user', 'login_num')
    op.drop_column('user', 'username')
    op.drop_column('user', 'last_login_time')
    op.drop_column('user', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('last_login_time', mysql.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('username', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('user', sa.Column('login_num', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('last_login_ip', mysql.VARCHAR(length=15), nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('username', 'user', ['username'], unique=True)
    op.drop_column('user', 'name')
    # ### end Alembic commands ###