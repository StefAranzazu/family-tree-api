"""empty message

Revision ID: a634a2fa3ae8
Revises: 6481f0c7c406
Create Date: 2021-08-29 21:40:40.486700

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a634a2fa3ae8'
down_revision = '6481f0c7c406'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('person_ibfk_3', 'person', type_='foreignkey')
    op.drop_column('person', 'child_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('child_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('person_ibfk_3', 'person', 'person', ['child_id'], ['id'])
    # ### end Alembic commands ###
