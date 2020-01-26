# Part of example 11: Marshmallow schemas
from flask_marshmallow import Marshmallow
from flask_examples import models

# First we create Marshmallow object
ma = Marshmallow()

# And then define schemas.
# Because we use flask_marshmallow, we only need to define
# meta information about the model, and the schemas will
# be filled accordingly. Otherwise we would have
# to define it ourselves.
class GenreSchema(ma.ModelSchema):
    class Meta:
        model = models.Genre


class ArtistSchema(ma.ModelSchema):
    class Meta:
        model = models.Artist
