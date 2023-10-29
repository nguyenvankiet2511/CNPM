def get_categories():
    return [{
        "id":1,
        "name":"Mobile"
    },
        {
            "id": 2,
            "name": "Taplet"
        },
        {
            "id": 3,
            "name": "Phone"
        }
    ]
def get_product(key):
    products =[{
        "id" :1,
        "name":"Iphone",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"
    },{
        "id" :2,
        "name":"Garaxy",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"
    },{
        "id" :3,
        "name":"Iphone",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"
    },{
        "id" :4,
        "name":"Samsung",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"
    },{
        "id" :5,
        "name":"Iphone",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"
    },{
        "id" :6,
        "name":"Samsung",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg"
    }
    ]
    if key:
        products=[ p for p in products if p["name"].find(key)>=0]
    return  products