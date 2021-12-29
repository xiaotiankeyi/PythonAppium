"""'model_file'

Revision ID: 3f322c93f1d0
Revises: 
Create Date: 2021-12-18 18:10:01.922000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f322c93f1d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.Boolean(), nullable=True),
    sa.Column('createTime', sa.DateTime(), nullable=True),
    sa.Column('updateTime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_new',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag', sa.String(length=10), nullable=False),
    sa.Column('context', sa.String(length=100), nullable=True),
    sa.Column('createTime', sa.DateTime(), nullable=True),
    sa.Column('updateTime', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['t_author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_new')
    op.drop_table('t_author')
    # ### end Alembic commands ###
