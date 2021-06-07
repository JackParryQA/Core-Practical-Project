from application import db

class MLBDraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(2), nullable=False)
    pick = db.Column(db.Integer, nullable=False)
