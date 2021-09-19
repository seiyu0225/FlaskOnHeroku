from flask import *
from api import text_count_bp
import pyrebase

app = Flask(__name__, static_folder='./templates/static', template_folder='./templates')
# app = Flask(__name__)
app.register_blueprint(text_count_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/api/user_name/post', methods=['POST']) 
# basic関数を定義
def name_post():
    ret = []
    for _ in range(5):
        ret.append(
            {
                "text" : "aaa",
                "index" : _
            }
        )
    return jsonify(ret)


if __name__ == '__main__':
    app.run()