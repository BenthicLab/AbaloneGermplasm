from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    email = db.Column(db.String(255), nullable=False, primary_key=True, unique=True)
    username = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # 1.function
    # def generate_password_hash(self, origin_password):
    #   self.password_hash = generate_password_hash(origin_password)

    # 2.property
    @property
    def hash_password(self):
        return ""

    @hash_password.setter
    def hash_password(self, origin_password):
        self.password_hash = generate_password_hash(origin_password)

    def check_password_hash(self, query_password):
        return check_password_hash(self.password_hash, query_password)

    def to_dict(self):
        return {'email': self.email, 'username': self.username}


class Germplasm(db.Model):
    __tablename__ = "germplasm"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    species = db.Column(db.String(255), nullable=False)
    pop = db.Column(db.String(255), default='')
    strain = db.Column(db.String(255), default='')
    total = db.Column(db.String(255), default='')
    year1_percent = db.Column(db.String(255), default='')
    year2_percent = db.Column(db.String(255), default='')
    year2_length = db.Column(db.String(255), default='')
    year2_weight = db.Column(db.String(255), default='')

    def to_dict(self):
        return {
            'id': self.id,
            'species': self.species,
            'pop': self.pop,
            'strain': self.strain,
            'total': self.total,
            'year1_percent': self.year1_percent,
            'year2_percent': self.year2_percent,
            'year2_length': self.year2_length,
            'year2_weight': self.year2_weight,
        }
