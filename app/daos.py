from app.models import User
from app.extensions import db

class UserDAO:

    def __init__(self, model):
        self.model = model

    def getUsers(self):
        users = db.session.query(self.model).all()
        return users

    def getUser(self, email):
        user = db.session.query(self.model).filter_by(email = email).one_or_none()
        return user
    
    def createUser(self, name, email, password):
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
    
    def deleteUser(self, email):
        user = db.session.query(self.model).filter_by(email = email).one_or_none()
        if user is None:
            raise TypeError
        db.session.delete(user)
        db.session.commit()
        return "User deleted"
    
    def deleteUsers(self):
        User.query.delete()
        db.session.commit()
    
    def updateUser(self):
        db.session.commit()
user_dao = UserDAO(User)