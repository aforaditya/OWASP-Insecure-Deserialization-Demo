import pickle
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    session_data = request.cookies.get('session')
    user_data = session_data and pickle.loads(base64.b64decode(session_data))
    return 'Hello from web server'

app.run(debug=True)