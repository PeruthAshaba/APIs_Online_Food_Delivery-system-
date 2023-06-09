"""initial migration

Revision ID: 1e00ad8f67b7
Revises: d60cccd69e45
Create Date: 2023-03-16 11:32:30.655998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1e00ad8f67b7'
down_revision = 'd60cccd69e45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', mysql.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###
