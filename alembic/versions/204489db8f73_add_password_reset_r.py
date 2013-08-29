"""add password_reset_required column to user

Revision ID: 204489db8f73
Revises: 25e7a9839cd4
Create Date: 2013-08-29 19:45:42.023964

"""

# revision identifiers, used by Alembic.
revision = '204489db8f73'
down_revision = '25e7a9839cd4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('password_reset_required', sa.Boolean(), nullable=False,
        server_default=sa.sql.expression.false()))
    op.alter_column('user', 'password_reset_required', server_default=None)


def downgrade():
    op.drop_column('user', 'password_reset_required')
