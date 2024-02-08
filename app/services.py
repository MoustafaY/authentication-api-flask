from app.daos import user_dao
from app.extensions  import bcrypt

class UserService:
    def getUsers(self):
        queryUsers = user_dao.getUsers()
        users = []
        for qUser in queryUsers:
            users.append(qUser.toJSON())
        return users
    
    def getUser(self, email):
        user = user_dao.getUser(email)
        if user is None:
            raise TypeError
        return user.toJSON()
    
    def createUser(self, name, email, password):
        hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')
        user = user_dao.createUser(name, email, hashedPassword)
        return user.toJSON()
    
    def deleteUser(self, email):
        return user_dao.deleteUser(email)
    
    def updateUser(self, email, name):
        user = user_dao.getUser(email)
        if user is None:
            raise TypeError
        user.name = name
        user_dao.updateUser()
        return user.toJSON()
    
    def deleteUsers(self):
        user_dao.deleteUsers()
    
    def checkUserPassword(self, inputPassword, userPassword):
        return bcrypt.check_password_hash(inputPassword, userPassword)

user_service = UserService()