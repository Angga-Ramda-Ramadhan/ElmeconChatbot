from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os


load_dotenv('.env')
print(os.environ.get('VERIFY_TOKEN'))

token_verif = 'elm2026'
app = Flask(__name__)
@app.route('/webhook', methods=['POST', 'GET'])
def webhook_elm():

    
    if request.method == 'GET':
        
        token = request.args.get('hub.verify_token')
        print(token)
        challenge = request.args.get('hub.challenge')
        print(challenge)
        if token == token_verif:
            return challenge, 200
        
        else:
            return "failed", 403
        
    elif request.method == 'POST':
        data = request.json
        print(data)
        return data


