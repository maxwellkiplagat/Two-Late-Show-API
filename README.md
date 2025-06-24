# Two-Late-Show-API

This is a RESTful API for managing a talk show with **Guests**, **Episodes**, and their **Appearances**, built using Flask, SQLAlchemy, PostgreSQL, and JWT Authentication.



##  Setup Instructions

###  Requirements

- Python 3.10+
- PostgreSQL installed and running
- Virtualenv (recommended)

---

### 1. Clone the Repo

```bash
git clone https://github.com/maxwellkiplagat/Two-Late-Show-API.git
cd Two-Late-Show-API

2. Create a Virtual Environment and Install Dependencies
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Create the .env File
At the root of the project:

env
Copy
Edit
DATABASE_URI=postgresql://your_db_user:your_db_password@localhost:5432/your_db_name
JWT_SECRET_KEY=your_secret_key_here
Replace your_db_user, your_db_password, and your_db_name with your actual PostgreSQL credentials.

4. Create the Database
bash
Copy
Edit
createdb your_db_name

 How to Run
1. Migrate / Create Tables
Handled automatically in the seed file.

2. Seed the Database
bash
Copy
Edit
python seed.py
You should see:

csharp
Copy
Edit
Smooth as butter 🧈
3. Run the Flask Server
bash
Copy
Edit
flask --app server.app run
API will be live at:
👉 http://127.0.0.1:5000

🔐 Auth Flow
1. Register
POST /register

Request Body:

json
Copy
Edit
{
  "username": "maxwell",
  "password": "password123"
}
Response:

json
Copy
Edit
{
  "message": "User registered"
}
2. Login
POST /login

Request Body:

json
Copy
Edit
{
  "username": "maxwell",
  "password": "password123"
}
Response:

json
Copy
Edit
{
  "access_token": "your.jwt.token.here"
}
3. Using the Token
For protected routes (like /appearances), include this in the headers:

makefile
Copy
Edit
Authorization: Bearer your.jwt.token.here

🧪 Sample POST Request: Appearance
Endpoint: /appearances
Auth: ✅ Bearer Token Required

Headers:

makefile
Copy
Edit
Authorization: Bearer your.jwt.token.here
Body:

json
Copy
Edit
{
  "rating": 9.5,
  "guest_id": 1,
  "episode_id": 2
}
Response:

json
Copy
Edit
{
  "message": "Appearance created"
}
 Postman Usage Guide
Import endpoints manually or use a collection.

Register a user at /register

Log in via /login to get the token.

Add Authorization: Bearer <token> to any protected requests (like /appearances).

Example setup in Postman:

Authorization tab:
Type: Bearer Token
Token: paste your JWT here

