from datetime import datetime
from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    text = db.Column(db.Text)
    theme = db.Column(db.String(100))
    tag = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
