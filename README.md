# Late Show API Challenge

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
   pipenv shell
   ```
2. **Create PostgreSQL database:**
   ```sql
   CREATE DATABASE late_show_db;
   ```
3. **Set environment variables:**
   - Edit `server/config.py` with your DB credentials if needed.
   - Optionally set `JWT_SECRET_KEY` in your environment.

4. **Run migrations and seed data:**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   python server/seed.py
   ```

## How to Run

```bash
export FLASK_APP=server/app.py
flask run
```

## Auth Flow
- Register: `POST /register` (username, password)
- Login: `POST /login` (returns JWT)
- Use JWT as `Authorization: Bearer <token>` for protected routes

## Routes
| Route                | Method | Auth? | Description                       |
|----------------------|--------|-------|-----------------------------------|
| /register            | POST   | ❌    | Register a user                   |
| /login               | POST   | ❌    | Log in, get JWT                   |
| /episodes            | GET    | ❌    | List episodes                     |
| /episodes/<id>       | GET    | ❌    | Get episode + appearances         |
| /episodes/<id>       | DELETE | ✅    | Delete episode + appearances      |
| /guests              | GET    | ❌    | List guests                       |
| /appearances         | POST   | ✅    | Create appearance                 |

## Postman
- Import `challenge-4-lateshow.postman_collection.json` for testing.
- Register, login, and use JWT for protected endpoints.

## GitHub
- Push your code to a public repo and share the link.

---

**Good luck!**
