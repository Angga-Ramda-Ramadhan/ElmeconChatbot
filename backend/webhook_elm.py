from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/webhook', methods=['POST', 'GET'])
def webhook_elm():

    if request.method == 'POST':
        data = request.json

        print('Received POST data: ', data)

        return jsonify({
            'message':'Berhasil terima post webhook'
        })
    
    elif request.method == 'GET':
        data = request.json
        print('Received Get Data: ', data)
        return jsonify({
            'message':'Berhasil terima get webhook'
        })


if __name__ == '__main__':
    app.run(host='88.222.215.217', debug=True, port=5004)
