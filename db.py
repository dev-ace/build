import MySQLdb
from config import CREDS

def conn():
    conn = MySQLdb.connect(host=CREDS.get('host'), user=CREDS.get('user'), passwd=CREDS.get('pass'), db=CREDS.get('db'))
    return conn

def read(table_name='celery_taskmeta'):
    con = conn()
    cursor = con.cursor()
    statement = ('SELECT task_id, status, date_done, result FROM ' + table_name + ' WHERE date_done >= now() - INTERVAL 1 HOUR')
    cursor.execute(statement)
    output = cursor.fetchall()
    con.commit()
    con.close()
    toreturn = []
    for tup_row in output:
        row = list(tup_row)
        result = row.pop()
        results = result.split('//')
        results = results[1:-1]
        for result in results:
            row.append(result)
        toreturn.append(row)
    return toreturn
