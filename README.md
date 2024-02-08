# authentication-api-flask

## Objective
This is an authentication system that can be used for any web application. Using flask and sqlalchemy, the objective of this project is to authenticate a user when attempting to log in. There are other functionalities to the project that are needed to achieve this objective, such as creating a user, editing the user's name or deleting the user's account. This project uses sqlite for its database, there is only one model which represents the user, each user has a name, email, and a password. Upon creating a new user, using bycrypt, the password is encrypted before it is stored in the database.

