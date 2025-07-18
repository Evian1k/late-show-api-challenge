from flask import Flask
from server.config import Config
from server.extensions import db, migrate, jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

@app.route("/")
def index():
    return {"message": "Welcome to the Late Show API!"}

# Register blueprints
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.auth_controller import auth_bp

app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
