# models/certificate.py

from . import db

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False)
    issued_date = db.Column(db.String(100))
    expiration_date = db.Column(db.String(100))
    certificate_data = db.Column(db.Text)

    def __repr__(self):
        return f"<Certificate {self.domain}>"
