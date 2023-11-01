from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    key = request.args.get("key")
    cates = dao.get_categories()
    prod = dao.get_product(key)
    return render_template('index.html', categories=cates, products=prod)


if __name__ == '__main__':
    app.run(debug=True)
