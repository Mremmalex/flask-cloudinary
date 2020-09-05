from flask import Blueprint, request, jsonify, render_template
from api.model.productsModel import productTable
from api import app
import secrets
import os
from PIL import Image
import cloudinary as Cloud
import api.config

products = Blueprint('products', __name__)

Cloud.config(
    cloud_name=os.environ.get('cloud_name'),
    api_key=os.environ.get('api_key'),
    api_secret=os.environ.get('api_secret_key')
)


def saveProductImage(image):
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(image.filename)
    image_fn = random_hex + ext
    image_path = os.path.join(app.root_path, "static/productImage", image_fn)

    size = (125, 125)
    i = Image.open(image)
    i.thumbnail(size)
    i.save(image_path)

    return image_path


def saveImageToCloud(image):
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(image.filename)
    image_fn = random_hex + ext

    size = (125, 125)
    i = Image.open(image)
    i.thumbnail(size)
    image_url = Cloud.CloudinaryImage(image_fn)
    return image_url.url


@products.route("/product", methods=['GET', 'POST'])
def create_product():
    if request.method == "POST":
        productName = request.form['productName']
        productImg = request.files['productImage']
        productDesc = request.form['productDesc']
        productPrice = request.form['productPrice']
        print(productName)
        print(productImg)
        print(productDesc)
        print(productPrice)

        image_path = saveImageToCloud(productImg)
        print(image_path)

        productTable.newProduct(productName, image_path,
                                productDesc, productPrice)
        # return jsonify({'output':"prodiuct recieved"})

    if request.method == "GET":
        output = []
        results = productTable.getAllProducts()
        for result in results:
            output.append(result)
        return jsonify({'output': output})
        # return render_template('loadProduct.html')
    return jsonify({"message": "good"})
