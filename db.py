import MySQLdb
from config import CREDS

def conn():
    conn = MySQLdb.connect(host=CREDS.get('host'), user=CREDS.get('user'), passwd=CREDS.get('pass'), db=CREDS.get('db'))
    return conn

def read_completed(table_name='celery_taskmeta'):
    con = conn()
    cursor = con.cursor()
    statement = ('SELECT task_id, status, date_done, result FROM ' + table_name + ' WHERE date_done >= now() + INTERVAL 4 HOUR')
    cursor.execute(statement)
    output = cursor.fetchall()
    statement = ('SELECT task_id, ip_addr, requested FROM in_progress')
    cursor.execute(statement)
    output2 = cursor.fetchall()
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

def read_in_progress(table_name='in_progress'):
    con = conn()
    cursor = con.cursor()
    statement = ('SELECT task_id, ip_addr, requested FROM in_progress')
    cursor.execute(statement)
    output = cursor.fetchall()
    con.commit()
    con.close()
    return output

def write_in_progress(requested, ip_addr, task_id, table_name='in_progress'):
    con = conn()
    cursor = con.cursor()
    statement = ("INSERT INTO " + table_name + " (task_id, ip_addr, requested) VALUES('" + task_id + "','" + ip_addr[:-1] + "','" + ", ".join(requested) + "')")
    cursor.execute(statement)
    output=cursor.fetchall()
    con.commit()
    con.close()
    return output

def del_in_progress(task_id, table_name='in_progress'):
    con = conn()
    cursor = con.cursor()
    statement = ("DELETE FROM " + table_name + " WHERE task_id='" + task_id + "'")
    cursor.execute(statement)
    output=cursor.fetchall()
    con.commit()
    con.close()
    return output
