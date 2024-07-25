from flask import Flask

def create_app():
    app = Flask(__name__)
    app.debug = True


    from petfax import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)


    @app.route('/')
    def index():
        return 'Hello, PetFax!'

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
