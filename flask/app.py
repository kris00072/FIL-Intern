from flask import Flask, render_template, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

rs = {
    1: {'name': 'Krishan', 'class': 'nginx'},
    2: {'name': 'Hey', 'class': 'gunicorn'},
    3: {'name': 'hohoho', 'class': 'vite'},
}


class ItemList(Resource):
    def get(self):
        return rs  

class SingleItem(Resource):
    def get(self, pk):
        return rs.get(pk, {"error": "Item not found"})  

class PostItem(Resource):
    def post(self):
        data = request.json
        if not data or 'name' not in data or 'class' not in data:
            return {"error": "Invalid input, 'name' and 'class' are required"}, 400
        
        new_id = max(rs.keys()) + 1  
        rs[new_id] = data  
        return {"message": "Item added", "id": new_id}, 201 



api.add_resource(ItemList, '/items')  
api.add_resource(SingleItem, '/items/<int:pk>')  
api.add_resource(PostItem, '/items/new')  

# Serve HTML (Optional)
@app.route('/fil')
def hello():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
