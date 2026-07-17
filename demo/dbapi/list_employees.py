import sqlite3
import dbutil

con = None
cur = None

try:
    con = sqlite3.connect(dbutil.DBNAME)
    cur = con.cursor()

    cur.execute("SELECT * FROM employees")

    for emp_id, name, job, salary in cur.fetchall():
        print(f"{emp_id:2} {name:20} {job:10} {salary:10}")

except Exception as ex:
    print("Error:", ex)

finally:
    if cur is not None:
        print('Closing cursor')
        cur.close()

    if con is not None:
        print('Closing connection')
        con.close()

