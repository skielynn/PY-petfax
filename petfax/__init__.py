from flask import Flask

def create_app():
    app = Flask(__name__)
    app.debug = True

    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    return app
