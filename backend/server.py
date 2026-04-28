from app import create_app

app = create_app()
# socketio.init_app(app)

if __name__ == '__main__':
    # app.run(debug=True,host="0.0.0.0")
    app.run(host="127.0.0.1", port=5003, debug=True)
    