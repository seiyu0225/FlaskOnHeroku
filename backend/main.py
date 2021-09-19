from flask import *
from api import text_count_bp
import pyrebase

config = {
  "apiKey" : "AIzaSyBqw-_4pLOOAMArM8k6Iqla37aWk1T3enY",
  "authDomain" : "flaskonheroku.firebaseapp.com",
  "projectId" : "flaskonheroku",
  "storageBucket" : "flaskonheroku.appspot.com",
  "messagingSenderId" : "644162721537",
  "appId" : "1:644162721537:web:ed2cfbd05bb5919e706d00",
  "measurementId" : "G-80ZC9Y9D9H",
  "databaseURL" : "https://post_text.asia-northeast3.firebaseio.com"
}

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
    # POSTでリクエストされたら
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    # formから値を取得
    name = request.json['name']
    post_text = db.child("post_text").order_by_child("name").equal_to(name).get()
    
    ret_object = []
    for dic in post_text.each():
        ret_object.append(
            {
                "text" : dic.val()["text"]
            }
        )
    return jsonify(ret_object)


if __name__ == '__main__':
    app.run()