# Authentication Api

## Objective
This is an authentication system that can be used for any web application. Using flask and sqlalchemy, the objective of this project is to authenticate a user when attempting to log in. There are other functionalities to the project that are needed to achieve this objective, such as creating a user, editing the user's name or deleting the user's account. This project uses sqlite for its database, there is only one model which represents the user, each user has a name, email, and a password. Upon creating a new user, using bycrypt, the password is encrypted before it is stored in the database.

### API Calls

**Create a user**
----
Creates and returns a new user

* **URL** <br />
/Users

* **Method** <br />
POST

* **URL Params** <br />
None

* **Data Params** <br />
**Required:** <br />
```json
{
  "name": "Moustafa",
  "email": "email@gmail.com",
  "password": "pass"
}
```

* **Success Response** <br />
**Code:** 200 <br />
**Content:** `{"email": "email@gmail.com", "name": "Moustafa", "password": "$2b$12$ZD6hvWZKKWhkGfRu0p3Pq.Jq.Ttq1Ql.0L4t3EUvEi5nvrKmcL3AW"}`

* **Error Response** <br />
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

* **URL** <br />
/login

* **Method** <br />
POST

* **URL Params** <br />
None

* **Data Params** <br />
**Required:** <br />
```json
{
  "email": "email@gmail.com",
  "password": "pass"
}
```

* **Success Response** <br />
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


**Look up user information**
----
A user looks up their information

* **URL** <br />
/User

* **Method** <br />
GET

* **URL Params** <br />
**Required:** `email=[email address of user]`

* **Data Params** <br />
None

* **Success Response** <br />
**Code:** 200 <br />
**Content:** `{"email": "email@gmail.com", "name": "Moustafa", "password": "$2b$12$l.B3Yag.9VB4udQQaQsISeY0dXeboKK5KHWjaLoFq.L9uCMWfxY3a"}`

* **Error Response**
  * **Code:** 400 <br />
  **Content:** `{"message": "Invalid input"}` <br />
  OR
  * **Code:** 404 <br />
  **Content:** `{"message": "User was not found"}`
    
* **Sample Call:** <br />
```json
curl --location 'http://127.0.0.1:5000/User?email=email%40gmail.com' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNzM5NTU5NCwianRpIjoiYjU2OTQzM2MtOTQ4Zi00YmRiLWIyZGQtMWRlY2Y1NWY4NGU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsQGdtYWlsLmNvbSIsIm5iZiI6MTcwNzM5NTU5NCwiY3NyZiI6IjFkOWE0OTgxLWExNTQtNDYzZS1iNjAwLTAzNGQyODhmZTMwZSIsImV4cCI6MTcwNzM5NjQ5NH0.ciqqnPV-YqZ-WwZe3IbL9fyhLQB0byuOHux8XMBkowo'
```


**Change user information**
----
A user changes their information

* **URL** <br />
/User

* **Method** <br />
PUT

* **URL Params** <br />
None

* **Data Params** <br />
```json
{
  "email": "email@gmail.com",
  "name": "Lily"
}
```

* **Success Response** <br />
**Code:** 200 <br />
**Content:** `{"email": "email@gmail.com", "name": "Lily", "password": "$2b$12$l.B3Yag.9VB4udQQaQsISeY0dXeboKK5KHWjaLoFq.L9uCMWfxY3a"}`

* **Error Response**
  * **Code:** 400 <br />
  **Content:** `{"message": "Invalid input"}` <br />
  OR
  * **Code:** 404 <br />
  **Content:** `{"message": "User was not found"}`
    
* **Sample Call:** <br />
```json
curl --location --request PUT 'http://127.0.0.1:5000/User' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNzM5NTU5NCwianRpIjoiYjU2OTQzM2MtOTQ4Zi00YmRiLWIyZGQtMWRlY2Y1NWY4NGU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsQGdtYWlsLmNvbSIsIm5iZiI6MTcwNzM5NTU5NCwiY3NyZiI6IjFkOWE0OTgxLWExNTQtNDYzZS1iNjAwLTAzNGQyODhmZTMwZSIsImV4cCI6MTcwNzM5NjQ5NH0.ciqqnPV-YqZ-WwZe3IbL9fyhLQB0byuOHux8XMBkowo' \
--data-raw '{
    "email": "email@gmail.com",
    "name": "Lily"
}'
```

**Delete user**
----
A user deletes their account

* **URL** <br />
/User

* **Method** <br />
DELETE

* **URL Params** <br />
**Required:** `email=[email address of user]`

* **Data Params** <br />
None

* **Success Response** <br />
**Code:** 200 <br />
**Content:** `{'message': 'User deleted'}`

* **Error Response**
  * **Code:** 400 <br />
  **Content:** `{"message": "Invalid input"}` <br />
  OR
  * **Code:** 404 <br />
  **Content:** `{"message": "User was not found"}`
    
* **Sample Call:** <br />
```json
curl --location --request DELETE 'http://127.0.0.1:5000/User?email=email%40gmail.com' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNzM5NjU1NSwianRpIjoiMTE5ZDc4OTktMDE2My00YzE2LWFhMmItNjg5ZjdlNGIyOGU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsQGdtYWlsLmNvbSIsIm5iZiI6MTcwNzM5NjU1NSwiY3NyZiI6ImJkOGEwZDIyLTNmZDMtNDM0ZC05Y2Y1LTRjMmYzY2Y3Zjg4NSIsImV4cCI6MTcwNzM5NzQ1NX0.2a0U-uItzNHJ7KUOQg1DlM8Zyz3poKEsaHm4BIR0ZfI'
```


**Get all users**
----
A call used for development purpose only, returns all the users in the database

* **URL** <br />
/Users

* **Method** <br />
GET

* **URL Params** <br />
None

* **Data Params** <br />
None

* **Success Response** <br />
**Code:** 200 <br />
**Content:** `[{all users}]`
    
* **Sample Call:** <br />
```json
curl --location 'http://127.0.0.1:5000/Users'
```

**Delete all users**
----
A call used for development purpose only, deletes all the users in the database

* **URL** <br />
/Users

* **Method** <br />
DELETE

* **URL Params** <br />
None

* **Data Params** <br />
None

* **Success Response** <br />
**Code:** 200 <br />
**Content:** `{'message': 'Table reset'}`
    
* **Sample Call:** <br />
```json
curl --location --request DELETE 'http://127.0.0.1:5000/Users'
```
