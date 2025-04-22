from . import db

class Mural(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(6), unique=True, nullable=False)
    titulo = db.Column(db.String(120), nullable=False)
    feedbacks = db.relationship('Feedback', backref='mural', cascade="all, delete", lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    mural_id = db.Column(db.Integer, db.ForeignKey('mural.id'), nullable=False)
