from .chat import chat_bp


def register_app(app):
    app.register_blueprint(chat_bp)
    