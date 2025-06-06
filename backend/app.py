from backend.flask import Flask
from backend.booking import booking_bp
from backend.notify import notify_bp
from backend.auth import auth_bp
from backend.export import export_bp

app = Flask(__name__)
app.register_blueprint(booking_bp, url_prefix="/api/book")
app.register_blueprint(notify_bp, url_prefix="/api/notify")
app.register_blueprint(auth_bp, url_prefix="/api/login")
app.register_blueprint(export_bp, url_prefix="/api/export")

if __name__ == "__main__":
    app.run(debug=True)
