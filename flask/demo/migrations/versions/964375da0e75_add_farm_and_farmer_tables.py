"""Add farm and farmer tables

Revision ID: 964375da0e75
Revises: f6e97a20d9f6
Create Date: 2024-03-19 17:39:04.360680

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "964375da0e75"
down_revision = "f6e97a20d9f6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "farmer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=30), nullable=False),
        sa.Column("middle_name", sa.String(length=30), nullable=False),
        sa.Column("last_name", sa.String(length=30), nullable=False),
        sa.Column("id_number", sa.String(length=30), nullable=False),
        sa.Column(
            "created_on",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "updated_on",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("farmer", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_farmer_first_name"), ["first_name"], unique=False
        )
        batch_op.create_index(batch_op.f("ix_farmer_id"), ["id"], unique=False)

    op.create_table(
        "farm",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=30), nullable=False),
        sa.Column("farmer_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_on",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "updated_on",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["farmer_id"],
            ["farmer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("farm", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_farm_id"), ["id"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("farm", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_farm_id"))

    op.drop_table("farm")
    with op.batch_alter_table("farmer", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_farmer_id"))
        batch_op.drop_index(batch_op.f("ix_farmer_first_name"))

    op.drop_table("farmer")
    # ### end Alembic commands ###