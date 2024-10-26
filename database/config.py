import psycopg2

# Database Settings
DATABASE = {
    'NAME': 'db_pr',
    'USER': 'dbpr',
    'PASSWORD': '321',
    'HOST': 'localhost',
    'PORT': 5432
}

# Execute a SQL file
def execute_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
    with psycopg2.connect(
        dbname=DATABASE['NAME'],
        user=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        host=DATABASE['HOST'],
        port=DATABASE['PORT']
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()

# Runs the init.sql and debug.sql scripts
if __name__ == '__main__':
    try:
        execute_sql_file('sql/init.sql')
        execute_sql_file('seeds/debug.sql')
        print("Scripts executed succesfully!")
    except Exception as e:
        print(f"Error: {e}")
