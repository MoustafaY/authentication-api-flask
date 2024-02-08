# Authentication Api

## Objective
This is an authentication system that can be used for any web application. Using flask and sqlalchemy, the objective of this project is to authenticate a user when attempting to log in. There are other functionalities to the project that are needed to achieve this objective, such as creating a user, editing the user's name or deleting the user's account. This project uses sqlite for its database, there is only one model which represents the user, each user has a name, email, and a password. Upon creating a new user, using bycrypt, the password is encrypted before it is stored in the database.

## API Calls

**Create a user**
----
Creates and returns a new user

* **URL**
/Users

* **Method**
POST

* **URL Params**
None

* **Data Params**
**Required**
```json
{
  "name": "Moustafa",
  "email": "email@gmail.com",
  "password": "pass"
}
```

* **Success Response**
**Code:** 200 <br />
**Content:** `{"email": "email@gmail.com", "name": "Moustafa", "password": "$2b$12$ZD6hvWZKKWhkGfRu0p3Pq.Jq.Ttq1Ql.0L4t3EUvEi5nvrKmcL3AW"}`

* **Error Response**
  * **Code:** 400 <br />
  **Content:** `{"message": "Invalid input"}` <br />
  OR
  * **Code:** 401 <br />
  **Content:** `{"message": "Email already exists"}`
    
* **Sample Call:** <br />
```json
curl --location 'http://127.0.0.1:5000/Users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Moustafa",
    "email": "email@gmail.com",
    "password": "pass"
}'
```


**Login as a user**
----
Validates and creates a JWT token that can be used for protected api calls

* **URL**
/login

* **Method**
POST

* **URL Params**
None

* **Data Params**
**Required**
```json
{
  "email": "email@gmail.com",
  "password": "pass"
}
```

* **Success Response**
**Code:** 200 <br />
**Content:** `{'message': f"Hello {name}, you are logged in!", 'token': {access_token}}`

* **Error Response**
  * **Code:** 400 <br />
  **Content:** `{"message": "Invalid password"}` or  `{"message": "Invalid input"}` <br />
  OR
  * **Code:** 404 <br />
  **Content:** `{"message": "User was not found"}`
    
* **Sample Call:** <br />
```json
curl --location 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "email@gmail.com",
    "password": "pass"
}'
```
