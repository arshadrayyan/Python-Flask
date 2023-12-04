from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data (you can replace this with your own data storage mechanism)
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    {"id": 4, "name": "Item 4"},
    {"id": 5, "name": "Item 5"},
    {"id": 6, "name": "Item 6"},
    {"id": 7, "name": "Item 7"},
    {"id": 8, "name": "Item 8"},
    {"id": 9, "name": "Item 9"},
    {"id": 10, "name": "Item 10"},
    {"id": 11, "name": "Item 11"},
]

# Route to display the initial data
@app.route('/')
def index():
    return render_template('index.html', data=data)

# Route to handle the DELETE request
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    deleted_item = None

    for item in data:
        if item['id'] == item_id:
            deleted_item = item
            data.remove(item)
            break

    if deleted_item:
        return jsonify({"deleted_item": deleted_item, "status": "Item deleted successfully"})
    else:
        return jsonify({"status": "Item not found"})

if __name__ == '__main__':
    app.run(debug=True)