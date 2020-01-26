# Models for example 10 and 11
from flask_sqlalchemy import SQLAlchemy

# The db object defined below will serve as a DeclarativeBase and
# db engine.
db = SQLAlchemy()

# Models are defined as usual with SQLAlchemy, but with all objects (Columns, Table etc.)
# from db rather than raw SQLAlchemy


class Artist(db.Model):
    __tablename__ = "Artist"
    id = db.Column(db.Integer, primary_key=True, name="ArtistId")
    name = db.Column(db.String(120), name="Name")

    albums = db.relationship("Album", back_populates="artist")

    def __repr__(self):
        return f"<Artist(id={self.id}, name={self.name})>"


class Album(db.Model):
    __tablename__ = "Album"
    id = db.Column(db.Integer, primary_key=True, name="AlbumId")
    title = db.Column(db.String(160), name="Title")
    artist_id = db.Column(db.Integer, db.ForeignKey("Artist.ArtistId"), name="ArtistId")

    artist = db.relationship(Artist, back_populates="albums")
    tracks = db.relationship("Track", back_populates="album")

    def __repr__(self):
        return f"<Album(id={self.id}, title={self.title})>"


class MediaType(db.Model):
    __tablename__="MediaType"
    id = db.Column(db.Integer, primary_key=True, name="MediaTypeId")
    name = db.Column(db.String(120), name="Name")


class Genre(db.Model):
    __tablename__ = "Genre"
    id = db.Column(db.Integer, primary_key=True, name="GenreId")
    name = db.Column(db.String(120), name="Name")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Track(db.Model):
    __tablename__ = "Track"
    id = db.Column(db.Integer, primary_key=True, name="TrackId")
    name = db.Column(db.String(200), name="Name")
    album_id = db.Column(db.Integer, db.ForeignKey("Album.AlbumId"), name="AlbumId")
    media_type_id = db.Column(db.Integer, db.ForeignKey("MediaType.MediaTypeId"), name="MediaTypeId")
    genre_id = db.Column(db.Integer, db.ForeignKey("Genre.GenreId"), name="GenreId")
    composer = db.Column(db.String(220), name="Composer")
    milliseconds = db.Column(db.Integer, name="Milliseconds")
    bytes = db.Column(db.Integer,name="Bytes")
    unit_price = db.Column(db.Float, name="UnitPrice")

    album = db.relationship(Album, back_populates="tracks")
    genre = db.relationship(Genre)
    media_type = db.relationship(MediaType)

    def __repr__(self):
        return f"<Track(name='{self.name}')>"


playlists_tracks = db.Table(
    "PlaylistTrack",
    db.Model.metadata,
    db.Column("PlaylistId", db.ForeignKey("Playlist.PlaylistId"), primary_key=True),
    db.Column("TrackId", db.ForeignKey("Track.TrackId"), primary_key=True)
)


class Playlist(db.Model):
    __tablename__ = "Playlist"
    id = db.Column(db.Integer, primary_key=True, name="PlaylistId")
    name = db.Column(db.String(120), name="Name")

    tracks = db.relationship(Track, secondary=playlists_tracks)
