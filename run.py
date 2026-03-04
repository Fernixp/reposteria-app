from app import create_app
from app.extensions import db
from app.models import Pastel

app = create_app()

def poblar_base_de_datos():
    if Pastel.query.count() == 0:
        pasteles_muestra = [
            Pastel(
                nombre="Tarta de Fresa Salvaje",
                descripcion="Deliciosa tarta con fresas frescas y crema batida artesanal.",
                precio=25.50,
                imagen_url="https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=800&q=80"
            ),
            Pastel(
                nombre="Pastel de Chocolate Intenso",
                descripcion="Doble capa de chocolate con un centro líquido derretido.",
                precio=30.00,
                imagen_url="https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80"
            ),
            Pastel(
                nombre="Cheesecake de Frutos Rojos",
                descripcion="Base de galleta crujiente con suave queso crema y frutos del bosque.",
                precio=28.75,
                imagen_url="https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=800&q=80"
            ),
            Pastel(
                nombre="Cupcakes Red Velvet",
                descripcion="Seis mini cupcakes aterciopelados con glaseado de vainilla.",
                precio=15.00,
                imagen_url="https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?auto=format&fit=crop&w=800&q=80"
            ),
            Pastel(
                nombre="Macarons Surtidos",
                descripcion="Docena de macarons franceses de pistacho, frambuesa y limón.",
                precio=22.00,
                imagen_url="https://images.unsplash.com/photo-1569864358642-9d1684040f43?auto=format&fit=crop&w=800&q=80"
            ),
            Pastel(
                nombre="Tarta de Limón y Merengue",
                descripcion="Equilibrio perfecto entre cítrico y dulce con merengue flameado.",
                precio=26.50,
                imagen_url="https://images.unsplash.com/photo-1519869325930-281384150729?auto=format&fit=crop&w=800&q=80"
            )
        ]
        db.session.bulk_save_objects(pasteles_muestra)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        poblar_base_de_datos()
    app.run(debug=True)