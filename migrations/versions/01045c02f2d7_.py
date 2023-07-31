"""empty message

Revision ID: 01045c02f2d7
Revises: e89c5c7a9798
Create Date: 2023-07-31 10:15:37.294236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01045c02f2d7'
down_revision = 'e89c5c7a9798'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kitchen_side',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'item_id')
    )
    op.drop_table('kitchen side')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kitchen side',
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name='kitchen side_item_id_fkey'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name='kitchen side_order_id_fkey'),
    sa.PrimaryKeyConstraint('order_id', 'item_id', name='kitchen side_pkey')
    )
    op.drop_table('kitchen_side')
    # ### end Alembic commands ###
