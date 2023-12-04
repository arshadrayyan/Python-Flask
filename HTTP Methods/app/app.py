from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))

# Route With Navigation using /square
@app.route('/square', methods=['GET'])
def squarenumber():
    if request.method == 'GET':
        if request.args.get('num') is None:
            return render_template('squarenum.html')
        elif request.args.get('num') == '':
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number = request.args.get('num')
            sq = int(number) * int(number)
            return render_template('answer.html', squareofnum=sq, num=number)

# Default Route
@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)