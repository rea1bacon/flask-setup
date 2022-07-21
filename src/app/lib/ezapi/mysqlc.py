import mysql.connector


def CheckConnection(host: str, port: int, login: str, password: str, db: str):
    """Check connection to database

    Args:
        host (str): host
        port (int): port
        login (str): login
        password (str): password
        db (str): dbname

    Returns:
        object: mysql.connector.connection_cext.CMySQLConnection if connection is valid
        bool: False if connection failed
    """
    try:
        TestCnx = mysql.connector.connect(
            user=login, database=db, host=host, port=port, password=password)
        return TestCnx
    except mysql.connector.errors.DatabaseError:
        return False


def ReadDB(query: str, connection, params):
    """ Read database

    Args:
        query (str): sql query
        connection (object): mysql.connector object
        params (list): query parameters

    Returns:
        list: fetch
    """
    try:
        DBcursor = connection.cursor()
        DBcursor.execute(query, params)

        return DBcursor.fetchall()
    except Exception as e:
        raise e


def WriteDB(query: str, connection, params):
    """ Write in Database

    Args:
        query (str): sql query
        connection (object): mysql.connector object
        params (list): query params
    """
    try:
        DBcursor = connection.cursor()
        DBcursor.execute(query, params)
        connection.commit()
        return True
    except Exception as e:
        raise e
