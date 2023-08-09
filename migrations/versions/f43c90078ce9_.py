"""empty message

Revision ID: f43c90078ce9
Revises: 4559cd5f6bdd
Create Date: 2023-08-09 14:46:49.890495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f43c90078ce9'
down_revision = '4559cd5f6bdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.INTEGER(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
