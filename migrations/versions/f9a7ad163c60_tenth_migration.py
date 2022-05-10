"""tenth Migration

Revision ID: f9a7ad163c60
Revises: deab40c8ce3c
Create Date: 2022-05-10 20:29:45.635284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9a7ad163c60'
down_revision = 'deab40c8ce3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('pitches', 'pitch_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'title')
    # ### end Alembic commands ###
