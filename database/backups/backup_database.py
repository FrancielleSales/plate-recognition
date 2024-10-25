import subprocess
import datetime
import os

# Database Settings
DATABASE = {
    'NAME': 'pr_db',
    'USER': 'user',
    'PASSWORD': '321',
    'HOST': 'localhost',
    'PORT': 5432
}

# Folder where backups will be stored
BACKUP_DIR = '/backups'

# Back up the database.
def backup_database():
    backup_file = os.path.join(BACKUP_DIR, f"{DATABASE['NAME']}_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql")

    # pg_dump comand
    command = [
        'pg_dump',
        '-U', DATABASE['USER'],
        '-h', DATABASE['HOST'],
        '-p', str(DATABASE['PORT']),
        '-F', 'c',  # Custom format
        '-f', backup_file,
        DATABASE['NAME']
    ]

    # Configures the PGPASSWORD environment variable
    os.environ['PGPASSWORD'] = DATABASE['PASSWORD']

    try:
        subprocess.run(command, check=True)
        print(f"Backup performed successfully: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error when backing up: {e}")

if __name__ == '__main__':
    backup_database()
