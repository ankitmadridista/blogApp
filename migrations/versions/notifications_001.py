"""add notifications

Revision ID: notifications_001
Revises: 4adfd6852573
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'notifications_001'
down_revision = '4adfd6852573'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'notification',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('actor_id', sa.Integer(), nullable=False),
        sa.Column('type', sa.String(length=50), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=True),
        sa.Column('comment_id', sa.Integer(), nullable=True),
        sa.Column(
            'is_read',
            sa.Boolean(),
            server_default=sa.text('false'),
            nullable=False
        ),
        sa.Column('timestamp', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(['actor_id'], ['user.id']),
        sa.ForeignKeyConstraint(['comment_id'], ['comment.id']),
        sa.ForeignKeyConstraint(['post_id'], ['post.id']),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),

        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        'ix_notification_timestamp',
        'notification',
        ['timestamp'],
        unique=False
    )


def downgrade():
    op.drop_index(
        'ix_notification_timestamp',
        table_name='notification'
    )

    op.drop_table('notification')