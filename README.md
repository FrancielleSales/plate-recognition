# PLATE RECOGNITION

Tool for automatic recognition and detection of Brazilian license plates in images

## Creating the development environment

### Requirements

- Node.js
- Postgresql
- Python

### Database

**With PostgreSQL installed, access it:**

```sh
psql -U postgres
```

**Create a user to manage the database:**

```sh
CREATE USER dbpr WITH PASSWORD '321';
```

**Create the database:**

```sh
CREATE DATABASE db_pr;
```

**Grant permissions to the user:**

```sh
GRANT ALL PRIVILEGES ON DATABASE db_pr TO dbpr;
```

To exit the shell, use: \q

**To create the database tables and add users for testing:**

```sh
cd /database
python3 config.py
```

**To create a backup:**

```sh
cd /database/backups
python3 backup_database.py
```

### Backend

**Install requirements**

```sh
cd backend
pip install -r requirements.txt
```

**Create migrations for all apps**

```sh
cd /backend
python manage.py makemigrations
```

**For apply migrations**

```sh
cd /backend
python manage.py migrate
```

**For check migrations**

```sh
cd /backend
python manage.py showmigrations
```

**if it is necessary to run fake migration**

```sh
cd /backend
python manage.py migrate <app_name> <migration_name> --fake
```

**Start backend**

```sh
cd /backend
python3 manage.py runserver
```

### Frontend

**Installation of dependencies**

```sh
cd frontend
npm install
```

**Start frontend**

```sh
npm run serve
```

**Ports**

> Frontend: localhost:8080
> Backend: localhost:8000
