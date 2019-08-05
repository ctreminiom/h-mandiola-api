from app.modules.product.service import Product
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

product_module = Blueprint('product_module', __name__)

@product_module.route('/api/module/product', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = Product()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}

    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]



@product_module.route('/api/module/products', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = Product()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]
