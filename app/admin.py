from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product
from app import app, db

admin = Admin(app=app, name="QUAN TRI BAN HANG", template_mode='bootstrap4')
admin.add_view((ModelView(Category, db.session)))
admin.add_view((ModelView(Product, db.session)))
