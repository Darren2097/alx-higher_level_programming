#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) > 3:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
        cur = conn.cursor()
        cur.execute("""SELECT * FROM states WHERE name LIKE 'N%'
                ORDER BY states.id ASC""")
        rows = cur.fetchall()
        for row in rows:
            if row[1][0] == "N":
                print(row)

        cur.close()
        conn.close()
