# Example 11: using Flask with Marshmallow
from flask import Flask, request, jsonify

# We import models as well as schemas
from flask_examples.models import db, Artist
from flask_examples.schemas import ma, ArtistSchema

app = Flask(__name__)

# Configure database as in Example 10
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mypass@localhost/Chinook?charset=utf8mb4"

db.init_app(app)
# Marshmallow has also to be initialized. Remember that ma
# has to be initialized AFTER db engine.
ma.init_app(app)

# Instantiate schemas.
artist_schema = ArtistSchema()  # This one is for single employee
artists_schema = ArtistSchema(many=True)  # And this one for lists

# Resource for adding new artist
@app.route("/artists/", methods=["POST"])
def add_artist():
    data = request.get_json()
    # Schemas can validate incoming data. The validate methods
    # returns "errors" dict. If it is empty, the object is valid.
    errors = artist_schema.validate(data)
    if errors:
        # If there were some errors, we return them with 400 Bad Request status.
        response = jsonify(errors=errors)
        response.status_code = 400
        return response
    # In case there are no errors, we make instance of the Model and save it.
    artist = artist_schema.make_instance(data)
    db.session.add(artist)
    db.session.commit()
    # Schemas also have
    return artist_schema.jsonify(artist)


@app.route("/artists/", methods=["GET"])
def get_all_artists():
    return artists_schema.jsonify(db.sessoin.Query(Artist).all())


# Resource for getting artist of given ID
@app.route("/artists/<int:artist_id>", methods=["GET"])
def get_artist(artist_id):
    emp = db.session.query(Artist).filter_by(id=artist_id).first_or_404()
    return artist_schema.jsonify(emp)


if __name__ == "__main__":
    app.run()
