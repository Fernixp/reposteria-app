from app import create_app
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Esto crea las tablas en tu MySQL (puerto 3307)
        db.create_all() 
    app.run(debug=True)