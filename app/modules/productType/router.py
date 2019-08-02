from app.modules.productType.service import ProductType
from flask import Blueprint, request, jsonify
from app.utils.jwt import protected, adminOnly

product_type_module = Blueprint('product_type_module', __name__)

@product_type_module.route('/api/module/product/type', methods=['POST'])
@protected
@adminOnly
def create(data):
    service = ProductType()

    body = request.get_json(silent=True)

    data = {"jwt_user": data['username']}

    main_dict = {**body, **data}

    message = service.create(main_dict)

    return jsonify(message["message"]), message["status"]



@product_type_module.route('/api/module/product/types', methods=['GET'])
@protected
@adminOnly
def getAll(data):
    service = ProductType()

    data = {"jwt_user": data['username']}

    message = service.gets(data)

    return jsonify(message["message"]), message["status"]
