from perionet import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameLast = db.Column(db.String(30), nullable=False)
    nameFirst = db.Column(db.String(30), nullable=False)
    nameDob = db.Column(db.String(15), default='01/01/1800')

    def __repr__(self):
        return f"Patient('{self.nameFirst}', '{self.nameLast}')"
