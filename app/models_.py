from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cparent = db.Column(db.Integer(11), db.ForeignKey('category.idn'))

    children = db.relationship(
        'Category',
        # cascade deletions
        cascade="all",

        # many to one + adjacency list - remote_side
        # is required to reference the 'remote'
        # column in the join condition.
        backref=backref("parent", remote_side='category.id'),

        # children will be represented as a dictionary
        # on the "name" attribute.
        collection_class=attribute_mapped_collection('name'),
        lazy="joined",
        join_depth=3,
    )
    product = db.relationship(
        'Product',
        collection_class=list,
        backref=backref("category", remote_side='category.id'),
        lazy="joined",
        join_depth=3, # так как продукты у меня связаны только с третьим уровнем.
    )

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent


class Product(db.Model):
    id = db.Column(db.Integer(11), primary_key=True)
    id_cat = db.Column(db.Integer(11), db.ForeignKey('category.id'))
    cat = db.relationship("Category")
    data = db.Column(db.String(255))


# root_node = session.query(Category).filter(
#     Category.name == root_node_name).first()