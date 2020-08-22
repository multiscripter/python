import psycopg2


class DBDriver:
    """PostgreSQL database driver"""

    def __init__(self, params={}):
        """Initializes instance

        :param params: collection with connection parameters named:
        dbname, host, password, port, user.
        :type params: dictionary
        """

        self.con = False
        self.params = {
            'dbname': False,
            'host': False,
            'password': False,
            'port': False,
            'user': False
        }
        if len(params):
            for key in self.params:
                if key in params:
                    self.params[key] = params[key]

    def close(self):
        """Closes connection with database.
        """

        if self.con and not self.con.closed:
            self.con.close()

    def delete(self, query=''):
        """Deletes from database

        :param query: SQL query string.
        :type query: str
        :returns: number of affected rows
        :rtype: int
        """

        return self.executeSql(query)['affected']

    def executeSql(self, query=''):
        """Executes SQL query

        :param query: SQL query string.
        :type query: str
        :returns: result dictionary
        :rtype: dict
        """

        query = self.stripQuery(query)
        if not self.con or self.con.closed:
            self.setConnection()
        result = {}
        try:
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            if 'select' in cur.statusmessage.lower():
                result['columns'] = cur.description
                result['rows'] = cur.fetchall()
            result['affected'] = cur.rowcount
        except:
            self.con.rollback()
            raise
        finally:
            cur.close()
            self.close()
        return result

    def executeSqlScript(self, name):
        """Executes SQL queries from file

        :param name: SQL script name.
        :type name: str
        :returns: number of affected rows
        :rtype: int
        """

        with open(name) as f:
            queries = f.read()
        return self.executeSql(queries)['affected']

    def insert(self, query=''):
        """Inserts data into database

        :param query: SQL query string.
        :type query: str
        :returns: number of affected rows
        :rtype: int
        """

        return self.executeSql(query)['affected']

    def isConnected(self):
        """Checks connection openness.

        :returns: True if connection is opened. Otherwise False.
        :rtype: bool
        """

        return self.con and not self.con.closed

    def select(self, query=''):
        """Selects data from database.

        :param query: SQL query string.
        :type query: str
        :returns: [{ colName: colVal[, colName: colVal]}[, { . . . }]]
        :rtype: dict list
        """

        fetched = self.executeSql(query)
        cols = fetched['columns']
        result = []
        for row in fetched['rows']:
            entry = {}
            a = 0
            for val in row:
                entry[cols[a][0]] = val
                a += 1
            result.append(entry)
        return result

    def setConnection(self):
        """Sets connection with database"""

        if self.isConnected():
            return
        params = []
        for key in self.params:
            if self.params[key]:
                params.append(f'{key}={self.params[key]}')
        params = ' '.join(params)
        if params:
            self.con = psycopg2.connect(params)
        else:
            raise Exception('No params for connection')

    def stripQuery(self, query=''):
        """Deletes trailing spaces from query string

        :param query: SQL query string.
        :type query: str
        :returns: stripped SQL query string.
        :rtype: str
        """

        query = query.strip()
        if not query:
            raise Exception('Empty query')
        return query

    def update(self, query=''):
        """Updates data in database

        :param query: SQL query string.
        :type query: str
        :returns: number of affected rows
        :rtype: int
        """

        return self.executeSql(query)['affected']
