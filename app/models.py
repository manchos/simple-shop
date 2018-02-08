from app import db
from sqlalchemy_utils import JSONType, observes


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(120), index=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    descr = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.Numeric)

    def __repr__(self):
        return '<Product {}>'.format(self.model_name)


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    descr = db.Column(db.Text)
    products_comp = db.relationship('Product', backref='company')

    def __repr__(self):
        return '<{}>'.format(self.name)



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    details = db.Column(JSONType)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalogs.id'))
    products = db.relationship('Product', backref='category')

    def __repr__(self):
        return '<{}>'.format(self.name)

# product = Feature()
# product.details = {
# 'color': 'red',
# 'type': 'car',
# 'max-speed': '400 mph'
# }
# session.commit()


class Catalog(db.Model):
    __tablename__ = 'catalogs'
    id = db.Column(db.Integer, primary_key=True)
    product_count = db.Column(db.Integer, default=0)

    @observes('categories.products')
    def product_observer(self, products):
        self.product_count = len(products)

    categories = db.relationship('Category', backref='catalog')
#
#
# class Feature(db.Model):
#
#
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)