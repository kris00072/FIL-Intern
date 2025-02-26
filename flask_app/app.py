from flask import Flask, request, jsonify, Response
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/car_db"
# mongo = PyMongo(app)

# MongoDB Atlas Connection
MONGO_URI = "mongodb+srv://kris6uu7:chessChess2*2*@krishanfil.1vix8.mongodb.net/?retryWrites=true&w=majority&appName=krishanfil"

try:
    client = MongoClient(MONGO_URI)
    db = client["car_db"]  # Make sure this matches your database name in Atlas
    cars_collection = db["cars"]
    print("✅ Connected to MongoDB Atlas successfully!")
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")

# Test route
@app.route("/")
def demo():
    return Response("Hello from Flask!")

# Create a new car (POST)
@app.route("/cars", methods=["POST"])
def add_car():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    car_id = cars_collection.insert_one(data).inserted_id
    return jsonify({"message": "Car added", "id": str(car_id)}), 201

# Get all cars (GET)
@app.route("/cars", methods=["GET"])
def get_cars():
    cars = list(cars_collection.find({}, {"_id": 0}))  # Exclude _id
    return jsonify(cars), 200

# Get a single car by model (GET)
@app.route("/cars/<model>", methods=["GET"])
def get_car(model):
    car = cars_collection.find_one({"model": model}, {"_id": 0})
    if car:
        return jsonify(car), 200
    return jsonify({"error": "Car not found"}), 404

# Update a car by model (PUT)
@app.route("/cars/<model>", methods=["PUT"])
def update_car(model):
    data = request.json
    updated_car = cars_collection.find_one_and_update(
        {"model": model},
        {"$set": data},
        return_document=True
    )
    if updated_car:
        return jsonify({"message": "Car updated"}), 200
    return jsonify({"error": "Car not found"}), 404

# Delete a car by model (DELETE)
@app.route("/cars/<model>", methods=["DELETE"])
def delete_car(model):
    result = cars_collection.delete_one({"model": model})
    if result.deleted_count:
        return jsonify({"message": "Car deleted"}), 200
    return jsonify({"error": "Car not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')