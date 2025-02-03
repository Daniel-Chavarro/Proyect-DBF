import psycopg2 # type: ignore

class PostgresDatabaseConection():
    def __init__(self):
        self._dbname = 'crud'
        self._duser = 'postgres'
        self._dpassword = 'P4$$w0rd'
        self._dhost = 'localhost'
        self._dport = '5432'
        self._connection = None
    
    def connect(self):
        try:
            self._connection = psycopg2.connect(
                dbname=self._dbname,
                user=self._duser,
                password=self._password,
                port=self._dport,
                host=self._dhost
            )
        except psycopg2.Error as e:
            print(f'Error: {e}')