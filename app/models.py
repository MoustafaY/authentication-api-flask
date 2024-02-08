from app.extensions import db

class User(db.Model):
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def toJSON(self):
        return{
            'name': self.name,
            'email': self.email,
            'password': self.password
        }