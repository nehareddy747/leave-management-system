from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.leave_routes import leave_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(leave_bp, url_prefix='/api/leaves')

    @app.route('/health', methods=['GET'])
    def health_check():
        return {"status": "ok", "message": "Server is running"}

    return app
