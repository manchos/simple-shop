from app import db
from sqlalchemy_utils import JSONType, observes
from sqlalchemy_mptt.mixins import BaseNestedSets


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(400), index=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    descr = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.Numeric)
    product_features = db.relationship('Feature',
                                       backref='product',
                                       lazy='dynamic'
                                       )

    def __repr__(self):
        return '<Product {}>'.format(self.model_name)


class Feature(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True)
    feature_type_id = db.Column(db.Integer, db.ForeignKey('feature_types.id'))
    value = db.Column(db.String(400), index=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return '<{}>'.format(self.value)



class Feature_type(db.Model):
    __tablename__ = 'feature_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    default_value = db.Column(db.String(400), index=True)
    feature_type_features = db.relationship('Feature', backref='feature_type')

    def __repr__(self):
        return '<{}>'.format(self.name)


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    descr = db.Column(db.Text)
    products_comp = db.relationship('Product', backref='company', lazy='dynamic')

    def __repr__(self):
        return '<{}>'.format(self.name)



class Category(db.Model, BaseNestedSets):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    details = db.Column(JSONType)
    products = db.relationship('Product', backref='category', lazy='dynamic')

    @staticmethod
    def initial_data_structure():
        db.session.add(Category(name="root"))  # root node
        db.session.add_all(  # first branch of tree
            [
                Category(name="Компютерная техника", parent_id=1),
                Category(name="Компьютеры", parent_id=2),
                Category(name="Ноутбуки", parent_id=3),
                Category(name="Ноутбуки Apple", parent_id=4),
            ]
        )
        db.drop_all()
        db.create_all()
        db.session.commit()

    def __repr__(self):
        return '<Category {}>'.format(self.name)



# product = Feature()
# product.details = {
# 'color': 'red',
# 'type': 'car',
# 'max-speed': '400 mph'
# }
# session.commit()

# class Catalog(db.Model):
#     __tablename__ = 'catalogs'
#     id = db.Column(db.Integer, primary_key=True)
#     product_count = db.Column(db.Integer, default=0)
#
#     @observes('categories.products')
#     def product_observer(self, products):
#         self.product_count = len(products)
#
#     categories = db.relationship('Category', backref='catalog')
#
#
# class Feature(db.Model):
#
#
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)