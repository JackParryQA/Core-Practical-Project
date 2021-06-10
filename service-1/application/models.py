from application import db

class MLBDraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(2), nullable=False)
    pick = db.Column(db.Integer, nullable=False)
