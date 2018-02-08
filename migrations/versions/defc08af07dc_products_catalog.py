"""products catalog

Revision ID: defc08af07dc
Revises: 
Create Date: 2018-02-07 08:15:51.468533

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'defc08af07dc'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('details', sqlalchemy_utils.types.json.JSONType(), nullable=True),
    sa.Column('catalog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['catalog_id'], ['catalogs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('descr', sa.Text(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('model_name', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_model_name'), 'products', ['model_name'], unique=False)
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_index(op.f('ix_products_model_name'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_table('categories')
    op.drop_table('catalogs')
    # ### end Alembic commands ###
