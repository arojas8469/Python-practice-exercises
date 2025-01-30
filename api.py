from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800},
    {"id": 3, "name": "Headphones", "price": 150}
]

# Route: Welcome page (Root endpoint)
@app.route("/")
def home():
    return "<h1>Welcome to the Product API</h1><p>Use /api/product to get products.</p>"

# Route: About page
@app.route("/about")
def about():
    return "<h1>About Us</h1><p>This is a simple REST API using Flask.</p>"

# Route: GET /api/product - Returns list of products
@app.route("/api/product", methods=["GET"])
def get_products():
    return jsonify(products)

# Route: GET /api/product/count - Returns product count
@app.route("/api/product/count", methods=["GET"])
def get_product_count():
    return jsonify({"count": len(products)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

