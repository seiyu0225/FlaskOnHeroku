from flask import *

app = Flask(__name__, static_folder='./templates/static', template_folder='./templates')

@app.route('/')
def index():
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