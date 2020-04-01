"""empty message

Revision ID: 67c68151f28b
Revises: dfdc20e14f72
Create Date: 2020-04-01 15:40:34.472574

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '67c68151f28b'
down_revision = 'dfdc20e14f72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('email', sa.String(length=50), nullable=False))
    op.drop_column('log', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('username', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('log', 'email')
    # ### end Alembic commands ###
