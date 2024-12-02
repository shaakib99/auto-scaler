"""empty message

Revision ID: 60d888538c8c
Revises: 
Create Date: 2024-12-02 18:12:30.224722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '60d888538c8c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('id', table_name='environment_variables')
    op.drop_table('environment_variables')
    op.drop_index('id', table_name='ports')
    op.drop_table('ports')
    op.add_column('workers', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.add_column('workers', sa.Column('is_cloned', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'workers', 'workers', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workers', type_='foreignkey')
    op.drop_column('workers', 'is_cloned')
    op.drop_column('workers', 'parent_id')
    op.create_table('ports',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('worker_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('port_number', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('port_type', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('mapped_port', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], name='ports_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'ports', ['id'], unique=True)
    op.create_table('environment_variables',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('worker_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('key', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('value', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], name='environment_variables_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'environment_variables', ['id'], unique=True)
    # ### end Alembic commands ###
