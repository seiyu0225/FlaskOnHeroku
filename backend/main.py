from flask import Flask, render_template
from api import text_count_bp


app = Flask(__name__, static_folder='./templates/static', template_folder='./templates')
# app = Flask(__name__)
app.register_blueprint(text_count_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()