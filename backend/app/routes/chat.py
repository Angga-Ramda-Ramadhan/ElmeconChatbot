from flask import Blueprint, request, g, jsonify
# from db import connection_db
from model import chat_with_tools



chat_bp = Blueprint('chat_bp', __name__)
@chat_bp.route('/chat', methods=['POST'])
def chat():
    # print(os.environ.get('OPENAI_API_KEY'))
    data = request.json
    message = data.get('message')

    results = chat_with_tools(msg=message)


    return jsonify(results)