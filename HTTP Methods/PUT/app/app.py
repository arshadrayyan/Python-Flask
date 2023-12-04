from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for demonstration
data = {'name': 'John Doe', 'age': 25}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data=data)

@app.route('/', methods=['PUT'])
def update_data():
    # Assume the updated data is sent in the request payload as JSON
    updated_data = request.get_json()
    
    # Update the existing data with the new values
    data.update(updated_data)
    
    # Redirect to the home page after the update
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)