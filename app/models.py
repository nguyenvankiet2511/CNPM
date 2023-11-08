from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


# class Category(db.Model):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, unique=True)
#     products = relationship('product', backref='category', lazy=True)
#
#
# class Product(db.Model):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, unique=True)
#     price = Column(Float, default=0)
#     img = Column(String(100), nullable=True)
#     category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class Category(db.Model):
    __tablename__ = 'category'


    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'


    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    img = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
    p1= Product(name='Iphone13',price=200000000,img='https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg',category_id=1)
    db.session.add(p1)
    db.session.commit()
        # db.create_all()
