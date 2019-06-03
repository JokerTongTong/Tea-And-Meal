"""initial

Revision ID: 602cf3f8a7c2
Revises: 
Create Date: 2019-06-03 17:25:30.213479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602cf3f8a7c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('pwd', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('face', sa.String(length=255), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('uuid', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('face'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_user_addtime'), 'user', ['addtime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_addtime'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
